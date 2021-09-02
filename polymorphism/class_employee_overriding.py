class Person:
    def printv(self,name,age):
        self.name=name
        self.age=age
        print(self.name+self.age)
class Employee(Person):
    def printv(self,id,salary):
        self.id=id
        self.salary=salary
        print(self.id)
        print(self.salary)
em=Employee()
em.printv(229,25000)
