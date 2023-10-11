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
        for i in range(2, n):
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
matrix = [[1, 1, 1, 1],
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

# 6.Write a function that receives as a parameter a variable
# number of lists and a whole number x.
# Return a list containing the items that appear exactly
# x times in the incoming lists.

def exactly_x_time_list(x, *lists):
    result = []
    input_lists = []

    # fixez lista formata din input ul variabil de liste
    for list in lists:
        input_lists += list

    for list in input_lists:
        if list not in result:
            if input_lists.count(list) == x:
                result.append(list)
    return result


print("EXERCICE 6")
print("For the input: [1,2,3], [2,3,4],[4,5,6], [4,1, 'test'] and x = 2  the result is: ")
print(exactly_x_time_list(2, [1, 2, 3], [2, 3, 4],[4, 5, 6], [4, 1, 'test']))

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


# 8.Write a function that receives a number x,
# default value equal to 1, a list of strings,
# and a boolean flag set to True. For each string,
# generate a list containing the characters that have
# the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters
# that have the ASCII code not divisible by x.

def generate_lists(lists, flag=True, x=1):
    resulted_lists = []
    for string in lists:
        specific_list = []
        for char in string:
            # print(char)
            if flag:
                # print("here4")
                # print(ord(char) % x)
                if ord(char) % x == 0:
                    specific_list.append(char)

            else:
                # print("here3")
                # print(ord(char) % x)
                if ord(char) % x != 0:
                    specific_list.append(char)
        resulted_lists.append(specific_list)

    return resulted_lists


print("EXERCICE 8")
print('For x=2, lists=["test", "hello", "lab002"] , flag=False and x = 1')
print('The resulted lists are: ')
lists, flag = ["test", "hello", "lab002"], False
result = generate_lists(lists, flag, 2)
for string in result:
    print(string)


# 9.Write a function that receives as paramer a matrix
# which represents the heights of the spectators in a stadium
# and will return a list of tuples (line, column) each one representing
# a seat of a spectator which can't see the game. A spectator can't see the game
# if there is at least one taller spectator standing in front of him.
# All the seats are occupied. All the seats are at the same level.
# Row and column indexing starts from 0,
# beginning with the closest row from the field.

# a spectator can't see the game: people standing in front of each other by columns and row 0 is the closest from the field
# spectator(r, c)
# if  exists s'(r', c') with c=c', r' < r => s(r,c) cannot see the game
def not_seeing_game(stadium):
    people_not_seeing = []
    rows = len(stadium)
    cols = len(stadium[0])

    for col in range(0, cols):
        for row in range(1, rows):

            human_taller_in_front = 0
            for in_front in range(row - 1, 0, -1):
                if stadium[row][col] <= stadium[in_front][col]:
                    human_taller_in_front = 1
                    break

            if human_taller_in_front == 1:
                people_not_seeing.append([row, col])

    return people_not_seeing


print("EXERCICE 9")
print("For the following stadium: ")
stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
for i in range(0, len(stadium)):
    print(stadium[i])

print('The not seeing people are: ')
people_cannot_see = not_seeing_game(stadium)
for i in range(0, len(people_cannot_see)):
    print(people_cannot_see[i])


# 10. Write a function that receives a variable number of lists and
# returns a list of tuples as follows: the first tuple contains
# the first items in the lists,
# the second element contains the items on the position 2
# in the lists, etc.

def tuples_elements_from_position(*lists):
    maxLength = max(len(list) for list in lists)
    tuples_list = []
    for i in range(0, maxLength):  # tuple building: a tuple will have the length = max length of the input lists
        tuple = []
        for list in lists:
            if i >= len(list):
                tuple.append(None)
            else:
                tuple.append(list[i])

        tuples_list.append(tuple)
    return tuples_list


print("EXERCICE 10")
print('For this input  [1,2,3], [5,6,7], ["a", "b"]  the resulted tuples are: ')
tuples_ex_10 = tuples_elements_from_position([1, 2, 3], [5, 6, 7], ["a", "b"])
print(tuples_ex_10)


# 11.Write a function that will order a list of string tuples
# based on the 3rd character of the 2nd element in the tuple.
def order_list(tuples_list):
    count_tuples = len(tuples_list)

    # bubble sort
    for tuple in range(count_tuples): #parcurg tuplele
        for j in range(0, count_tuples - tuple - 1):
            char1 = tuples_list[tuple][1][2] #caracterul al 3-lea din al doile string din tuplul curent
            char2 = tuples_list[j + 1][1][2]
            if ord(char1) > ord(char2):
                aux = tuples_list[tuple]
                tuples_list[tuple] = tuples_list[tuple + 1]
                tuples_list[tuple + 1] = aux

    return tuples_list

print("EXERCICE 11")
print("The tuples: [('abc', 'bcd'), ('abc', 'zza')] "
      "sorted based on the 3rd character of the 2nd element in the tuple: ")
sorted_tuples = order_list([['abc', 'bcd'], ['abc', 'zza']])
print(sorted_tuples)


# 12.Write a function that will receive a list of words
# as parameter and will return a list of lists of words,
# grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.

def group_by_rhyme(words):
    # dictionar {grup_ultimele_2_litere -> cuvinte care se termina cu el}
    rhymed_words ={}
    for word in words:
        last_letters = word[-2:]
        if last_letters not in rhymed_words:
            rhymed_words[last_letters] = [word]
        else:
            rhymed_words[last_letters].append(word)

    grouped_words_by_rhyme = list(rhymed_words.values())
    return grouped_words_by_rhyme

print("EXERCICE 12")
print("The words: ['ana', 'banana', 'carte', 'arme', 'parte'] grouped by rhyme are: ")
print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))









