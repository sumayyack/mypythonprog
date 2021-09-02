def values(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(values(1,2,3,4))