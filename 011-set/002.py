A = input("Enter the first set: ")
A = set(A.split(" "))
# print(set(a.split(' ')))


b = input("Enter the sec set: ")
b = set(b.split(" "))
print(A, b)

print(f"union - {A.union(b)}")
print(f"interssection - {A.intersection(b)}")
print(f"difference - {A.difference(b)}")
