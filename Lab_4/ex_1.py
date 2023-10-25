# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor
# din directorul dat ca parametru.
import os


def ex_1(directory):
    extensions = set()

    if os.path.exists(directory) and os.path.isdir(directory):
        for root, directories, files in os.walk(directory): # For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames)
            # print(root)
            # print(directories)
            # print(files)
            for file in files:
                file_path = os.path.join(root, file)
                #print(file_path)
                extension = file_path.split('.')[-1] #impart path-ul prin separatorul . si iau ultimul elm din lista returnata de split
                extensions.add(extension)

    extensions = sorted(list(extensions))
    return extensions

director_1 = "D:\Ale\Facultate\An III sem I\AI\sap_2"  # Înlocuiți cu calea către directorul dorit
extensii_1 = ex_1(director_1)
print(extensii_1)

print("``````````````````````````````````````````````````````````````")

director_2 = "D:\Ale\Facultate\An III sem I\ML"  # Înlocuiți cu calea către directorul dorit
extensii_2 = ex_1(director_2)
print(extensii_2)