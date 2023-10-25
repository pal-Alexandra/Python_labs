# Să se scrie o funcție care primește ca parametru un șir
# de caractere care reprezintă calea către un fișer si
# returnează un dicționar cu următoarele cămpuri:
# full_path = calea absoluta catre fisier,
# file_size = dimensiunea fisierului in octeti,
# file_extension = extensia fisierului (daca are) sau "",
# can_read, can_write = True/False
# daca se poate citi din/scrie in fisier.
import os.path


def ex_7(file_path):
    file_information = {}
    if os.path.exists(file_path) and os.path.isfile(file_path):
        full_path = os.path.abspath(file_path)
        file_size = os.path.getsize(file_path)
        extension = file_path.split('.')[-1]
        if extension == file_path:
            extension = ''
        can_read = os.access(file_path, os.R_OK)
        can_write = os.access(file_path, os.W_OK)

        file_information['full_path'] = full_path
        file_information['file_size'] = file_size
        file_information['extension'] = extension
        file_information['can_read'] = can_read
        file_information['can_write'] = can_write

        return file_information


file = "D:\Ale\Facultate\An III sem I\A3D\Imagini proiect\goldfishlateral.jpg"
result = ex_7(file)
for key, value in result.items():
    print(key + " : " + str(value))

