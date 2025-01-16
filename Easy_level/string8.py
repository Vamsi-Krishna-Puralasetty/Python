# Count Occurrences of a Character
# Question: Write a function that counts the occurrences of a specific character in a string.
# Testcase: "hello world", "l"
# Output: 3
# Explanation: The character 'l' appears 3 times in the string "hello world".

str=input("Enter the string : ")
check=input("Enter the value : ")
count=0
for i in str:
    if i==check:
        count+=1
print(count)