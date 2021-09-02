


import re
n=input("enter a string to validate")
x='[a-zA-Z]+\d$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")