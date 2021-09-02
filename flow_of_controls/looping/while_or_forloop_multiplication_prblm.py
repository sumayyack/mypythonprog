#num=int(input("enter a number"))
#fact=1
#for i in range(1,num+1):
 #   fact=fact*i
#print(fact)           #factorial of 6= 6*5*4*3*2*1




num=int(input("enter a number"))
if num>0:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
elif num==0:
    print("factorial of 0 is 1")
else:
    print("factorial doesnt exist for -ve numbers")
