que=[]
size=int(input("enter the size::"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>size:
        print("queue is full")
    else:
        p=int(input("enter the element want to insert"))
        que.insert(rear,p)
        rear+=1

        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue is empty")
    else:
        front+=1

        for i in range(front,rear):
            print(que[i])

while n!=1:
    print(".............enter operation want to perform.......")
    opt=int(input("press\n1)enqueue\n2)dequeue\n"))
    if opt==1:
        insert()
    elif opt==2:
        delete()