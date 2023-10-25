# Să se scrie o funcție ce returnează o listă cu extensiile
# unice a fișierelor din directorul dat ca argument la linia de comandă
# (nerecursiv). Lista trebuie să fie sortată crescător.
import os
import sys


def ex_4(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        extensions = set()
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                # print(file)
                extension = file.split('.')[-1]
                extensions.add(extension)

        return sorted(list(extensions))


print(ex_4("D:\Ale\Facultate\An III sem I\AI\sap_2"))
#print(ex_4(sys.argv[1])) --nu o sa mearga asta pt ca am spatii albe in numele directorului dat