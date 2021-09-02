# function with arguments and return type
def add(x,y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("select operation")
print("1.Add")
print("2.subtraction")
print("3.multiply")
print("4.division")
while True:
    choice =int(input("enter the choice"))
    num1 = float(input("enter a number"))
    num2 = float(input("enter a number"))
    if choice ==1:
        print(add(num1, num2))
    elif choice == 2:
        print(substract(num1, num2))
    elif choice == 3:
        print(multiply(num1, num2))
    elif choice == 4:
        print(divide(num1 ,num2))
    else:
        print("invalid choice")











