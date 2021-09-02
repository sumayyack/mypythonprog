class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def print(self):
        print(self.model,self.regno,self.color)
    def __str__(self):
        return self.model+self.color

vh=Vehicle("grazia","KL55D9435","grey")
vh.print()
print(vh)