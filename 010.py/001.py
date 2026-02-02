number = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]

for num in number:
    print(num)
    
pnc = 0
for num in number:
    if num >0:
        pnc +=1
print("Final count of pnc is :", pnc)