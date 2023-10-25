# Să se scrie o funcție ce primește un parametru cu numele dir_path.
# Acest parametru reprezintă calea către un director aflat pe disc.
# Funcția va returna o listă cu toate căile absolute ale fișierelor
# aflate în rădăcina directorului dir_path.
import os


def ex_8(dir_path):
    list = []
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        for root, directories, files in os.walk(dir_path):
            for file in files:
                # print(root)
                # print(file)
                file_path = os.path.join(root, file)
                list.append(file_path)
        return list


result = ex_8("D:\Ale\Facultate\An III sem I\A3D")
for file in result:
    print(file)
