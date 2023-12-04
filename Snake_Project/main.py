import json
import os
import sys

from SnakeGame import SnakeGame


def read_file(file_name):

    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
            width = data['width']
            height = data['height']
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

        snake_game = SnakeGame(window_width, window_height, obstacles)
        snake_game.start_game()
        snake_game.window.mainloop()

    except FileNotFoundError as e:
        print(e)

