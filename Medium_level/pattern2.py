# Write a program that takes number of rows as input and print below respective pattern.

# Testcase1	:  Enter number of rows: 4
# Output     	: 

# 4 3 2 1
# 4 3 2
# 4 3
# 4

num=int(input("Enter the number of rows:"))
for row in range(num,0,-1):
    for col in range(num,num-row,-1):
        print(col,end=" ")
    print()