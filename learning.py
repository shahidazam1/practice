# lists

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