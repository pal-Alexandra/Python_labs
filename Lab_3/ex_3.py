# # 3. Compare two dictionaries without using the operator "==" returning True or False.
# # (Attention, dictionaries must be recursively covered because they can contain other containers,
# # such as dictionaries, lists, sets, etc.)
def ex_3(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if len(dict_1.keys()) != len(dict_2.keys()):
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1.keys():
        if key not in dict2.keys():
            return False

        if type(dict1[key]) != type(dict2[key]):
            return False

        if isinstance(dict1[key], dict):
            if not ex_3(dict1[key], dict2[key]):
                return False
            continue
        elif isinstance(dict1[key], (list, set)):
            if len(dict1[key]) != len(dict2[key]):
                return False
            for elm1, elm2 in zip(dict1[key], dict2[key]):  # zip ne da o tupla de iteratori peste parametrii
                if isinstance(elm1, (list, set)):
                    if not ex_3(elm1, elm2):
                        return False
                elif elm1 != elm2:
                    return False
        elif dict1[key] != dict2[key]:
            return False

    return True


print("EXERCICE 3")
dict_1 = {
    'k1': 1,
    ('q', 'w'): ('a', 'b'),
    2: 'a',
    'k2': 2,
    'k3': 3,
    'k4': {
        'x': 1,
    },
    'list_k': [1, 2]
}

dict_2 = {
    'k1': 1,
    2: 'a',
    ('q', 'w'): ('a', 'b'),
    'k2': 2,
    'k3': 3,
    'k4': {
        'x': 1,
    },
    'list_k': [1, 2]
}
print(ex_3(dict_1, dict_2))

dict_3 = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'k4': {
        'x': 1,
    },
    'list_k': [1, 2, 3]
}

dict_4 = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'k4': {
        'x': 1,
    },
    'list_k': [1, 2, 2]
}
print(ex_3(dict_3, dict_4))

