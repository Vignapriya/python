a=float(input("Enter Your Language Mark:"))
b=float(input("Enter Your Maths Mark:"))
c=float(input("Enter Your Physics Mark:"))
d=float(input("Enter Your Chemistry Mark:"))
e=float(input("Enter Your Biology Mark:"))
x=(a+b+c+d+e)/5
print"The Average of the Marks:",x
if(x>=90):
   print"You Have Secured O Grade."
elif(x<=89 and x>= 80):
   print"You Have secured A+ Grade."
elif(x<= 79 and x>= 70):
   print"You Have Secured A Grade."
elif(x<=69 and x>=60):
   print"You Have Secured B+ Grade."
elif(x<=59 and x>= 55):
   print"You Have Secured B Grade."
elif(x>=54 and x<=50):
   print"You Have Secured C Grade."
else:
   print"You Have Failed."
