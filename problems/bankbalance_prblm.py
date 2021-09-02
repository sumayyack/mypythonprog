#fixed_amount=10000
#withdraw=int(input("enter the amount to withdraw"))
#if withdraw<fixed_amount:
#    balance=fixed_amount-withdraw
#    print("your balance",balance)
#else:
#    print("insufficient")



#num1=int(input("enter a number1"))
#num2=int(input("enter a number2"))
#if num1>num2:
#    print("num1 greater")
#elif num1==num2:
 #   print("num1 and num2 are equal")
#else:
#    print("num2 is greater")



#num1=6
#num2=2
#num3=2
#if num1>num2 or num2==num3:
#    print("hello")



no1=int(input("enter num1"))
no2=int(input("enter num2"))
no3=int(input("enter num3"))
if (no1>no2)&(no1>no3):
    print("no1 is max ")
elif (no2>no1)&(no2>no3):
    print("no2 is max")
elif no1==no2==no3:
    print("equal")
else:
    print("no3 is max")