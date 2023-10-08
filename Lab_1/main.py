# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# Lab exercices

# 1. Find The greatest common divisor of multiple numbers read from the console.
def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x
def greatest_common_divisor():
    print("Enter some numbers to find their greatest common divisor: ")
    numbers = [int(i) for i in input().split()]
    count_numbers = len(numbers)

    num1 = numbers[0]
    num2 = numbers[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, count_numbers):
        gcd = find_gcd(gcd, numbers[i])

    print(gcd)


greatest_common_divisor()


