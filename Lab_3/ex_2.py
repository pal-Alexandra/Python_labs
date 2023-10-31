# 2.  Write a function that receives a string as a parameter and returns a dictionary in which
# the keys are the characters in the character string and the values are the number of occurrences
# of that character in the given text.

def ex_2(string):
    occurences = {}
    for char in string:
        if char != ' ':
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] += 1
    return occurences

print("EXERCICE 2")
print("The dictionary {char : occurences } for: /Ana has apples/ is:")
print(ex_2("Ana has apples"))