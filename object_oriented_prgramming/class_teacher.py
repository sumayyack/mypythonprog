class Teacher:
    college=" PSMO"
    def __init__(self,name,id,subject,department):
        self.name=name
        self.id=id
        self.subject=subject
        self.department=department
    def printvalue(self):
        #print(self.name,self.id,self.subject,self.department,Teacher.college)
         print(self.name)
         print(self.id)
         print(self.subject)
         print(self.department)
         print(Teacher.college)
tr1=Teacher("sumayya",229,"maths","lp")
tr2=Teacher("anu",216,"eng","up")
tr1.printvalue()
tr2.printvalue()