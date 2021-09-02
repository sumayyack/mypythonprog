#constructure
# used to initialize instance variables

class Person:
    def __init__(self,name,age,adress): #constucture
        self.name=name
        self.age=age
        self.adress=adress

    def printvalue(self):
        print(self.name,self.age,self.adress)
obj=Person("anu",26,"abc")   # ivde nammal values onnich kodukkum

obj.printvalue()