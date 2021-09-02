a = input("enter a string")
count = 0
for i in a:
    if i in "aeiou":
        count+=1
    else:
        pass
print("the count of vowel in ",a,'is=',count)