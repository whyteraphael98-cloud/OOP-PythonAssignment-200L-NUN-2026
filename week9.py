class Person:
    def __new__(cls, name, age):
        print(f"Creating a new Person object")
        instance = super().__new__(cls)
        return instance
    def __init__(self, name, age):
        print(f"Initializing Person Object")
        self.name = name
        self.age = age
    def __del__(self):
        print(f"{self.name} is being destroyed")

p = Person("Alice", 45)  

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point at ({self.x}, {self.y})"
    def __repr__(self):
        return f"Point ({self.x}, {self.y})"
    def __format__(self, format_spec):
        if format_spec == "polar":
            r = (self.x**2 + self.y**2)**0.5
            theta = math.atan2(self.y, self.x)
            return f"r={r:.2f}, ={theta:.2f}"
        return str(self)
    
p = Point(3, 4)
p
print(str(p))
print(repr(p))
print(f"{p:polar}")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self.celsius == other.celsius
        return False
    def __lt__(self, other):
        if isinstance(other, Temperature):
            return self.celsius < other.celsius
        return NotImplemented
    def __bool__(self):
        return self.celsius > 0

t1 = Temperature(20)
t2 = Temperature(30)
t3 = Temperature(20)
print(t1 == t3)
print(t1 < t2)
print(bool(t1))   

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, item, quantity=1):
        self.items[item] = self.items.get(item, 0) + quantity

    def __getitem__(self, item):
        return self.item.get(item, 0)

    def __setitem__(selef, item, quantity):
        if quantity <= 0:
            if item in self.items:
                del self.items[item]
            else:
                self.items[item] = quantity
    def __len__(self):
        return sum(self.item.values())

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        for item, quantity in self.items.items():
            for _ in range(quantity):
                yield item
    def __str__(self):
        if not self.items:
            return "Empty Cart"
        return "\n".join(f"{q}x {i}" for i, q in self.items.items())

cart = ShoppingCart()
cart.add("apple", 3)
cart.add("banana", 2)

print(len(cart))
print("apple" in cart)
print(cart["apple"])

cart["orange"] = 