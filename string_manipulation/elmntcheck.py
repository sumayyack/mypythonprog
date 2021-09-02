#a="luminar"
#b=(input('enter a elemnt to check'))
#if b in a:
#     print("present")
#else:
#    print("not")


a="luminar"
b=(input("enter an elemnt to check"))
fla=0
for i in a:
    if i in b:
        fla=1
if fla==1:
    print("present")
else:
    print("not")
