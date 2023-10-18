# 8. Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start". Starting with the value
# of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value,
# until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.

def ex_8(mapping):
    result = [mapping['start']]
    new_key = mapping['start']
    visited_keys = ['start']

    while new_key not in visited_keys:
        if mapping[new_key] not in result:
            result.append(mapping[new_key])
        visited_keys.append(new_key)
        new_key = mapping[new_key]

    return result

print("EXERCICE 8")
print("Input: {'start': 'a', 'b': 'a', 'a': '6',"
      " '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}")
print("Output: " + str(ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})))
