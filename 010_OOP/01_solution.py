class Car:
    def __init__(self, userBrand, userModel):
        self.brand = userBrand
        self.model = userModel
    
car_details = Car("Toyota", "Corolla")
print(car_details.brand)
print(car_details.model)