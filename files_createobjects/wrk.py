class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printv(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("course",self.course)
        print("mark",self.mark)
f1=open("wrk",'r')
for w in f1:
    k=w.split(",")
    name=k[0]
    rollno=k[1]
    course=k[2]
    mark=k[3]
    st=Student(name,rollno,course,mark)
    st.printv()