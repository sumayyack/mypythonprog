#fibnocci series
# 0,1,1,2,3,5,8,13,....
n1=0
n2=1
for i in range(10):
    print(n1)  # 0,1,1
    nth = n1 + n2 #1,2
    n1 = n2  # 1,1,
    n2 = nth  # 1,2
