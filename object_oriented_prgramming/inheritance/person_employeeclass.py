class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
   # def printvalue(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    company="abd"
    def set(self,id,salary,department):
        self.id=id
        self.salary=salary
        self.department=department
   # def printval(self):
        print(self.id)
        print(self.salary)
        print(self.department)
        print(Employee.company)
#pe=Person()
#pe.setvalue("sumayya",24)
#pe.printvalue()
em=Employee()
em.setvalue("sumayya",24)

em.set(229,25000,"software")


