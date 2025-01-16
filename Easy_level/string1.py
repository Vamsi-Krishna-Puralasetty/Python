# Reverse a String : 
# Question: Write a function to reverse a given string.
# Testcase: "hello"
# Output: "olleh"
# Explanation: The reverse of the string "hello" is "olleh". Each character's order is reversed.

#method-1
str=input("Enter the string: ")
print(str[::-1])

#method-2
str=input("Enter the string: ")
res=""
for i in range(len(str)-1,-1,-1):
    res=res+str[i]
print(res)
    