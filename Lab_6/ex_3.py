# 3. Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:


# Use the sys module to read the directory path from the command line. Utilize the os module to iterate through all
# the files in the given directory and its subdirectories. Sum up the sizes of all files and display the total size
# in bytes. Implement exception handling for cases like the directory not existing, permission errors, or other file
# access issues.

import os


def files_from_directory(directory_path):
    files_list = []
    for root, directories, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)
    return files_list


def main():
    # directory_path = sys.argv[1]
    directory_path = "D:\Ale\Facultate\An III sem I\AI"

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Invalid directory path: {directory_path} does not exist")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Invalid directory path: {directory_path} is not a directory")

        directory_files = files_from_directory(directory_path)

        print(f"Total size of all files found in {directory_path}:\n\n")
        total_size = 0
        for file in directory_files:
            try:
                total_size += os.path.getsize(file)
            except PermissionError as e:
                print(f"Error getting size of the file {file}: {e}")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")

    print(f"Total size of all files found in {directory_path}: {total_size} bytes")


main()
