import re
n=input("enter")
x=('^[a]\d+[b]$')
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")