a=int(input("enter your age"))
if a<18:
    raise Exception("vaccination under age 18 is not eligilble")
else:
    print("you are eligible")