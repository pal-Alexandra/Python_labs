import os
import sys


def text_dir(path):
    text = str()
    for file in os.listdir(path):
        try:
            file_n = os.path.join(path, file)
            if os.path.isfile(file_n):
                f = open(file_n, "r")
                text1 = f.read()
                text += text1
                f.close()

        except PermissionError as e:
            print("error at reading")

    return text


def text_file(path):
    try:

        f = open(path, "r")
        text = f.read()
        f.close()

    except PermissionError as e:
        print("error at reading")
    return text


def main():
    try:

        if len(sys.argv < 4):
            raise Exception("NOT ENOUGH ARGUMENTS")

        path = sys.argv[1]
        symbol = sys.argv[2]
        reverse = sys.argv[3]

        if not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} does not exists")

        if os.path.isdir(path):
            text = text_dir(path)

        if os.path.isfile(path):
            text = text_file(path)

        if symbol == 'char':
            symbols = dict()
            for char in text:
                if char != ' ' and char != '\n':
                    if char in symbols:
                        symbols[char] += 1
                    else:
                        symbols[char] = 1

        elif symbol == 'word':
            symbols = dict()
            words = text.split()
            for word in words:
                if word in symbols:
                    symbols[word] += 1
                else:
                    symbols[word] = 1

        if reverse == 'false':
            symbols = sorted(symbols, key=lambda x: x[1], reverse=False)
        else:
            symbols = sorted(symbols, key=lambda x: x[1], reverse=True)

        for (key, value) in symbols:
            print(f"{key} {value}")

    except (FileNotFoundError, Exception) as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    main()
