# # Să se scrie o funcție care primește ca argumente
# # două șiruri de caractere, target și to_search și
# # returneaza o listă de fișiere care conțin to_search.
# # Fișierele se vor căuta astfel: dacă target este un fișier,
# # se caută doar in fișierul respectiv iar dacă este un director
# # se va căuta recursiv in toate fișierele din acel director.
# # Dacă target nu este nici fișier, nici director, se va arunca
# # o excepție de tipul ValueError cu un mesaj corespunzator.
# import os
#
#
import os


def ex_5(target, to_search):
    list = []
    if os.path.isfile(target):
        if to_search_in_file(target, to_search):
            list.append(target)
            return list
    elif os.path.isdir(target):
        for root, directories, files in os.walk(target):
            for file in files:
                file_path = os.path.join(root, file)
                if to_search_in_file(file_path, to_search):
                    list.append(file_path)
        return list
    elif not os.path.isfile(target) and not os.path.isdir(target):
        raise ValueError(f'The given path is not a file or a directory: {target}')

def to_search_in_file(file_path, to_search):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
            if to_search in data:
                return True
    except (OSError, UnicodeDecodeError):
        pass
    return False




directory = 'D:\Ale\Facultate\An III sem I\Test_PY_lab_4'
file = 'D:\Ale\Facultate\An III sem I\Test_PY_lab_4\B.txt'
dummy = 'ceva aiurea'
to_search = 'buna ziua'
try:
    matching_files = ex_5(directory, to_search)
    if matching_files:
        print("Fisierele din directorul dat care conțin /buna ziua/ sunt:")
        for file in matching_files:
            print(file)
    else:
        print("Nu exista fișiere care conțin /buna ziua/.")

    matching_files = ex_5(file, to_search)
    if matching_files:
        print(f"Fisierul {file} contine /buna ziua/")
    else:
        print(f"Fisierul {file}  NU contine /buna ziua/ :")

    ex_5(dummy, to_search)

except ValueError as e:
    print(f"Eroare: {e}")


