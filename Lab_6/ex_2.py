# 2. Write a script using the os module that renames
# all files in a specified directory to have a sequential number prefix.
# For example, file1.txt, file2.txt, etc.
# Include error handling for cases like the directory not existing
# or files that can't be renamed.

import os


def files_from_directory(directory_path):
    files_list = []
    for root, directories, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)
    return files_list

def main():
    directory_path = "D:\\test_py_lab_6"
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Invalid directory path: {directory_path} does not exist")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Invalid directory path: {directory_path} is not a directory")

        directory_files = files_from_directory(directory_path)

        for index, file in enumerate(directory_files):
            # print("\n")
            # print(file)
            file_name = os.path.basename(file)
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = f"file{index + 1}{file_extension}"
            new_file_path = os.path.join(os.path.dirname(file), new_file_name)
            # print(new_file_path)
            try:
                os.rename(file, new_file_path)
            except PermissionError as e:
                print(f"Error at renaming file {file}: {e}")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")


main()