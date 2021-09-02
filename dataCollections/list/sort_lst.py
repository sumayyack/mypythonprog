my_lst=[111,-15,-26,15,1,0,8,876,100,-64,23,76]
#my_lst.sort()
#print(my_lst)


new_lst=[]
while my_lst:
    min=my_lst[0]
    for i in my_lst:
        if i<min:
            min=i
    new_lst.append(min)
    my_lst.remove(min)


print(new_lst)
print(my_lst)
