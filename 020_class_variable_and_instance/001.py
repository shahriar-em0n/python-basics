class Customer:
    coupons = {"Dec": 20, "Last": 30, "SH": 50}

    def __init__(self, id, budget, cupon):
        self.id = id
        self.budget = budget
        self.coupon = cupon

    def buyProduct(self, price):
        couponValue = 0
        for key, value in self.coupons.items():
            if key == self.coupon:
                couponValue = value
        discountPrice = price * (100 - couponValue) / 100
        self.budget = self.budget - discountPrice


cust1 = Customer(2, 5000, "Dec")
cust1.buyProduct(400)
print(cust1.budget)


cust2 = Customer(8, 10000, "SH")
cust2.buyProduct(10000)
print(cust2.id)
print(cust2.budget)
  