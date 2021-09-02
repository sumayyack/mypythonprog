lst=[1,2,3,4,5,6,7,5,4,3]
b=[]
for i in lst:
    if i not in b:
        b.append(i)
    else:
        print(i)
