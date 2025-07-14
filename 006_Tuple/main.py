tea_types = ("Black", "Green", "White")

print(tea_types[0])

# len method

print(len(tea_types))

more_tea = ("Herbal", "Earl grey")

all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have Green tea")

#change ref

more_tea = ("Herbal", "Earl Grey", "Herbal")

print(more_tea)

#count method

print(more_tea.count("Herbal"))


#type method
print(type(tea_types))

