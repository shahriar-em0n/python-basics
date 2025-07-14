# 🐍 Python সংখ্যাগত ফিচার ও মডিউল ব্যবহার: বাংলায় ব্যাখ্যা সহ

এই ডকুমেন্টটিতে আমরা Python-এর বিভিন্ন সংখ্যাগত ফিচার যেমন: গাণিতিক অপারেশন, float ↔ int কনভার্সন, math ও random মডিউল, set, fraction, এবং decimal নিয়ে বিস্তারিত আলোচনা করেছি।

---

## 🔢 গাণিতিক অপারেশন ও Power Operator

```python
x = 2
y = 3
z = 4

ans = (x + y) * z       # প্রথমে যোগ, পরে গুণ
print(ans)              # Output: 20

ans2 = x + (y * z)      # প্রথমে গুণ, পরে যোগ
print(ans2)             # Output: 14

# Power operator (exponentiation)
print("my number = ", 2 ** 1000)  # 2 এর power 1000
```

---

## 🔁 Float কে Integer এ রূপান্তর

```python
print("first int ", int(5.78))  # দশমিক অংশ বাদ দিয়ে পূর্ণসংখ্যা রিটার্ন

a = 5.50
print(int(50) + a)              # int ও float যোগ
```

---

## 🔁 Integer কে Float এ রূপান্তর

```python
print("second float ", float(72.22))  # int → float

b = 10
print(float(5.50) + b)               # float ও int যোগ
```

---

## ➕ Operator Overloading

```python
print("python overloading ---> " + "hello" + "shahriar")
```

**ব্যাখ্যা:** `+` অপারেটর শুধু সংখ্যার জন্য নয়, string কনক্যাট করার জন্যও ব্যবহার হয়।

---

## ✅ Boolean মান

```python
print(a > 5)   # True
print(3 < 4)   # True
```

---

## 📐 math module

```python
import math

# Floor function → নিচের পূর্ণসংখ্যা
print(math.floor(5.80))     # 5
print(math.floor(3.80))     # 3
print(math.floor(-5.60))    # -6

# Trunc function → দশমিক অংশ বাদ দেয়
print(math.trunc(4.2))      # 4
print(math.trunc(-4.2))     # -4
```

---

## 🎲 random module

```python
import random

print(random.random())            # 0.0 - 1.0 এর মধ্যে random float
print(random.randint(1, 10))      # 1 - 10 এর মধ্যে random পূর্ণসংখ্যা

names = ['shahriar', 'emon', 'akash', 'hasan']
print(random.choice(names))       # list থেকে random item

random.shuffle(names)             # list কে shuffle করে
print(names)
```


---

## 🔁 Set Operations

```python
setone = {1, 2, 3, 4}

print(setone & {1, 3})            # common element: {1, 3}
print(setone | {1, 3})            # union: {1, 2, 3, 4}
print(setone | {1, 3, 7})         # union: {1, 2, 3, 4, 7}
print(setone - {1, 2, 3, 4})      # difference: set()
```

---

## 🧮 Fraction Module

```python
from fractions import Fraction

myFra = Fraction(2, 7)
print(myFra)    # Output: 2/7
```

---

## 💰 Decimal Module

```python
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Output: 0.3
```

---

## 🧠 Extra ব্যাখ্যা

### 1. `repr()`:
- একটি object এর **official string representation** দেয় (debugging বা eval করার জন্য)
```python
repr("hello") → "'hello'"
```

### 2. `str()`:
- একটি object এর **readable (user-friendly)** রূপে কনভার্ট করে
```python
str("hello") → "hello"
```

### 3. `print()`:
- output দেখানোর জন্য ব্যবহার হয়
```python
print("hello") → hello
```

---

📚 এই নোটটি Python এর সংখ্যা, লজিক, র‍্যান্ডমনেস ও কাস্টম ডেটা টাইপ নিয়ে একটি beginners guide হিসেবে ব্যবহার করা যেতে পারে।
