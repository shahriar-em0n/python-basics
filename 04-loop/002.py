x = int(input('Enter the number : '))
Flag = True

i = 2 
while i < x:
    if x %  i == 0:
        Flag = False
    i +=1
    
if Flag:
    print("Prime number")
else:
    print("Not prime")