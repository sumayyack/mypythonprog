stk=[]
size=int(input("enter the size"))
top=0
n=0
def push():         # push=insertion of element
    global top, size
    if(top>size):
        print("size is full")
    else:
        p=int(input("enter the element want to push"))
        stk.append(p)
        top+=1
def pop():      #pop= removal of elemnt
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
def display():
    print (stk)
while(n!=1):
    print("enter the operation want to perform")
    opt=int(input("press1)push press2)pop press3)display"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    n=int(input("do you want to continue press 1 for exist"))

