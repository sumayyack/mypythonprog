import re
count = 0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("match available at",match.start())   # return position
    print("group=",match.group())     #which object find match
    count+=1
print("count=",count)