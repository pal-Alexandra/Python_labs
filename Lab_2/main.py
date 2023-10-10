# 1.Write a function to return a list of the first n numbers in the Fibonacci string.

def firsts_n_fibonacci(n):
    fibonacci_list = [1]
    if n == 1:
        return fibonacci_list
    elif n == 2:
        fibonacci_list = fibonacci_list.append(1)
        return fibonacci_list
    elif n >= 3:
        fibonacci_list.append(1)
        a, b = 1, 1
        for i in range(2,n):
            c = a + b
            fibonacci_list.append(c)
            a = b
            b = c
        return fibonacci_list


print("EXERCICE 1")
print("The first 10 numbers in the Fibonacci string are: " + str(firsts_n_fibonacci(10)))


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prime_numbers_from_list(numbers):
    prime_numbers = []
    for i in range(len(numbers)):
        x = numbers[i]
        is_prime = True
        if x != 1:
            for d in range(2, x // 2):
                if x % d == 0:
                    is_prime = False
                    break
            if is_prime == True:
                prime_numbers.append(x)
    return prime_numbers


print("EXERCICE 2")
print("From the list [1, 2, 12, 17, 21, 35, 31] the prime numbers are: "
      + str(prime_numbers_from_list([1, 2, 12, 17, 21, 35, 31])))


# 3. Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

def sets_operation(a, b):
    union = a + b
    intersection = [element for element in a if element in b]
    a_minus_b = [element for element in a if element not in b]
    b_minus_a = [element for element in b if element not in a]

    result = [["union : ", union],
              ["intersection : ", intersection],
              ["a-b :", a_minus_b],
              ["b-a : ", b_minus_a]]
    return result

print("EXERCICE 3")
print("a = [3, 6, 7, 8, 10, 11, 12], b = [3, 6, 7, 8, 16, 17], here are some operations with them: ")
result = sets_operation([3, 6, 7, 8, 10, 11, 12], [3, 6, 7, 8, 16, 17])
for i in range(0, len(result)):
    for j in range(0, len(result[0])):
        print(result[i][j])


# 4.Write a function that receives as a parameters a list of musical notes (strings),
# a list of moves (integers) and a start position (integer).
# The function will return the song composed by going though the musical notes
# beginning with the start position and following the moves given as parameter.

def compose(notes, moves, start):
    song = [notes[start]]
    position = start
    for i in range(0, len(moves)):
        position += moves[i]
        song.append(notes[position % len(notes)])
    return song

print("EXERCICE 4")
print('For notes = ["do", "re", "mi", "fa", "sol"], moves=[1, -3, 4, 2] and start=2 the song is:')
print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# 5.  Write a function that receives as parameter a matrix and
# will return the matrix obtained by replacing all
# the elements under the main diagonal with 0 (zero).

def replace_main_diagonal(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = 0
    return matrix

print("EXERCICE 5")
matrix = [ [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
print("The input matrix: ")
for i in range(0, len(matrix)):
        print(matrix[i])

print("The transformed matrix: ")
result = replace_main_diagonal(matrix)
for i in range(0, len(result)):
        print(result[i])


# 6.Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.


print("EXERCICE 6 TO DO")


# 7.Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def compute_reflected(number):
    reflected = 0

    while number != 0:
        reflected = reflected * 10 + number % 10
        number = number // 10
    return reflected


def is_palindrom(number):
    if number == compute_reflected(number):
        return True
    else:
        return False


def compute_tuple(numbers):
    count_palindromes = 0
    for i in range(0, len(numbers)):
        if is_palindrom(numbers[i]):
            count_palindromes += 1
            if count_palindromes == 1:
                max_palindrome = numbers[i]
            elif max_palindrome < numbers[i]:
                max_palindrome = numbers[i]
    tuple = (count_palindromes, max_palindrome)
    return tuple


print("EXERCICE 7")
print("For the list [13, 12, 22, 44, 121, 55, 123 ], "
      "the tuple(number_of_palindroms, greatest_palindrome) is: ")
print(compute_tuple([13, 12, 22, 44, 121, 55, 123]))