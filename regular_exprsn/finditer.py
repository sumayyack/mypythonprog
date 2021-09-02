# patter printing

#re__regular expression........package for pattern printing

import re

count =0
matcher = re.finditer ('ab' ,'abaabbab')
#print(matcher)
for match in matcher:
    count+=1
print ("count=",count)
