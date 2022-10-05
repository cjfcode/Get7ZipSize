import os
import time
from subprocess import Popen, PIPE


def main():
    print_header()
    path = input("Enter the path to 7z.exe: ")  # Example: C:\Program Files\7-Zip\7z.exe
    working_dir = input("Enter the path to the archives: ")  # Example: Y:\software\games
    print_table_header()
    start_time = time.time()
    filenames = get_filenames(working_dir)
    os.chdir(working_dir)
    print_files(filenames)
    supported_filetypes = working_dir + '\\*'
    size_in_bytes = get_size_in_bytes(path, supported_filetypes)
    size = to_gigabyte(size_in_bytes)
    file_count = count_files(filenames)
    runtime = compute_runtime(start_time)
    print_footer(runtime, file_count, size)


def print_header():
    title = "Get7ZipSize"
    version = "Version 1.0"
    description = "This program calculates the required HDD space \n" \
                  "to store extracted files from a directory \n" \
                  "of compressed files in 7z format.\n"
    border = '=' * 45
    print("{0} {1}\n{3}\n{2}".format(title, version, description, border))


def print_table_header():
    columns = "\nTitle\n"
    border = '=' * 5
    print(columns + border)


def print_footer(runtime, file_count, size):
    formatted_size = "{:.2f} GB".format(size)
    print("\nFile count: " + str(file_count))
    print("Total Size Required: " + formatted_size)
    print("Completed execution in " + "{:.2f}".format(runtime) + " seconds.\n")


def get_size_in_bytes(path, supported_filetypes):
    try:
        process = Popen([path, 'l', supported_filetypes], stdout=PIPE)
        output = process.stdout.readlines()
        size_in_bytes = int(str.split(str(output[len(output) - 5]))[2])
        return size_in_bytes
    except (ValueError, IndexError) as error:
        print("Check that the folder contains all valid archives and try again.")
        return 0


def count_files(filenames):
    count = 0
    for file in filenames:
        count += 1
    return count


def print_files(filenames):
    for filename in filenames:
        print(filename)


def compute_runtime(start_time):
    end_time = time.time()
    running_time = end_time - start_time
    return running_time


def get_filenames(working_dir):
    os.chdir(working_dir)
    process = Popen(['cmd', '/c', 'dir'], stdout=PIPE)
    lines = process.stdout.readlines()[7:-2]
    filenames = []
    for filename in lines:
        filenames.append(str(filename[39:].decode('utf-8').strip()))
    return filenames


def to_gigabyte(size_in_bytes):
    gigabyte_in_bytes = 1073741824
    try:
        size_in_gigabytes = size_in_bytes / gigabyte_in_bytes
        return size_in_gigabytes
    except TypeError:
        print("Invalid byte size provided.")


if __name__ == '__main__':
    main()
