import json
import os
import sys


def read_file(file_name):

    try:
        with open(file_name, 'r') as f:
            data = json.load(file_name)
            width = data['window_width']
            height = data['window_height']
            obstacles = data.get('obstacles', [])

        return width, height, obstacles

    except PermissionError as e:
        print(f"Error ar reading file: {file_name}")


if __name__ == '__main__':
    file = sys.argv[1]

    try:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File {file} not found")

        if not os.path.isfile(file):
            raise FileNotFoundError(f"{file} is not a file")

        if not file.endswith('.json'):
            raise FileNotFoundError(f"{file} is not a json file")

        window_width, window_height, obstacles = read_file(file)

    except FileNotFoundError as e:
        print(e)

