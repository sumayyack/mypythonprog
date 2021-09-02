class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,id,salary,dprtmnt,name,age):
        super(). __init__(name,age)
        self.id=id
        self.salary=salary
        self.dprtmnt=dprtmnt
    def printf(self):
        print(self.id)
        print(self.salary)
        print(self.dprtmnt)


em=Employee(229,25000,"software","sumayya",24)
em.print()
em.printf()