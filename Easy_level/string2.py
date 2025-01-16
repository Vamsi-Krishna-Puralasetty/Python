# Check if a String is a Palindrome
# Question: Write a function to check if a given string is a palindrome.
# Testcase: "racecar"
# Output: true
# Explanation: A palindrome is a string that reads the same forward and backward. Since "racecar" is the same in both directions, the output is true.

str=input("Enter the string: ")
pali=""
for i in range(len(str)-1,-1,-1):
    pali+=str[i]
if str==pali:
    print("true")
else:
    print("false")