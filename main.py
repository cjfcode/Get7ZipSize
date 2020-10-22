# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#  Get7ZipSize
#
#  This program calculates the required HDD space to store
#  extracted files from a directory of compressed
#  files in 7z format.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import time
from subprocess import Popen, PIPE


# entry point of the application
def main():
    start_time = time.time()
    print_header()
    path = input("Enter the path to 7z.exe: ")  # Example: C:\Program Files\7-Zip\7z.exe
    working_dir = input("Enter the path to the archives: ")  # Example: Y:\software\games\iso\xbox
    columns = "\n{0:54} Size\n".format("Title")
    border = "{0:54} {1}".format('=' * 5, '=' * 4)
    print(columns + border)
    filenames = get_filenames(working_dir)
    sizes = []
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
    print("\nTotal Size Required: " + all_sizes)
    end_time = time.time()
    running_time = end_time - start_time
    print("File count: " + str(file_count))
    print("Completed execution in " + "{:.2f}".format(running_time) + " seconds.")


# displays program information header
def print_header():
    title = "Get7ZipSize"
    version = "Version 1.0"
    description = "This program calculates the required HDD space \n" \
                  "to store extracted files from a directory \n" \
                  "of compressed files in 7z format.\n"
    border = '=' * 45
    print("{0} {1}\n{3}\n{2}".format(title, version, description, border))


# returns a list of the filenames including file extension
def get_filenames(working_dir):
    os.chdir(working_dir)
    process = Popen(['cmd', '/c', 'dir'], stdout=PIPE)
    lines = process.stdout.readlines()[7:-2]
    filenames = []
    for name in lines:
        filenames.append(str(name[39:].decode('utf-8').strip()))
    return filenames


# returns filesize in gigabytes given an input size in bytes
def to_gigabyte(filename, size_in_bytes):
    gigabyte_in_bytes = 1073741824
    size_in_gigabytes = size_in_bytes / gigabyte_in_bytes
    output_str = "{0:54} {1}"
    print(output_str.format(filename, "{:.2f} GB".format(size_in_gigabytes)))
    return size_in_gigabytes


# returns the total required space (in GB) given a list of sizes (in GB)
def compute_total_size(sizes):
    total = 0
    for size in sizes:
        total += size
    return "{:.3f}".format(total) + " GB"


if __name__ == '__main__':
    main()
