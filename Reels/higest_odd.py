# HIGHEST ODD NUMBER

# Write a Python program that takes a string of digits as input and removes trailing even digits until an odd digit is encountered. The program should then print the modified string.

# Method - 1 
string = input("Enter the string : ")
str1=""
for i in string[::-1]:
    i=int(i)
    if i % 2 !=0:
        break
    else:
        if i % 2 == 0:
            string = string[0:-1]
print(string)

# Method - 2
num = int(input("Enter the number: "))
big = 0
while(num>0):
    last = num%10
    if last%2==0:
        num=num//10
    else:
        big = num
        break
print(big)

