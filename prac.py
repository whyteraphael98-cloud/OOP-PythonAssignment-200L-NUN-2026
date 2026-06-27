my_list = [1, 4, 5, 6, 7]
print(my_list[3])
my_list.append(9)
print(my_list)
print(my_list[1:3])
my_list.remove(5)
print(my_list)
del my_list[3]
print(my_list)
my_list.extend([2, 3, 4])
print(my_list)

new_list = my_list + [56, 78, 23]
print(new_list)


b_tuple = (7, 8, 9 , 4, 3)
print(b_tuple[4])
print(len(b_tuple))

b = 7
n = 9 
m = 4
upon = (b, n, m)
x, y, z = upon
print(y)

new_dict = {"Name": "Orayi", "Age": 18, "Race": "Black"}
print(new_dict["Name"])

new_dict["City"] = "Abuja"
print(new_dict)
removed_stuff = new_dict.pop("Race")
print(new_dict)

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 4, 3}
my_set.remove(4)
print(my_set)

s = "Sipline"
s = s + " are trustworthy partners"
print(s)


n = "Birkin"
print(n[-2])

m = "ford, toyota, mercedez"
cars = m.split(", ")
print(cars)


b = 7.889
i = 4.987

division = round(b/i, 1)
print(division)


sentence = "data science with data and science"

words = sentence.split()

unique_words = set(words)

print(unique_words)

x = 56
x += 14
print(x)

c = -67.89
print(abs(c))

for num in range(1, 10):
    if num % 2 == 0:
        print(num)

def greet(first_name, last_name):
    print("Hello", first_name, last_name)

greet("Orayi", "Jordan")     
greet("Ozigi", "Junior")