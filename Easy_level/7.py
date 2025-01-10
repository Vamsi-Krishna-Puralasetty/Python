# Write a program to print the vowels in the given string in reverse order.  
# Testcase1 : Helloworld  
# Output : ooe  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
# Testcase1 : JackspArrow  
# Output : oAa  
# Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa.  

#method-1
string=input("Enter the String :")
check="aeiouAEIOU"
vow=""
for i in string:
    if i in check:
        vow=vow+i
# print(vow[::-1])
for j in reversed(vow):
    print(j,end="")