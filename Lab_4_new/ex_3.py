#Write a Python class that simulates a matrix of size NxM,
# with N and M provided at initialization.
# The class should provide methods to
# access elements (get and set methods)
# and some methematical functions such as transpose, matrix multiplication
# and a method that allows iterating through all elements form a matrix an apply
# a transformation over them (via a lambda function).
import random


class Matrix:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.matrix = [[None for i in range(M)] for j in range(N)]

    def get(self, i, j):
        if i >= self.N or j >= self.M or i < 0 or j < 0:
            print("Index out of bounds")
            return None
        return self.matrix[i][j]

    def set(self, i, j, value):
        if self.N > i >= 0 and self.M > j >= 0:
            self.matrix[i][j] = value
        else:
            print("Index out of bounds")

    def print(self):
        for i in range(self.N):
            for j in range(self.M):
                print(self.get(i, j), end=" ")
            print()

    def transpose(self):
        new_matrix = Matrix(self.M, self.N)
        for i in range(self.N):
            for j in range(self.M):
                new_matrix.set(j, i, self.get(i, j))
        return new_matrix

    def multiply(self, other):
        if self.M != other.N:
            print("Matrices cannot be multiplied")
            return None
        else:
            new_matrix = Matrix(self.N, other.M)
            for i in range(self.N):
                for j in range(other.M):
                    sum = 0
                    for k in range(self.M):
                        if (isinstance(self.get(i, k), int) or isinstance(self.get(i, k), float)) and (isinstance(other.get(k, j), int) or isinstance(other.get(k, j), float)):
                            sum += self.get(i, k) * other.get(k, j)
                        else:
                            print(self.get(i, k))
                            print(other.get(k, j))
                            print("Matrices cannot be multiplied. Not all elements are not numbers")
                            return None
                    new_matrix.set(i, j, sum)
            return new_matrix

    def apply(self, lambda_function):
        for i in range(self.N):
            for j in range(self.M):
                self.set(i, j, lambda_function(self.get(i, j)))


matrix1 = Matrix(2, 3)
matrix2 = Matrix(3, 4)

for i in range(matrix1.N):
    for j in range(matrix1.M):
        x = random.randint(0, 11)
        matrix1.set(i, j, x)


for i in range(matrix2.N):
    for j in range(matrix2.M):
        x = random.randint(11, 31)
        matrix2.set(i, j, x)

print("MATRIX 1")
matrix1.print()
print()

print("MATRIX 2")
matrix2.print()
print()

matrix3 = matrix1.transpose()
print("MATRIX1 TRANSPOSED (aka matrix3)")
matrix3.print()
print()


matrix4 = matrix1.multiply(matrix2)
print("MATRIX1 MULTIPLIED BY MATRIX2 (aka matrix4)")
matrix4.print()
print()

matrix4.apply(lambda t: t + t % 2)
print("MATRIX4 AFTER APPLYING LAMBDA FUNCTION")
matrix4.print()
print()
