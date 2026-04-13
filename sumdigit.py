
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
