# Să se scrie o funcție ce primește ca argumente două căi:
# director si fișier.
#  Implementati functia astfel încât în fișierul de la calea fișier
#  să fie scrisă pe câte o linie, calea absolută a fiecărui fișier
#  din interiorul directorului de la calea folder, ce incepe cu litera A.
import os


def ex_2(directory, file):
    f = open(file, "a")

    if os.path.exists(directory) and os.path.isdir(directory):
        for root, directories, files in os.walk(directory): # For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames)
            # print(root)
            # print(directories)
            # print(files)
            for file in files:
                if file.startswith('A'):
                    file_path = os.path.join(root, file)
                    f.write(file_path)
                    f.write("\n")
    f.close()
    print("Done")


directory = "D:\Ale\Facultate\An III sem I\Test_PY_lab_4"
output_file = "D:\Ale\Facultate\An III sem I\Test_PY_lab_4\Output_ex_2.txt"
ex_2(directory, output_file)
