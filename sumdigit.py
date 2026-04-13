x=raw_input("Enter The String1:")
y=raw_input("Enter the String2:")
if(x==y):
   print("Strings are equal.")
else:
   print("Strings are not equal.")
[23bee028@mepcolinux ~]$python 2c.py
Enter The String1:test
Enter the String2:case
Strings are not equal.
[23bee028@mepcolinux ~]$cat 2d.py
a=int(input("Enter the 4-Digit Number"))
sum=0
if(a>=1000 and a<=9999):
   while a>0:
        x=a%10
        sum+=x
        a=a//10
   print"Sum of the Digits=",sum
else:
    print"Enter Valid Number."
