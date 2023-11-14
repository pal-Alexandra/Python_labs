# 1.Create a Python script that does the following:
# Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.
import os
import sys


def files_from_directory(directory_path):
    files_list = []
    for root, directories, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)
    return files_list


def main():
    # directory_path = sys.argv[1]
    # file_extension = sys.argv[2]

    directory_path = "D:\Ale\Facultate\An III sem I\AI\sap_2"
    file_extension = ".txt"


    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Invalid directory path: {directory_path} does not exist")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Invalid directory path: {directory_path} is not a directory")

        if not file_extension.startswith("."):
            raise ValueError(f"Invalid file extension: {file_extension} must start with a dot")

        directory_files = files_from_directory(directory_path)

        print(f"All files found in {directory_path}:\n {directory_files}\n\n")
        for file in directory_files:
            if file.endswith(file_extension):
                try:
                    f = open(file, "r", encoding="utf8")
                    content = f.read()
                    print(f"Content of file {file} is:\n {content}\n\n")

                except PermissionError as e:
                    print(f"Error at reading file {file}: {e}")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")


main()

