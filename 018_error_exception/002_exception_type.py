try:
    x = int(input("Enter your value: "))
    print(10 / x)
    print(10 + "fox")
except ZeroDivisionError:
    print("Can't divide by zero!")

except TypeError:
    print("Type Error!")

except Exception as e:
    print(e)
    print("Something is wrong!")
else:
    print("Everything is printed")
finally:
    print("I always run ")
