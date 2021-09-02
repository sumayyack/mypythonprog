# multilevel inheritance

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
class Student(Child):
    def printS(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)

st=Student()
st.printp("anu",3,)
st.printc("snm",4)
st.printS(6,54)
