# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 1
# 1 2
# 1 2 3
# 1 2 3 4

#method - 1
num=int(input("Enter number of rows: "))
for row in range(1,num+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

#method - 2
print("1")
print("1 2")
print("1 2 3")
print("1 2 3 4")