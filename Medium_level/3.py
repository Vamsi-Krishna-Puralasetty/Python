# Write a program that takes array of numbers as input, among the numbers in array, print the numbers which forms a prime number by adding one to it. Print such numbers in the given array separated b spaces.

# Testcase1	:  [ 7, 4, 7, 23, 10 ]
# Output     	:  4 10
# Explanation : In the given array of number [ 7, 4, 7, 23, 10 ] the numbers 4 and 10 by adding one to these numbers, they formed prime number 5 and 11. So the output is 4 10.

lst=[]
ans=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    num=int(input("Enter the number : "))
    lst.append(num)
for num in lst:
    check=num+1
    isprime=True
    for i in range(2,check//2):
        if check%i==0:
            isprime=False
    if isprime:
        ans.append(num)
for i in ans:
    print(i,end=' ')
        




