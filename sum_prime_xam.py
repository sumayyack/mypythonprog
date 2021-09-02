#def prime(i):
     #sum=sum+i
n=int(input("enter a number"))
count=0
sum=0
for i in range(2,n):
    if n%i == 0:
        count=count+1
        sum=sum+i
print(sum)
print(count)

