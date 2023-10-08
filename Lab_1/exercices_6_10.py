# 6. Write a function that validates if a number is a palindrome.

def compute_reflected(number):
    reflected = 0

    while(number != 0):
        reflected = reflected * 10 + number % 10
        number = number // 10
    return reflected

def is_palindrom(number):
    if number == compute_reflected(number):
        return True
    else:
        return False


print('EXERCICE 6')
print('356 is palindrome: ' + str(is_palindrom(356)))
print('424 is palindrome: ' + str(is_palindrom(424)))
print('555 is palindrome: ' + str(is_palindrom(555)))


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

