import os


def compare_files(file1, file2, output1, output2):
    """
    Compares two files line by line in a streaming manner and writes the unique
    lines of each file into two separate output files. This is memory-efficient for large files.
    """
    file_exists(file1)
    file_exists(file2)

    with open(file1, 'r', encoding="utf-8") as f1, open(file2, 'r', encoding="utf-8") as f2, \
         open(output1, 'w', encoding="utf-8") as o1, open(output2, 'w', encoding="utf-8") as o2:
        line1 = f1.readline()
        line2 = f2.readline()

        while line1 or line2:
            if not line2 or (line1 and line1 < line2):
                o1.write(line1)
                line1 = f1.readline()
            elif not line1 or (line2 and line2 < line1):
                o2.write(line2)
                line2 = f2.readline()
            else:  # lines are equal
                line1 = f1.readline()
                line2 = f2.readline()

def file_exists(file_path):
    """
    Check if a file exists at the given path.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def get_output_file_name(input_file):
    """
    Generate output file name based on the input file name.
    """
    return f"data/output/unique_{os.path.basename(input_file)}"

def main():
    file1 = input("Enter path for the first input file: ")
    file2 = input("Enter path for the second input file: ")

    output1 = get_output_file_name(file1)
    output2 = get_output_file_name(file2)

    try:
        compare_files(file1, file2, output1, output2)
        print("File Comparison Completed Successfully.")
        print(f"Lines unique to '{file1}' have been written to '{output1}'.")
        print(f"Lines unique to '{file2}' have been written to '{output2}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
