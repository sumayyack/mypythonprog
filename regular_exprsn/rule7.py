import re

x = "\w"
matcher= re.finditer(x,"abtA c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())