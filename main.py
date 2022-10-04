import os
import time
from subprocess import Popen, PIPE


def main():
    print_header()
    path = input("Enter the path to 7z.exe: ")  # Example: C:\Program Files\7-Zip\7z.exe
    working_dir = input("Enter the path to the archives: ")  # Example: Y:\software\games
    print_table_header()
    start_time = time.time()
    sizes = []
    filenames = get_filenames(working_dir)
    os.chdir(working_dir)
    file_count = 0
    for file in filenames:
        process = Popen([path, 'l', file], stdout=PIPE)
        output = process.stdout.readlines()
        size_in_bytes = None
        index = 0
        while size_in_bytes is None:
            try:
                size_in_bytes = int(str.split(str(output[len(output) - 3]))[index])
            except ValueError:
                index += 1
                pass
        sizes.append(to_gigabyte(file, size_in_bytes))
        file_count += 1
    all_sizes = compute_total_size(sizes)
    runtime = compute_runtime(start_time)
    print_footer(runtime, file_count, all_sizes)


def print_header():
    title = "Get7ZipSize"
    version = "Version 1.0"
    description = "This program calculates the required HDD space \n" \
                  "to store extracted files from a directory \n" \
                  "of compressed files in 7z format.\n"
    border = '=' * 45
    print("{0} {1}\n{3}\n{2}".format(title, version, description, border))


def print_table_header():
    columns = "\n{0:54} Size\n".format("Title")
    border = "{0:54} {1}".format('=' * 5, '=' * 4)
    print(columns + border)


def print_footer(runtime, file_count, all_sizes):
    print("\nTotal Size Required: " + all_sizes)
    print("File count: " + str(file_count))
    print("Completed execution in " + "{:.2f}".format(runtime) + " seconds.")


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


def to_gigabyte(filename, size_in_bytes):
    gigabyte_in_bytes = 1073741824
    size_in_gigabytes = size_in_bytes / gigabyte_in_bytes
    output_str = "{0:54} {1}"
    print(output_str.format(filename, "{:.2f} GB".format(size_in_gigabytes)))
    return size_in_gigabytes


def compute_total_size(sizes):
    total = 0
    for size in sizes:
        total += size
    return "{:.3f}".format(total) + " GB"


if __name__ == '__main__':
    main()
