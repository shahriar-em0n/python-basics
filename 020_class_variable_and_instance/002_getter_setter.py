class BannkAccoount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def setBalance(self, newBanalce):
        self.__balance = newBanalce


aiblAccount = BannkAccoount("Shahriar", 10000)
print(aiblAccount.getBalance())

aiblAccount.setBalance(14000)
print(aiblAccount.getBalance())
