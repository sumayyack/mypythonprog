class Parent:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print(self.name)
        print(self.age)
        print(self.place)

class Teacher(Parent):
    def __init__(self,id,dprtmnt,subjct,name,age,place):
        super().__init__(name,age,place)
        self.id=id
        self.dprtmnt=dprtmnt
        self.subjct=subjct
    def printv(self):
        print(self.id,self.dprtmnt,self.subjct)

    def __str__(self):
        return self.name+str(self.id)

tr=Teacher(229,"lp","maths","sumayya",24,"tanur")
tr.print()
tr.printv()
print(tr)