# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price


# Bmw = Car("BMW", "M5", "10000000")
# print(Bmw.brand)
# print(Bmw.model)
# print(Bmw.price)

# cars = [
#     Car("Toyota", "Prius", "50000"),
#     Car("Toyota", "LC200", "50000"),
#     Car("Toyota", "camry", "50000"),
#     Car("Toyota", "Premio", "50000"),
#     Car("Toyota", "Alion", "50000")
# ]

# for car in cars:
#     print(car.brand)
#     print(car.model)
#     print(car.price)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("toyota", "Corolla")
print(my_car.brand.capitalize())
print(my_car.model.capitalize())

new_car = Car("Tata", "safari")
print(new_car.model.capitalize())
print(new_car.brand.capitalize())
