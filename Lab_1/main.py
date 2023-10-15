# 1. Find The greatest common divisor of multiple numbers read from the console.
def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x
def greatest_common_divisor():
    print("Enter some numbers to find their greatest common divisor: ")
    numbers = [int(i) for i in input().split()]
    count_numbers = len(numbers)

    num1 = numbers[0]
    num2 = numbers[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, count_numbers):
        gcd = find_gcd(gcd, numbers[i])

    print(gcd)


print("EXERCICE 1")
greatest_common_divisor()


# 2. Write a script that calculates how many vowels are in a string.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(string.count(vowel) for vowel in vowels)
    print(string + " has: " + str(count) + " vowels")


print("EXERCICE 2")
print("Enter a string: ")
user_string_1 = str(input())
count_vowels(user_string_1)


# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurrences(substring, string):
    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start) # search if str1 appears in str2 from position start

        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break;

    print(substring + " appears in " + string + " for " + str(count) + " times")


print("EXERCICE 3")
print("Enter the substring: ")
user_substring_1 = str(input())
print("Enter the string: ")
user_string_2 = str(input())
count_occurrences(user_substring_1, user_string_2)


# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def upperCamelCase_into_lowercase_with_underscores(string):
    result0 = [string[0].lower()]
    for c in string[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result0.append('_')
            result0.append(c.lower())
        else:
            result0.append(c)

    result = ''.join(result0)
    print("Your UpperCamelCase string: " + string + " transformed in into_lowercase_with_underscores is: " + str(result))


print("EXERCICE 4")
upperCamelCase = "AleScrieCodPython"
upperCamelCase_into_lowercase_with_underscores(upperCamelCase)


# 5. Given a square matrix of characters write a script that prints the
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

        if 0 <= cr and cr < rows and 0 <= cc and cc < columns and not (seen[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]

    print('For the input matrix: ')
    print(matrix)
    print('We obtain the string: /' + string + '/')


print("EXERCICE 5")
input_matrix = [['f', 'i', 'r', 's'],
          ['n', '_', 'l', 't'],
          ['o', 'b', 'a', '_'],
          ['h', 't', 'y', 'p']]
spiral_order(input_matrix)


# 6. Write a function that validates if a number is a palindrome.

def compute_reflected(number):
    reflected = 0

    while number != 0:
        reflected = reflected * 10 + number % 10
        number = number // 10
    return reflected


def is_palindrome(number):
    if number == compute_reflected(number):
        return True
    else:
        return False


print('EXERCICE 6')
print('356 is palindrome: ' + str(is_palindrome(356)))
print('424 is palindrome: ' + str(is_palindrome(424)))
print('555 is palindrome: ' + str(is_palindrome(555)))


# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.
def extract_first_number(string):
    extracted_number = 0
    first_digit_found = False
    for c in string:
        if c.isdigit():
            extracted_number = extracted_number * 10 + (ord(c) - ord('0'))
            first_digit_found = True
        elif first_digit_found:
            break

    if first_digit_found:
        return extracted_number
    else:
        return None


print('EXERCICE 7')
print('The first number in the string: /An apple is 123 USD/ is: ' + str(extract_first_number('An apple is 123 USD')))
print('The first number in the string: /abc123abc/ is: ' + str(extract_first_number('abc123abc')))
print('The first number in the string: /!ww1iu11@/ is: ' + str(extract_first_number('!ww1iu11@')))


# 8. Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def count_true_bits(number):
    if number >= 1:
        if number % 2 == 1:
            return 1 + count_true_bits(number // 2)
        else:
            return 0 + count_true_bits(number // 2)
    else:
        return 0

print('EXERCICE 8')
# 24 -> 00011000
print('The binary format for 24 has: ' + str(count_true_bits(24)) + ' bits with value 1')
# 8 -> 1000
print('The binary format for 8 has: ' + str(count_true_bits(8)) + ' bits with value 1')
# 100 -> 1100100
print('The binary format for 100 has: ' + str(count_true_bits(100)) + ' bits with value 1')


# 9. Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.

def compute_the_most_common_letter(string):
    string = string.lower()
    characters = {}  # the set of the chars from the input <=> using a dictionary

    for char in string:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    the_most_common_char = max(characters, key=characters.get)
    print("The most common letter in the input: /" + string + "/ is: " + str(the_most_common_char))


print('EXERCICE 9')
compute_the_most_common_letter('an apple is not a tomato')
compute_the_most_common_letter('Ciresica are mere')


# 10. Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.

def count_words(string):
    words = len(string.split())
    print('The input: /' + string + '/ has: ' + str(words) + ' words')


print('EXERCICE 10')
count_words('I have Python exam')
























