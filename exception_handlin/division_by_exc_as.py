num1=int(input("enter number1"))
num2=int(input("enter number2"))
#res=num1/num2
try:
    res=num1/num2
    print(res)
except Exception as e:
    print(e.args)