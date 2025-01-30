# Rotate an Array

# Problem: Write a function that rotates an array to the right by a given number of steps.
# Testcase 1:
# Input: [1, 2, 3, 4, 5], 2
# Output: [4, 5, 1, 2, 3]

#Method - 1
# num = int(input("enter the number of elements: "))
# lst = []
# for i in range(0,num):
#     ele = int(input("enter the element: "))
#     lst.append(ele)
# k = int(input("enter the k value: "))
# for i in range(0,k):
#     lst.insert(0,lst[-1])       # adding that element at the start of the list and removing the elemnt at the same time
#     # del lst[-1]
#     lst.pop(-1)
# print(lst)



arr=list(map(int,input("Enter the elements : ").split()))
check=int(input("Enter the value:"))
arr1=[]
arr1=arr[check+1:] + arr[0:check+1]
print(arr[check+1:])
print(arr[0:check+1])
print(arr1)
# for i in range(0,len(arr)):
#     if i<=check:
#         arr.remove(arr[i])
#         arr1.append(arr[i])
# for i in arr1:
#     arr.append(arr[i])
# print(arr)
    # arr[i]=arr[i+check]