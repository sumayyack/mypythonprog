import re
n='9656831866'
x='[0-9]{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")