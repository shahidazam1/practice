# lists

from functools import reduce


myList = [1, 2, 3, 4, 5]
print(myList)

for i in myList:
    print(i+1)

# tuples
myTuple = (1, 2, 3, 4, 5)
print(myTuple)

for i in myTuple:
    print(i+1)


# sets 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
myset = set(list1 + list2)
print(f"set of list1 {list1} and list2 {list2}: {myset}")

# loops
print("for loop which prints numbers from 0 to 4:")
for i in range(5):
    print(i)

# while loop
print("while loop which prints numbers from 0 to 4:")
i = 0
while i <5:
    print(i)
    i += 1


# conditions
if 5 > 3:
    print("5 is greater than 3")
elif 5 < 3:
    print("5 is less than 3")
else:
    print("5 is equal to 3")

# functions
def my_function(x):
    return x + 1

print(my_function(5))



# Calculate:

# sum
# average
# maximum
# minimum
numbers = [10, 20, 30, 40, 50]
print("Calculations on the list of numbers [10, 20, 30, 40, 50]:")
sum =0
for i in numbers:
    sum+=i
print(f"Sum: {sum}")
print(f"Average: {sum/len(numbers)}")

# maximum
max_number = 0
for i in numbers:
    if i > max_number:
        max_number = i
print(f"Maximum: {max_number}")

# minimum
min_number = numbers[0]
for i in numbers:
    if i < min_number:
        min_number = i
print(f"Minimum: {min_number}")

# Day 2
print("Day 2")

myList = [1, 2, 3, 4, 5]
print("List:", myList)
updatedList = [i*i for i in myList if i % 2 == 0]
print("Updated List:", updatedList)

# lambda function

sum_of_tow_numbers = lambda x,y: x+y
print("Sum of 5 and 10 using lambda function:", sum_of_tow_numbers(5, 10))

def func(*args):
    for i in args:
        print(i)
    return "completed"
val = func(1, 2, 3, 4, 5, "hello", "world")
print(val, type(val))


def func2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print(func2(name="Alice", age=30, city="New York"))


def func3(*args, **kwargs):
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def func4(x, y):
    print(f"x: {x}, y: {y}")
    return x + y

print("Sum of 5 and 10 using func4:", func4(y=10,x=5))

mapList = [1, 2, 3, 4, 5]
def mapSquare(x):
 return x*x
mappedlist = map(mapSquare, mapList)

print ("Mapped List:", list(mappedlist))

def func5(x):
    return x==4

filteredlist = filter(func5, mapList)
print("Filtered List:", list(filteredlist))

# filter example
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, mapList))
print("Even Numbers:", even_numbers)

def sum(x, y):
    return x + y 

sum_result = reduce(sum, mapList)
print("Sum of all numbers in mapList using reduce:", sum_result)

# convert list to dictionary
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
my_dict = dict(zip(keys, values))
print("Dictionary:", my_dict)

# file I/O
file = open("students.txt", "r")
content = file.read()
print("Content of students.txt:", content)
file.close()


with open("students.txt", "r") as file:
    content = file.read()
    print("Content of students.txt using with statement:", content)

    with open("output.txt", "a") as file1:
        file1.write("Hello i am append call\n")

import json

with open("student.json", "w") as json_write_file:
    data_to_write = [{"name": "John", "marks": 85}, {"name": "Alice", "marks": 90}]
    json.dump(data_to_write, json_write_file)
    print("Data written to student.json")

with open("student.json", "r") as json_file:
    data = json.load(json_file)
    print("Content of student.json:", data)

data.append({
    "name": "Shahid",
    "marks": 85
})

with open("student.json", "w") as json_append_file:
    data_to_append = [{"name": "Bob", "marks": 75}]
    json.dump(data, json_append_file)
    print("Data appended to student.json")

try:
    input_number = int(input("Enter a number: "))
    print(f"You entered: {input_number}")
except ValueError:
    print("Invalid input. Please enter a valid number.")