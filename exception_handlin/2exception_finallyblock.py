a=[1,2,3]
index=int(input("enter the index"))
try:
    print(a[index])
except:
    print("index not in list")
finally:
    print("indexing done")
