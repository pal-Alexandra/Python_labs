# ﻿Să se scrie o funcție ce primește ca parametru
# un string my_path.
# Dacă parametrul reprezintă calea către un fișier, se vor returna
# ultimele 20 de caractere din conținutul fișierului.
# Dacă parametrul reprezintă calea către un director, se va returna
# o listă de tuple (extensie, count), sortată descrescător după count,
# unde extensie reprezintă extensie de fișier, iar count - numărul de
# fișiere cu acea extensie. Lista se obține din toate fișierele (recursiv)
# din directorul dat ca parametru.
import os


def ex_3(my_path):
    if os.path.exists(my_path):
        if os.path.isfile(my_path):
            f = open(my_path, 'r')
            return f.read()[-20:]
        elif os.path.isdir(my_path):
            extensions = {}
            for root, directories, files in os.walk(my_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    extension = file_path.split('.')[-1]
                    if extension not in extensions:
                        extensions[extension] = 1
                    else:
                        extensions[extension] +=1
            list = [(extension, count) for extension, count in extensions.items()]
            sorted_list = sorted(list, key=lambda x: x[1], reverse=True)
            #sorted sorteaza pe baza cheii key: functie lambda care ret al 2-lea elm din fiecare tupla
            return sorted_list


director = "D:\Ale\Facultate\An III sem I\ML"  # Înlocuiți cu calea către directorul dorit
print(ex_3(director))
