#num1=int(input("enter no1"))
#num2=int(input("enter no2"))
#res=num1/num2
#print(res)



num1=int(input("enter no1"))
num2=int(input("enter no2"))
try:              # error varan chanceulla code try blockl venam write cheyyan
    res=num1/num2
    print(res)
except:           # error vannal enthan print cheyyendath adh ivide wite cheyyuka
    print("exception occured")


    # try block always work
    # except block work only if there is an error
