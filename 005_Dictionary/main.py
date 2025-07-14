# Basic dictionary

tea_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(tea_types)

# see each dictionary

print(tea_types["Masala"])
print(tea_types["Green"])


# get method

print(tea_types.get("Ginger"))

# change the key value 

tea_types["Green"] = "Fresh"
print(tea_types)

# using loop 

for tea in tea_types:
    print(tea)
    
# using loop print key & value 

for tea in tea_types:
    print(tea,": ", tea_types[tea])
    

# items method

for key, value in tea_types.items():
    print(key, value)
    

# using condition

if "Masala" in tea_types:
    print("I have masala tea")
    
# see all items in len method

print(len(tea_types))

# add new dictionary

tea_types["Earl Grey"] = "Citrus"

print(tea_types)

# pop method

print(tea_types.pop("Ginger"))

# popitem method

print(tea_types.popitem())

# meomory ref delete

del tea_types["Green"]

# copy method

tea_types_copy = tea_types.copy()
 
 
 ### eta abar dekhe than notes banaite hobe
 