# Să se scrie o funcție care are același comportament
# ca funcția de la exercițiul anterior, cu diferența că
# primește un parametru în plus: o funcție callback,
# care primește un parametru, iar pentru fiecare
# eroare apărută în procesarea fișierelor,
# se va apela funcția respectivă cu instanța excepției ca parametru.
import os


def handle_exception(e):
    print(f"Error handled by callback")
    raise e


def ex_5(target, to_search, callback_function):
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
        callback_function(ValueError(f'The given path is not a file or a directory: {target}'))

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
    matching_files = ex_5(directory, to_search, handle_exception)
    if matching_files:
        print("Fisierele din directorul dat care conțin /buna ziua/ sunt:")
        for file in matching_files:
            print(file)
    else:
        print("Nu exista fișiere care conțin /buna ziua/.")

    matching_files = ex_5(file, to_search, handle_exception)
    if matching_files:
        print(f"Fisierul {file} contine /buna ziua/")
    else:
        print(f"Fisierul {file}  NU contine /buna ziua/ :")

    ex_5(dummy, to_search, handle_exception)

except ValueError as e:
    print(f"Eroare: {e}")

