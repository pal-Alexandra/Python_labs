# Given a square matrix of characters write a script that prints the
# string obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

# I will be using the simulation approach:
# Draw the path that the spiral makes. We know that the path should turn clockwise
# whenever it would go out of bounds or into a cell that was previously visited

def spiral_order(matrix):
    string = ''

    rows = len(matrix)
    columns = len(matrix[0])
    seen = [[0 for i in range(columns)] for j in range(rows)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x, y, di = 0, 0, 0

    # we want to visit rows x columns cells => Iterate from 0 to R * C - 1
    for i in range(rows * columns):
        string += matrix[x][y]
        seen[x][y] = True
        #compute candidate next position
        cr = x + dr[di]
        cc = y + dc[di]

        if (0 <= cr and cr < rows and 0 <= cc and cc < columns and not (seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]

    print('For the input matrix: ')
    print(matrix)
    print('We obtain the string: /' + string + '/')


matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]
spiral_order(matrix)
