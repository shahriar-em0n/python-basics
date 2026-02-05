def namta():
    x = int(input('Enter a number: '))
    tenx = x * 10
    temp = x
    while x <= tenx:
        print(x)
        x += temp
        
namta()