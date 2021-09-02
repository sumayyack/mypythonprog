class Student:
    def set(self,name,std,division,):
        self.name=name
        self.std=std
        self.division=division
        print(self.name,self.std,self.division)

    def __str__(self):
        return self.name+str(self.std)

st=Student()
st.set("anu",7,"D")
print(st)

