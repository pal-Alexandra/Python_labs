# Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurrences(substring, string):
    count = 0
    start = 0

    while start < len(string):
        pos = string.find(substring, start) # search if str1 appears in str2 from position start

        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break;

    print(substring + " appears in " + string + " for " + str(count) + " times")


print("Enter the substring: ")
substring = str(input())
print("Enter the string: ")
string = str(input())
count_occurrences(substring, string)