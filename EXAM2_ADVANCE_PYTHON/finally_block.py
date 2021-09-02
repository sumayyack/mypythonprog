num1=int(input("enter a number"))
num2=int(input("enter a number"))

try:
    res=num1/num2
    print("result is",res)
except:
    print("exception occured")
finally:
    print("division done")
