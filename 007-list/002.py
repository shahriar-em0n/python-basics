scores = [72, 75, 71, 74]
print(int(sum(scores) / len(scores)))

# Empty List
empty = []

# List of strings
colors = ["red", "green", "Blue"]

# list of booleans
flags = [True, False, True]

# List of mixed typed
info = ["Alice", 30, 3.5, False]

# List of inside a list(nesed)
matrix = [[1, 2], [3, 5], [5, 6]]

fruits = ["apple", "banana", "cherry"]
print(fruits[::-1])

number = [10, 20, 30, 40, 50]
print(number[::-1])
print(number[-3::])


fruits = ["apple", "banana", "cherry"]
fruits[1] = "Bluebery"
print(fruits)

fruits.append("Mango")
print(fruits)

fruits.insert(3, "Lici")
print(fruits)

fruits2 = ["Grapes", "Kiwi"]
fruits.extend(fruits2)
print(fruits)

fruits.remove("Lici")
print(fruits)

fruits.pop(3)
print(fruits)

del fruits[1:3]
print(fruits)

fruits.clear()
print(fruits)

a = [1, 2, 3]
print(a)

b = a
print(b)

b.append(4)
print(b )
