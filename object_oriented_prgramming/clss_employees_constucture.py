class Employee:
    def __init__(self,name,id,salary,company):
        self.name=name
        self.id=id
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.name,self.id,self.salary,self.company)

em=Employee("sumayya",112,25000,"abc")
em.printvalue()