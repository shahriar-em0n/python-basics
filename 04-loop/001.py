x = 1
while x <= 500:
    print("hello world", x)
    x += 1

name = "Shahriar"
for x in name:
    print(x.title())
    
for i in range(0, 10):
    print(list(range(i)))
    

for i in range(0, 10, -1):
    print("hello world", i)
    print(list(range(i)))
    
fruits = ['apple', 'banana', 'cherry', 'mango']
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i]) 
    