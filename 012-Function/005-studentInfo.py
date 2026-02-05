def showStudentInfo(name, roll, email, phone):
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")


showStudentInfo("Shahriar", 450, "shahriar@gmail.com", 58484544)

print()

# by default 
def showStudentInfo2(name, roll, email='xxx@gmail.com', phone='017xxxxxxxx'):
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

showStudentInfo2(
    name="Shahriar",
    phone=58484544,
    roll=450,
    email="",
)
