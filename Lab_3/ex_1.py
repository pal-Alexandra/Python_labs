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



