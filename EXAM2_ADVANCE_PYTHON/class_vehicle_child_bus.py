class Vehicle:
    def set(self,model,regno,color):
        self.mode=model
        self.regno=regno
        self.color=color
        print(self.model,self.regno,self.color)



class Bus(Vehicle):
    def setv(self,nameofbus,route):
        self.nameofbus=nameofbus
        self.route=route
        print(self.nameofbus,self.route)

bs=Bus()
bs.set("limitedstop","kl55AD4565","red")
bs.setv("ksrtc","kozhikode")
