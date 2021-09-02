class Student:
    def __init__(self,name,rollno,dprtmnt,college):
        self.name=name
        self.rollno=rollno
        self.dprtmnt=dprtmnt
        self.college=college
    def print(self):
        print(self.name)
        print(self.rollno)
        print(self.dprtmnt)
        print(self.college)
    def __str__(self):
       # return self.name+self.dprtmnt
         return self.name+str(self.rollno)   # integer odkkumbo athine string lott  convert cheyyanm

st=Student("sumi",33,"physics","psmo")
st.print()
print(st)