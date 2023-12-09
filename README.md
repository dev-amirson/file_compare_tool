# File Comparison Tool

## Overview
This tool is designed to compare two large text files and identify unique lines in each file. It's particularly efficient for handling very large files as it reads and processes the files line by line, minimizing memory usage. This makes it suitable for comparing files that are too large to be loaded entirely into memory.

## Key Features
- **Efficient File Handling:** Capable of handling very large files efficiently by processing them in a streaming manner.
- **Line-by-Line Comparison:** Compares files line by line, outputting unique lines in each file to separate output files.
- **Minimal Memory Usage:** Uses a minimal amount of memory, making it suitable for environments with limited resources.
- **Error Handling:** Includes basic error handling, such as checking if files exist.

## Requirements
- Python 3.x installed on your system.
- Two text files that you wish to compare. The files should be sorted lexicographically for the tool to work correctly.

## Installation
No specific installation is required, as the script is a standalone Python file. Simply ensure that Python 3.x is installed on your system.

## Usage
1. **Prepare Your Files:** Ensure that the text files you want to compare are sorted lexicographically and are accessible on your system.
2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python: `python3 file_compare_tool.py`
3. **Input File Paths:**
   - When prompted, enter the full path to the first input file. `data/input/input1.txt`
   - Next, enter the full path to the second input file. `data/input/input2.txt`
4. **Output:**
   - The script will create two output files in `data/output/`.
   - The output files will be named `unique_[input_file_name]`, corresponding to each input file.
   - Each output file will contain the lines that are unique to that particular input file.

## Limitations
- The tool assumes that the input files are sorted. If the files are not sorted, the output may not be accurate.
- The script does not perform in-memory sorting of unique lines due to memory efficiency considerations. If sorted output is required, it can be done separately.

## Troubleshooting
- **File Not Found:** Ensure that the paths to the input files are correct and that the files exist.
- **Permission Errors:** Make sure you have the necessary permissions to read the input files and write to the output directory.
