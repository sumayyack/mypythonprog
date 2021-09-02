#stdnt class

class Student:
    def setvalue(self,name,standard,rollno,schoolname):
        self.name=name
        self.standard=standard
        self.rollno=rollno
        self.schoolname=schoolname
    def printvalue(self):
        print("name",self.name)
        print("standard",self.standard)
        print("rollno",self.rollno)
        print("schoolname",self.schoolname)


st=Student()
st.setvalue("sumayya",3,33,"abc")
st.printvalue()









