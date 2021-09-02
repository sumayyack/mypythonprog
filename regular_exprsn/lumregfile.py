#import re
#f1=open("lumregno",'r')
#x='[L][U][M][0-9]{2}[P][Y][0-9]{3}$'
#for lum in f1:
  #  regno=lum.rstrip("\n")
    #print(regno)
   # matcher=re.fullmatch(x,regno)
  #  if matcher!=None:
     #   print(lum)



import re
f2=open("validreg",'w')
rule='([L][U][M]\d{2}[P][Y]\d{3}$)'
f=open("lumregno",'r')
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")