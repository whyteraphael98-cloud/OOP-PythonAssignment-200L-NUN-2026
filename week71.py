class Bicycle(Vehicle):
    def __init__(self, make, model, year, frame_type):
        super().__init__(make, model, year)
        self.frame_type = frame_type

    def ring_bell(self):
        print(f"The {self.year} {self.make} {self.model} rings its bell.")

my_car = car("Toyota", "Camry", 2022, 4)
my_bicycle = Bicycle("Schvinn")            