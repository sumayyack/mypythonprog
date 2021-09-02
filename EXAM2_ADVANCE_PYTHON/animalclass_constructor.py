class Animal:
    def __init__(self,name,number_of_legs):
        self.name=name
        self.number_of_legs=number_of_legs
    def print(self):
        print(self.name)
        print(self.number_of_legs)

class Dog(Animal):
    def __init__(self,breed,color,name,number_of_legs):
        super().__init__(name,number_of_legs)
        self.breed=breed
        self.color=color
    def printv(self):
        print(self.breed)
        print(self.color)

dg=Dog("german sheperd","black","Tommy",4)
dg.print()
dg.printv()