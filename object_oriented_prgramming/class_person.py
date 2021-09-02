class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print("age",self.age)
pe=Person()
pe.setvalue("anu",26)
pe.printvalue()

pe1=Person()
pe1.setvalue("sumayya",24)
pe1.printvalue()