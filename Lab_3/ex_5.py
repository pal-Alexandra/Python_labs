# TO DO
# 5. The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
# A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary matches all the rules, False otherwise.

# **: daca exista cheie in dict, dar nu exista cheie in rules => false
def ex_5(rules_set, dict):

    rules_keys = []
    for rule in rules_set:
        key, start, mid, end = rule[0], rule[1], rule[2], rule[3]

        rules_keys.append(key) #(tratare **)

        if key in dict:
            value = dict[key]
            if not value.startswith(start):
                return False
            if not value.endswith(end):
                return False

            if not value.startswith(mid) and not value.endswith(mid) and mid in value:
                continue
        else:
            print("OBS: Failed to find key: /" + key + "/ in the input dictionary")

        #continuare tratare **
        dict_keys = list(dict.keys())
        for dict_key in dict_keys:
            if dict_key not in rules_keys:
                return False
        return True

print("EXERCICE 5")
print('Input: rules={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and dict= {"key1": "come inside, it`s too cold out", "key3": "this is not valid"}')
print("Output: " + str(ex_5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key1": "come inside, it`s too cold out", "key3": "this is not valid"})))

