class Book:
    def __init__(self, title, author, price, code):
        self.title = title
        self.author = author
        self.price = price
        self.__code = code

    def getCode(self):
        return self.__code

    def setCode(self, newCode):
        self.__code = newCode


book1 = Book("Theory of Relativity", "Shahriar", 200, "AB3214")
print(book1.getCode())
print(book1.setCode("EF569"))
print(book1.getCode())
