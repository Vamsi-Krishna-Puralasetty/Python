# Write a program to check whether the digits in-between the first and last  
# digit are less than first and last digit, if yes then print true, otherwise print  false.  
# Testcase1 : 1672  
# Output : false
# Explanation : The middle digits 6,7 are not less than first digit 1 and  last digit 7 .  
# Testcase1 : 84719  
# Output : true  
# Explanation : The middle digits 4,7,1 are less than first digit 8 and last  digit 9 .  

num=int(input("Enter the number:"))
temp=num
last=num%10
count=0
while temp>0:
    temp=temp%10
    count+=1
    temp//=10
first=num//10**(count-1)
digit=str(num)
mid=digit[1:((len(digit))-1)]
remain=int(mid)
answer=True
for i in mid:
    remlast=remain%10
    if remlast<=first and remlast<=last:
        answer=True
        # print(true)
    else:
        answer=False
    # remain//=10
        # print(false)
print(answer)