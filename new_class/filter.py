lst=[2,3,4,5,6]


evens=list(filter(lambda num:num%2==0,lst))
print(evens)


# odd number

oddnumbers=list(filter(lambda num:num%2!=0,lst))
print(oddnumbers)