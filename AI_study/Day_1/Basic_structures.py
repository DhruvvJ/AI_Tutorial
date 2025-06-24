# Variable and Data Type :-

x = 10
y = 1.5
name = "Dhruv"
is_active = True

print(type(x), type(y), type(name), type(is_active))

# List :-

fruits = ["apple", "banana", "grapes"]
print(fruits)
print(fruits[0])
fruits[0] = "guava"
print(fruits)

fruits.append("apple")
print(fruits)

fruits.insert(2,"orange")
print(fruits)

fruits.remove("grapes")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

# Tuple :-

colors = ("red", "green", "blue", "yellow", "purple")
print(colors)

print(colors[0])

# Dictionaries ;-
student = {"name":"Dhruv", "age":23, "branch":"B-Tech"}
print(student)

print(student["name"])

student["age"] = 21

student["college"] = "SVVV"

print(student)

# sets :-
numbers = {1,2,3,4,6,7,8,9,}
print(numbers)

numbers.add(0)
print(numbers)

numbers.remove(0)
print(numbers)

# List Comprehensions :-
squares = [x**2 for x in range(10)]
print(squares)

even = [x for x in range(10) if x % 2 == 0]
print(even)

# Generator Expressions :- memory efficient loops
gen = (x**2 for x in range(1,100000))
print(next(gen))
print(next(gen))

# Create a list of 5 fruits. Replace the third fruit with “kiwi”.
fruit_list = ["apple", "banana", "grapes"]
fruit_list[2] = "kiwi"

print(fruit_list)

# Create a tuple of 3 colors. Try changing one value and note what error occurs.
color_tuple = ("red","green","blue")
color_tuple[0] = "white"

#TypeError: 'tuple' object does not support item assignment


# Create a dictionary with 3 keys: name, age, course. Add a new key “email”.
dict = {"name": "Dhruv", "age":23, "course":"CS"}
dict["email"] = "dhruv@gmail.com"

print(dict)

# Create a set from a list of numbers with duplicates: [1,2,2,3,4,4,5]
set1 = {1,2,2,3,4,4,5}
print(set1)

#Write a list comprehension to get all numbers from 1 to 20 divisible by 3.
divby3 = [x for x in range(1,21) if x % 3 == 0]
print(divby3)

# Create a generator expression to yield cube of first 10 numbers.
gen2 = (x**x*x for x in range(1,11))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

