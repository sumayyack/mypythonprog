# parallellogram pattern

#   * * * * *
#    * * * * *
#     * * * * *
#      * * * * *
#       * * * * *

def parallel(n):
    k=n
#   print(k)
    for i in range(n):
        for r in range(k):
            print(end=" ")
        k=k+1
        for j in range(0,n):
            print("*", end= " ")
        print()
parallel(5)