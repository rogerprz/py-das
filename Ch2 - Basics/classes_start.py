class Vehicle():
    def __init__(self, bodyStyle):
        self.bodyStyle = bodyStyle
    
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, engineType):
        super().__init__("Car")
        
        self.wheels = 4
        self.doors = 2
        self.engineType = engineType
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engineType, "car at ", self.speed, "mph")

class Motorcycle(Vehicle):
    def __init__(self, engineType, hasSideCar):
        super().__init__("Motorcycle")
        if (hasSideCar):
            self.wheels = 3
        else:
            self.wheels = 2
            
        self.doors = 0
        self.engineType = engineType
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engineType, "motorcycle at ", self.speed, "mph")

car1 = Car("gas")
car2 = Car("Electric")
bike1 = Motorcycle("Gasoline", False)

print(car1.bodyStyle)
print(car1.engineType)
print(car2.doors)
print(bike1.wheels)


car1.drive(55)
car2.drive(70)
bike1.drive(60)

