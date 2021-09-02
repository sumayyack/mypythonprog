class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def print(self):
        print(self.model)
        print(self.regno)
        print(self.color)

vh=Vehicle("grazia","KL55D9435","grey")
vh.print()
print(vh)