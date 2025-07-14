input_string = "teeter"

for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print("char is : ",char)
        break