lst=[2,4,6]
#total=sum(lst)
#op=[total-num for num in lst]
#print(op)


print(list(map(lambda num:sum(lst)-num,lst)))