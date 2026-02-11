class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


Bmw = Car("BMW", "M5", "10000000")
print(Bmw.brand)
print(Bmw.model)
print(Bmw.price)

cars = [
    Car("Toyota", "Prius", "50000"),
    Car("Toyota", "LC200", "50000"),
    Car("Toyota", "camry", "50000"),
    Car("Toyota", "Premio", "50000"),
    Car("Toyota", "Alion", "50000")
]

for car in cars:
    print(car.brand)
    print(car.model)
    print(car.price)