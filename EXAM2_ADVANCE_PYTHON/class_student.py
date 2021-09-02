class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def print(self):
        print("name",self.name)
        print("rollno",self.rollno)
        print("course",self.course)
        print("mark",self.mark)
lst=[]
f1=open("studentmark",'r')
for r in f1:
    m=r.rstrip("\n").split(",")
    print(m)
    name=m[0]
    rollno=m[1]
    course=m[2]
    mark=m[3]
    st=Student(name,rollno,course,mark)
    st.print()
    lst.append(st)
#print(mark)
mark=[]
for s in lst:
    mark.append(s.mark)
print(mark)
for s in lst:
    if (s.mark==max(mark)):
        print(s.rollno,s.name,s.course,s.mark)

# file nn maximum mark print cheyyunna prgrm