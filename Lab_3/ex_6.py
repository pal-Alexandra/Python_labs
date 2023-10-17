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