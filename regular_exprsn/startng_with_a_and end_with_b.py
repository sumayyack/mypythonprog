# star

import re
n=input("enter a string")
x='^a[a-zA-Z0-9\W]*[b]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

