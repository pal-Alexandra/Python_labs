# 4.Write a Python script that counts the number of files with each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv).
# Use the os module to list all files in the directory.
# Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.
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

    directory_path = "D:\Ale\Facultate\An III sem I\ML"

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"Invalid directory path: {directory_path} does not exist")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Invalid directory path: {directory_path} is not a directory")

        directory_files = files_from_directory(directory_path)

        if len(directory_path) == 0:
            raise Exception(f"Directory {directory_path} is empty")

        directory_extensions = dict()
        for file in directory_files:
            extension = file.split(".")[-1]
            if extension in directory_extensions:
                directory_extensions[extension] += 1
            else:
                directory_extensions[extension] = 1

        print(directory_extensions)

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(e)



main()
