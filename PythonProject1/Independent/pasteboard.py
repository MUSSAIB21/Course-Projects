class Car:
    def __init__(self, name="Default", age=10, i_d="", maxSpeed=100, currentSpeed=0):
        self.name = name

        self.age = age
        self.id = id
        self.maxSpeed=maxSpeed
        self.currentSpeed=currentSpeed
    def accelerate(self):
        self.currentSpeed += 10
        if self.currentSpeed > self.maxSpeed:
            self.currentSpeed = self.maxSpeed
    def brake(self):
        self.currentSpeed -= 10
        if self.currentSpeed < 0:
            self.currentSpeed = 0
m1=Car("MercedesM1",)
m1.accelerate()
m1.accelerate()
m1.accelerate()
print(m1.currentSpeed)
student={"Name":2
        ,"House":3}
def get_name():
    return lambda student: student.get("Name")
