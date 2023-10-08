# Write a script that calculates how many vowels are in a string.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(string.count(vowel) for vowel in vowels)
    print(string + " has: " + str(count) + " vowels")


print("Enter a string: ")
user_string = str(input())
count_vowels(user_string)