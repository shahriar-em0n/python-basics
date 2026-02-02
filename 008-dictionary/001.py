chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Fresh"}

for chai in chai_types:
    print(chai)


for tea in chai_types:
    print(tea, chai_types[tea])

print(chai_types)
chai_types["Earl Grey"] = "citrus"
print(chai_types)

print(chai_types.pop("Ginger"))
print(chai_types)


print(chai_types.popitem())

del chai_types["Green"]
print(chai_types)

ctc = chai_types.copy()
print(ctc)

teaShop = {
    "Chai": {"Masala": "Spicy", "ginger": "Zesty" },
    "Tea": {"Green": "Mild", "Black": "Strong"},
}

print(teaShop)

print("only chai",teaShop["Chai"])
print("Only Tea ", teaShop["Tea"])

keys = ["Masala", "ginger", "Lemon"]
print(keys)

dv = "Delicious"
nd = dict.fromkeys(keys, dv)
print(nd)


