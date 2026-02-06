n = [i for i in range(1, 21)]
print(n)

nSquare = [i**2 for i in range(1, 21)]  # list comprehention
print(nSquare)


# map
def square(x):
    return x**2

print(f"lamda - {list(map(lambda x: x**2, n))}") # using map
