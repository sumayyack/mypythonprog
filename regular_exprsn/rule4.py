import re

x = "[a-zA-Z]"
matcher=re.finditer(x,"abt9 c@5kAz")
for match in matcher:
    print(match.start())
    print(match.group())