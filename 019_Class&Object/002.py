class Customer:
    def __init__(self, id, budget):
        self.id = id
        self.budget = budget

    def buyProduct(self, price):
        self.budget -= price


C1 = Customer("22", 5000)
C1.buyProduct(4000)
print(C1.budgetsssssssssssssss)
