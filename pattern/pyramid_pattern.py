#      *
#     * *
#    * * *
#   * * * *


a=int(input("enter number of rows"))
for i in range(a):
    for s in range(a):
        print(end=" ")
    a=a-1
    for j in range(0,i+1):
        print("*",end=" ")
    print()
