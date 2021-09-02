a=input("enter a string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print("first recursive character in ",a,"is",i)
        break     #first only print aakaan again print aakkan break ozhivakkukka