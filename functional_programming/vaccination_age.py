def vaccine_eligibilty(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("age is less")
        else:
            return func(a,b,c)

    return wrapper



@vaccine_eligibilty
def vaccine(name,age,place):
    return "eligible"
print(vaccine("anu",16,"kochi"))
