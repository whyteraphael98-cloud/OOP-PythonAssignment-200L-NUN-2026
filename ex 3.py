x = -14
if x>0:
    print("x is positve")
else:
    print("x is negative")



age = 17
if age >= 18:
    print("Adult")
if age >= 70:
    print("Senior Citizen")
if age >= 13:
    print("Teenager")
else:
    print("Child")
num = 87
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is zero")
elif num > 0:
    print("number is positive")
else:
    print("this is not a number")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
appended_fruits = ["orange", "grape"]
fruits.extend(appended_fruits)
print(fruits)

count = 7
while count < 19:
    print(count)
    count += 1


number_of_days = 366
if number_of_days%6 == 0:
    print("leap year")
else:
    print("not a leap year")

year = 2036
if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("leap year")
else:
    print("not a leap year")



