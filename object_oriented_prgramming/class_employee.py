class Employee:
   # companyname="luminar"
    def setvalue(self,id,name,age,department,salary):
        self.id=id
        self.name=name
        self.age=age

        self.department=department
        self.salary=salary
    def printvalue(self):
        print("id",self.id)
        print("name",self.name)
        print("age",self.age)
        print("companyname",Employee.companyname)
        print("department",self.department)
        print("salary",self.salary)

em1=Employee()
em1.setvalue("203wd","sumayya",24,"software",25000)
em1.printvalue()
