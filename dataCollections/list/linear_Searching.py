lst=[1,2,3,4,5,6,88,99,45,89,67]

def linsearch(lst):
    ele=int(input("enter element to search"))
    fla=0
    for i in lst:
        if i==ele:
            fla=1
            break
    if fla==0:
        print("not found")
    else:
        print("found")
linsearch(lst)

