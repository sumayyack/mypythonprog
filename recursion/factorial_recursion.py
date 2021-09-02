# recursion  function call function itself
# call a function inside the function

def factorial(x):
    """ This is a recursive function
    to find the factorial of an integer"""

    if x == 0:
        return 1
   # elif x==0:
     #   return 1
    else:
        return x*factorial(x-1)

num = int(input("enter the number"))
print("the factorial is ",factorial(num))