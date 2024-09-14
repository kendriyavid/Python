## System design
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def __printModel(self):
        return self.model

    def printBrand(self):
        return self.brand

class ElectricCar(Car):
    def __init__(self,brand,model,batterySize):
        super().__init__(brand,model)
        self.batterySize = batterySize