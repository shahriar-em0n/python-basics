# def cube(x):
#     return x ** 3
# three_Cube = cube(3)
# print(three_Cube)


# def intro(name, age, country):
#     print("Hello Everyone!")
#     print(f"My Name is {name}")
#     print(f"I'm {age} years old")
#     print(f"I'm living {country}")
#     print("Good Bye!")

#     return name, country

# details = intro("Mohammad Shahriar", 20, "Bangladesh")


# def sumOfEven(li):
#     total = 0
#     for i in li:
#         if i % 2 == 0:
#             total += i
#     return total


# evenSUm = sumOfEven([1, 2, 3, 4, 5, 6, 7, 8])
# print(evenSUm)


def fun():
    '''Hello it will retunr son'''
    return "Hello", 12, True


print(type(fun()))
a, b, c = fun()
print(f"whitout type - {a}")
print(f"whitout type -{b}")
print(f"whitout type -{c}")

print(type(a))
print(type(b))
print(type(c))

print(fun.__doc__)
