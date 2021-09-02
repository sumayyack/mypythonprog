a=int(input("enter your age"))
if a<18:
    raise Exception("age is below 18")
else:
    print("you are eligible")