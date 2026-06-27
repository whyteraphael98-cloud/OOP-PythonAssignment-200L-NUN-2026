class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model}'s engine is stopped.")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        print(f"The {self.year} {self.make} {self.model} beeps its horn")
