# Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
# Testcase1 : Helloworld  
# Output : eo  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  

# Testcase1 : Jacksparrow  
# Output : ao  
# Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once, so consider it for one time , result is  ao.

#method-1(by using set vowels will be unordered)
# string=input("Enter the string : ")
# check="AEIOUaeiou"
# vow=""
# for i in string:
#     if i in check:
#         vow+=i
# rem_vow=set(vow)
# rem_vow=list(rem_vow)
# for i in rem_vow:
#     print(i,end="")

#method-2(without using set we will get ordered vowels)
string=input("Enter the string : ")         
check="AEIOUaeiou"
vow=""
for i in string:
    if i in check:
        if i in vow:
            continue
        else:
            vow+=i
print(vow)
