class Car:
    wheels = 4
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model} {self.color}"
    
    def move(self):
        return f"{self.year} {self.make} {self.model} {self.color}"
    
    def move(self):
        return f"{self.make} is moving"
        
my_car = Car("Toyota", "Corolla", "Blue", 2022)
print(my_car.get_description())        

my_car = Car("Toyota", "Corolla", "Blue", 2026)
print(my_car.get_description())