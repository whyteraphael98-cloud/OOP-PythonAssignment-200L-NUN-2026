class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.species} makes a generic animal sound.")

    def daily_task(self):
        print(f"{self.name} the {self.species} has a generic daily task.")


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def make_sound(self):
        print(f"{self.name} the {self.species} says: Roar")

    def daily_task(self):
        print(f"{self.name} the {self.species} patrols the territory.")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def make_sound(self):
        print(f"{self.name} the {self.species} says: Trumpet")

    def daily_task(self):
        print(f"{self.name} the {self.species} takes a mud bath.")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def make_sound(self):
        print(f"{self.name} the {self.species} says: Hiss")

    def daily_task(self):
        print(f"{self.name} the {self.species} basks in the sun.")


if __name__ == "__main__":
    zoo_animals = [
        Lion("Leo"),
        Elephant("Ella"),
        Snake("Slyther"),
        Animal("Mystery", "Unknown")
    ]

    for animal in zoo_animals:
        animal.make_sound()
        animal.daily_task()
        print()
