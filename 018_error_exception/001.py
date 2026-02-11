try:
    x = int(input("Enter your value: "))
    print(10 / x)
except Exception as e:
    print(e)
    print("Something is wrong!")
else:
    print('Everything is printed')
finally:
    print('I always run ')