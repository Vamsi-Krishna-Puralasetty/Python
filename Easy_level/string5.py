# Convert String to Title Case
# Question: Write a function that converts a string to title case (capitalize the first letter of each word).
# Testcase: "hello world"
# Output: "Hello World"
# Explanation: The first letter of each word is capitalized, resulting in "Hello World".

#method-1
str=input("Enter the string : ")
print(str.title())

#method-2
str=input("Enter the string : ")
lst=str.split()
ans=""
for i in lst:
    res=i[0].upper()
    
    for j in range(1,len(i)):
        res+=i[j]
    ans+=res+" "
print(ans)


