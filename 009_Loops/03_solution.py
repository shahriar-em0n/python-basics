number = 3

for i in range(1, 11):
    print(number, 'x', i, '=', (number * i))
    

# remove 5th iteration 

number = 3

for i in range(1, 11):
    if i == 5 :
        continue
    print(number, 'x', i, '=', (number * i))