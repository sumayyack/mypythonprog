# prime numbers
#2,3,5,7,11,13,17,19

num=int(input("enter a number"))
fla =0
if num>1:
 for i in range(2,num):
     if num%i ==0:
         break
 else:
      fla = 1
if fla==1:
     print("prime")
else:
     print("not prime")


