# factorial finding using function with arguments
#def factorial(fact):
    #  s=1
 #   if fact>0:
#        for i in range(1,fact+1):
#            s=s*i
#        print("factorial",s)
  #  elif fact==0:
 #       print("factorial of 0 is 1")
#    else:
#        print("factorial doesnt exist for -ve numbers")

#factorial(9)
#factorial(6)
#factorial(-1)

def factorial(fact):
    s=1
    if fact>0:
        for i in range(1,fact+1):
            s=s*i
        return s
    elif fact==0:
        return"factorial of 0 is 1"
    else:
        return"factorial does not exist for -ve numbers"
print(factorial(-7))
print(factorial(3))





