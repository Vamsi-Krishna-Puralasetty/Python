# Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
# Testcase1 : JohnWick  
# Output : jOHNwICK  
# Explanation : All the upper case letters changed to lower case and vise  versa.  
# Testcase1 : Korean  
# Output : kOREAN  
# Explanation : All the upper case letters changed to lower case and vise  versa.  

#method-1
str=input("Enter a value : ")
print(str.swapcase())

#method-2
str=input("Enter a value : ")
result=""
for i in str:
    if i>="a" and i<="z":
        result+=i.upper()
    elif i>="A" and i<="Z":
        result+=i.lower()
    else:
        print("It contains special characters")
        break
print(result)

