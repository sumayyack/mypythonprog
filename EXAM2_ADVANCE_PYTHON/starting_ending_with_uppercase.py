import re
n=input("enter")
x=('^[A-Z]+\w{5,10}[A-Z]$')
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")