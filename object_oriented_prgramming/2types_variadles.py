# types of variables
# instance variables.....related to methods.....calls using self
#static variables.....related to class.....calls using class


class Student:
    school="luminar"
    def setval(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def printval(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print(Student.school)

st=Student()
st.setval("sumayya",3)
st.printval()

st1=Student()
st1.setval("anu",4)
st1.printval()