class Person:
    def printp(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def printc(self,school,std):
        self.school=school
        self.std=std
        print(self.school,self.std)
class Parent(Person):
    def printm(self,job,place):
        self.job=job
        self.place=place
        print(self.job,self.place)
class Student(Child):
    def printf(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)

ch=Child()
ch.printp("any",8)
ch.printc("abc",4)
pr=Parent()
pr.printp("anu",30)
pr.printm("doctor","kakanad")
st=Student()
st.printc("cvb",5)
st.printf(64,89)