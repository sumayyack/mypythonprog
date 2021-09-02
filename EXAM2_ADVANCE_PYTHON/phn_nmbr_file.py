import re
f1=open("phn_Numbr",'r')
f2=open("phn_numm",'w')
x='[+][9][1]\d{10}$'
for num in f1:
   # print(num)
    number=num.rstrip("\n")
    #print(number)
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(num)