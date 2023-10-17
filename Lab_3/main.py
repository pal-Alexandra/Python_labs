# 1. Write a function that receives as parameters two lists a and b
# and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)

def ex_1(a, b):
    result = []
    union = set(set(a) | set(b))
    intersection = set([value for value in a if value in b])
    a_minus_b = set([value for value in a if value not in b])
    b_minus_a = set([value for value in b if value not in a])
    result.append(union)
    result.append(intersection)
    result.append(a_minus_b)
    result.append(b_minus_a)
    return result

print("EXERCICE 1")
print("[union, intersection, a_minus_b, b_minus_a] of [1, 2, 5, 5, 9] and [1, 2, 5, 7, 13]")
print(ex_1([1, 2, 5, 5, 9], [1, 2, 5, 7, 13]))


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
                occurences[char] +=1
    return occurences

print("EXERCICE 2")
print("The dictionary {char : occurences } for: /Ana has apples/ is:")
print(ex_2("Ana has apples"))

# TO DO
# 3. Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers,
# such as dictionaries, lists, sets, etc.)


# TO DO
# 4. The build_xml_element function receives the following parameters: tag, content,
# and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
# returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"


# TO DO
# 5. The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.


# 6.  Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list,
# and b representing the number of duplicate elements in the list (use sets to achieve this objective).
def ex_6(list):
    set_from_list = set(list)
    count_unique_elements = len(set_from_list)
    count_duplicate_elements = len(list) - count_unique_elements
    return (count_unique_elements, count_duplicate_elements)

print("EXERCICE 6")
print("(count_unique_elements, count_duplicate_elements) for: [1, 2, 2, 5, 8, 4, 4, 8]")
print(ex_6([1, 2, 2, 5, 8, 4, 4, 8]))


# 7.Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form:
# "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
def ex_7(*sets):
    result = {}
    input_sets = []
    for set in sets:
        input_sets.append(set)

    for i in range(0, len(input_sets)-1):
        for j in range(i+1, len(input_sets)):
            a = input_sets[i]
            b = input_sets[j]
            operations = ex_1(a, b)
            a_string = str(a)
            b_string = str(b)
            union_string = a_string + " | " + b_string
            intersection_string = a_string + " & " + b_string
            a_minus_b_string = a_string + " - " + b_string
            b_minus_a_string = b_string + " - " + a_string
            result[union_string] = operations[0]
            result[intersection_string] = operations[1]
            result[a_minus_b_string] = operations[2]
            result[b_minus_a_string] = operations[3]
    return result

print("EXERCICE 7")
print(ex_7({1,2}, {2, 3}))


# 8.