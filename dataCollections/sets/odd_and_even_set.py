a={1,2,3,4,5,6,7,8,9,10,11,12,13,14,33,44}
o=set()
e=set()
for i in a:
    if i%2==0:
        o.add(i)
      #  print(e)
    else:
        e.add(i)
        #print(o)
print(o)
print(e)