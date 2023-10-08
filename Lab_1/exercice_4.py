# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def upperCamelCase_into_lowercase_with_underscores(string):
    result0 = [string[0].lower()]
    for c in string[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            result0.append('_')
            result0.append(c.lower())
        else:
            result0.append(c)

    result = ''.join(result0)
    print("Your UpperCamelCase string: " + string + " transformed in into_lowercase_with_underscores is: " + str(result))


upperCamelCase = "AleScrieCodPython"
upperCamelCase_into_lowercase_with_underscores(upperCamelCase)
