greeting = "Hello"
name = "Alice"
 
full_greeting = greeting + " " + name
print(full_greeting) 


upper_case_version = full_greeting.upper()
print(upper_case_version)

lower_case_version = full_greeting.lower()
print(lower_case_version)


my_list = [1, 2, 3, 3, 5]
print("My list", my_list)


print(my_list[1:4])

my_list[0] = 6
print(my_list)
my_list.append(8)
print(my_list)
my_list.insert(3, 9)
print(my_list)

print(len(my_list))

tuple_whyte = (9, 8, 7)
print(tuple_whyte)

A = 5
B = 65
unopian_tuple = (A, B)
print(unopian_tuple)


my_dictionary = dict(name = "Bob", age = 98, city= "Abuja")

print(my_dictionary["city"])
print(my_dictionary["name"])

print(len(my_dictionary))

my_set = set([1, 2, 3, 4, 5, 6])
print(my_set)


settings = set([1, 5, 9, 3, 2])
settings2 = set([6, 7, 3, 6, 8])

union = settings | settings2
print(union)


intersection = settings & settings2
print(intersection)


number = 3.4456
rounded = round(number, 0)
print(rounded)


# Exercise 1: List of favorite foods
print("\n--- Exercise 1: Favorite Foods ---")
favorite_foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos"]
print("First food:", favorite_foods[0])
print("Last food:", favorite_foods[-1])
print("Middle three foods:", favorite_foods[1:4])


# Exercise 2: Student dictionary
print("\n--- Exercise 2: Student Dictionary ---")
student = {"name": "John", "age": 20, "grade": "A"}
print("Before update:", student)

student["grade"] = "A+"
print("After update:", student)


# Exercise 3: Find unique words using a set
print("\n--- Exercise 3: Unique Words ---")
sentence = "data science with data and science"
words = sentence.split()
unique_words = set(words)
print("Original sentence:", sentence)
print("All words:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))


# Exercise 4: Word frequency counter
print("\n--- Exercise 4: Word Frequency Dictionary ---")

def word_frequency(sentence):
    """
    Takes a sentence as input and returns a dictionary with word frequencies.
    """
    words = sentence.split()
    frequency_dict = {}
    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

# Test the function
test_sentence = "to be or not to be"
result = word_frequency(test_sentence)
print(f"Sentence: '{test_sentence}'")
print(f"Word frequencies: {result}")

# Alternative using .get() method
print("\n--- Alternative approach using .get() ---")
def word_frequency_v2(sentence):
    words = sentence.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

result2 = word_frequency_v2(test_sentence)
print(f"Word frequencies: {result2}")


# Exercise 5: Reverse each word while maintaining word order
print("\n--- Exercise 5: Reverse Each Word ---")

def reverse_words(sentence):
    """
    Takes a sentence as input and returns a new sentence where each word 
    is reversed, while maintaining the original word order.
    """
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Test the function
test_sentence2 = "hello world"
result3 = reverse_words(test_sentence2)
print(f"Original sentence: '{test_sentence2}'")
print(f"Reversed words: '{result3}'")

# More examples
test_cases = ["hello world", "python programming", "to be or not to be"]
print("\nMore examples:")
for test in test_cases:
    print(f"'{test}' -> '{reverse_words(test)}'")

# User's attempt (fixed)
phrase = input("put sumn")
thep = phrase.split()
reverse = [word[::-1] for word in thep]  # Reverse each word individually
print(reverse)




count = 7
while count<15:
    count += 2
    print(count)

