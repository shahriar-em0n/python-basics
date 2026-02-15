class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def showInfo(self):
        print(self.name, self.email)


userOne = User("Shahriar", "shahriar@gmail.com")
userOne.showInfo()


class Admin(User):
    def changeSetting(self):
        print("Changed Setting successfully")


adminOne = Admin("Shahriar", "Shahriar@Gmail.com")
adminOne.showInfo()
adminOne.changeSetting()


class Student(User):
    def takeExam(self):
        print("Exam taken succesfully")

studentOne = Student("Abdullah", "abdullah@gmail.com")
studentOne.showInfo()
studentOne.takeExam()
