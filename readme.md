# Get7ZipSize

This script uses 7zip's 'l' flag to parse information about compressed files in a folder. It's useful if you want to know how much space it would take to store all of the uncompressed data without actually having to extract the data.

## Instructions
1. Start the program from start.bat or by running main.py in python from the command prompt.
2. Input the paths to the 7Zip executable and the folder containing the compressed files.
3. Wait while the program outputs the data!

### Prerequisites
Requires Python and 7zip.

### Warnings
* This program is intended to be used with directories that only contain archives (for example, .zip, .rar, .7z). Running it on directories containing individual files may produce errors or incorrect results.
* Only tested on .7z format archives. It may work with other formats, but it's not tested.