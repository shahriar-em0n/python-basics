import random


print(random.random())


print(random.randint(1, 10))






# ----------------------------
# Python Arithmetic Operations
# ----------------------------

# Basic variables
x = 2
y = 3
z = 4

# (x + y) * z → Parentheses first, then multiplication
ans = (x + y) * z
print("Result of (x + y) * z:", ans)  # Output: 20

# x + (y * z) → Multiplication first, then addition
ans2 = x + (y * z)
print("Result of x + (y * z):", ans2)  # Output: 14


# ----------------------------------
# Convert Float number to Integer
# ----------------------------------
print("Convert float to int:", int(5.78))  # Output: 5 (decimal part removed)

a = 5.50
print("Add int(50) with float a:", int(50) + a)  # Output: 55.5


# ----------------------------------
# Convert Integer number to Float
# ----------------------------------
print("Convert number to float:", float(72.22))  # Output: 72.22

b = 10
print("Add float(5.50) with int b:", float(5.50) + b)  # Output: 15.5


# ----------------------------
# Operator Overloading Example
# ----------------------------
# '+' is used here to concatenate two strings
print("Python Overloading -->", "hello" + " shahriar")  # Output: hello shahriar


# ----------------------------
# Exponentiation Operator (**)
# ----------------------------
# 2 to the power of 1000
print("2 raised to the power 1000:", 2 ** 1000)


# ----------------------------
# Boolean in Python
# ----------------------------
print("Is a > 5 ?", a > 5)      # Output: True (since a = 5.50)
print("Is 3 < 4 ?", 3 < 4)      # Output: True

#** → পাওয়ার (exponentiation) এর জন্য ব্যবহৃত হয়।

#int() → দশমিক কেটে পূর্ণসংখ্যায় রূপান্তর করে।

#float() → পূর্ণসংখ্যাকে ভগ্নাংশে রূপ দেয়।

#+ অপারেটর সংখ্যার জন্য যোগ এবং স্ট্রিংয়ের জন্য যুক্ত করে (Operator Overloading).

#True/False → লজিক্যাল বা বুলিয়ান মান।

