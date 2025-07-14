name = "Shahriar"
print(name)

tea = "Masala tea"

first_tea = tea[0]
print(first_tea)

# slice

slice_tea = tea[0:6]
print(slice_tea)

num_list = "0123456789"
print(num_list)

slice_num= num_list[1:5]

print(slice_num)

slice_num_two = num_list[0:]

print(slice_num_two)

slice_num_three = num_list[:5]
print(slice_num_three)

slice_num_four = num_list[0:7:2]
print(slice_num_four)

slice_num_five = num_list[0:7:2]

slice_num_six = num_list[-0:7]
print(slice_num_six)

slice_num_seven = num_list[-0:-7]
print(slice_num_seven)

# function

tea1 = "black tea"
print(tea1.lower())
print(tea1.upper()) 

# strip fucntion

tea2 = "     milk tea     "
print("with out using strip - ", tea2)
print("using with strip - ",tea2.strip())

# replace func
tea3 = "green tea"
print(tea3.replace("green tea", "black tea"))

# split func

tea4 = "Pu-erh Tea, Oolong Tea, White Tea, Milk Oolong"
print(tea4.split())

print(tea4.split(", "))


# find func

tea5 = "rong cha"
print(tea5.find("cha"))

# count func

tea6 = "tea tea tea white white white"
print(tea6.count("tea"))
print(tea6.count("white"))

#  Order formating

tea_type = "lemon"
quantity = 2

order = "I orderd {} cups of {} tea"
print(order)

# format func

print(order.format(quantity, tea_type))

#list 

tea_variety = ["Lemon", "Masala", "White", "Milk"]
print(tea_variety)

# join func

print(" ".join(tea_variety))
print("-".join(tea_variety))
print(", ".join(tea_variety))

# len func

print(len(tea))


# \ \ usgaes

say = "He said , \"White tea is awesome\""
print(say)

