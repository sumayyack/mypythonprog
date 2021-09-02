#dict ={'d':4,'b':3,'s':7}
#if 'f' in dict:
#    print("exist")
#else:
 #   print("not")

d={1:10,2:20,3:30,4:40,5:50,6:60}

def is_key_present(x):
    if x in d:
        print(x,'is present in the dictionary')
    else:
        print(x,'is not present in the dictionary')

x=int(input("enter a key"))
is_key_present(x)