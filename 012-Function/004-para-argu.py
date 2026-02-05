def square(x):
    print(x ** 2)

def celciusToFarenheite(celcius):
    farenheite = celcius * 9 / 5 + 32
    print(farenheite)
    
def namta(x):
    tenx = x * 10
    temp = x
    while x <= tenx:
        print(x)
        x += temp
        
square(5)
celciusToFarenheite(50)
namta(10)