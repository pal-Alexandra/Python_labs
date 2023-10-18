# TO DO
# 3. Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers,
# such as dictionaries, lists, sets, etc.)

def ex_3(dict_1, dict_2):
    if len(dict_1.keys()) != len(dict_2.keys()):
        return False

    for dict_1_key in dict_1.keys():

        if dict_1_key not in dict_2.keys():
            return False

        if type(dict_1[dict_1_key]) != type(dict_2[dict_1_key]):
            return False

        if isinstance(dict_1[dict_1_key], dict):
            if not ex_3(dict_1[dict_1_key], dict_2[dict_1_key]):
                return False
            continue

        if dict_1[dict_1_key] != dict_2[dict_1_key]:
            return False

    return True

print("EXERCICE 3")
dict_1 = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'k4': {
        'x': 1,
    },
    'list_k': [1, 2]
}

dict_2 = {
    'k1': 1,
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
    'list_k': [1, 2]
}
print(ex_3(dict_3, dict_4))