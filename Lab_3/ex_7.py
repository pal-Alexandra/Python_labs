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