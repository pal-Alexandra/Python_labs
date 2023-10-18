# 9.  Write a function that receives a variable number of
# positional arguments and a variable number of keyword arguments
# and will return the number of positional arguments whose values
# can be found among keyword arguments values.

def ex_9(*pargs, **kargs):
    count = 0
    for positional_argument in pargs:
        if positional_argument in kargs.values():
            count += 1
    return count


print("EXERCICE 9")
print("Input: 1, 2, 3, 4, x=1, y=2, z=3, w=5")
print("Output: " + str(ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5)))