tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities)
print(tea_varities[-3])
print(tea_varities[1:3])
print(tea_varities[:2])
print(tea_varities[2:])

#change 

tea_varities[3]="Herbal"
print(tea_varities)

#tea_varities[1:2] = "Lemon"
print(tea_varities) #this is the wrong way to adding 

# right way

tea_varities[1:2] = ["Lemon"] # passing as like a array

print(tea_varities)

tea_varities[1:3] = ["green", "coffe"]
print(tea_varities)


print(tea_varities)

tea_varities[1:1]
print(tea_varities) 

tea_varities[1:1] = ["test", "test"]

print(tea_varities)

tea_varities[1:3]
print(tea_varities)

# insert nothing

tea_varities[1:3] = []
print(tea_varities)


# cheack the original 

print(tea_varities)



# Append

tea_varities.append("longTea")
print(tea_varities)


# pop method

tea_varities.pop()
print(tea_varities)

# remove method

tea_varities.remove("green")

print(tea_varities)

# insert method

tea_varities.insert(1, "green")
print(tea_varities)

# copy method

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

# append tea_varities_copy

tea_varities_copy.append("Lemon")
print(tea_varities_copy)

print(tea_varities)
