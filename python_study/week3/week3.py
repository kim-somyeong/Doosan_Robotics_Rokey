'''
#문제5
class Car:
    def __init__(self, make, model):
        self.make= make
        self.model= model
    
    def print(self):
        return (f'{self.make} {self.model}')

car= Car("KIA", "K3")
print(f'{car.print()} is starting')

#문제7
class Car:
    def __init__(self, make, model):
        self.make= make
        self.model= model
    
    def print(self):
        return (f'{self.make} {self.model}')


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size= battery_size

    def print(self):
        return f'{super().print()} {self.battery_size}'

Electric= ElectricCar("Kia","K3","75kWh")

print(Electric.print())

'''
#문제8
class Car:
    def __init__(self, make, model):
        self.make= make
        self.model= model
    def start(self):
        print(f'{self.make}{self.model}is starting')

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    
    def start(self):
        print(f"{self.make} {self.model} with a {self.battery_size} battery is starting")

my_electric_car= ElectricCar("Tesla","Model S", "75kWh")

my_electric_car.start()