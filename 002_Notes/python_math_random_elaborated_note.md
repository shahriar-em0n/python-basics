# 🐍 Python সংখ্যাগত ফিচার ও মডিউল ব্যবহার: বাংলায় বিস্তারিত ব্যাখ্যা সহ

এই ডকুমেন্টটিতে আমরা Python-এর বিভিন্ন সংখ্যাগত ফিচার যেমন: গাণিতিক অপারেশন, float ↔ int কনভার্সন, math ও random মডিউল, set, fraction, এবং decimal নিয়ে বিস্তারিত আলোচনা করেছি। প্রতিটি ফাংশন এবং প্যাকেজের উদ্দেশ্য ও কাজ ব্যাখ্যা করা হয়েছে।

---

## 📌 Python-এর বিল্ট-ইন গাণিতিক অপারেশন

```python
x = 2
y = 3
z = 4

ans = (x + y) * z
print(ans)  # Output: 20

ans2 = x + (y * z)
print(ans2)  # Output: 14
```

✅ এখানে আমরা Python এর arithmetic operators (+, *, ()) ব্যবহার করছি। `()` ব্র্যাকেট দিয়ে আমরা operation এর অগ্রাধিকার (precedence) নির্ধারণ করতে পারি।

---

## 🧮 Exponentiation Operator: `**`

```python
print("my number = ", 2 ** 1000)
```

✅ `**` অপারেটর ব্যবহার করে আমরা কোনো সংখ্যার ঘাত (power) বের করতে পারি।

---

## 🔁 Float → Integer কনভার্সন

```python
print("first int ", int(5.78))
```

✅ `int()` ফাংশন ব্যবহার করে আমরা দশমিক সংখ্যা থেকে পূর্ণ সংখ্যা তৈরি করতে পারি। দশমিক অংশ বাদ পড়ে যায় (round করে না)।

```python
a = 5.50
print(int(50) + a)
```

---

## 🔁 Integer → Float কনভার্সন

```python
print("second float ", float(72.22))
```

✅ `float()` ব্যবহার করে আমরা int সংখ্যাকে ভগ্নাংশ রূপে রূপান্তর করি।

```python
b = 10
print(float(5.50) + b)
```

---

## ➕ Operator Overloading

```python
print("python overloading ---> " + "hello" + "shahriar")
```

✅ Python-এ `+` অপারেটরকে ব্যবহার করা যায় স্ট্রিং জোড়ার জন্যও। এটাকেই বলা হয় Operator Overloading।

---

## ✅ Boolean মান

```python
print(a > 5)    # True
print(3 < 4)    # True
```

✅ Python-এ `>`, `<`, `==` ইত্যাদি ব্যবহার করে লজিক্যাল যাচাই করা যায়।

---

## 📐 `math` Module

```python
import math
```

✅ `math` প্যাকেজটি গাণিতিক calculation এর জন্য ব্যবহৃত হয়। এতে অনেক বিল্ট-ইন ফাংশন আছে যেমন: `floor()`, `trunc()`, `sqrt()`, `log()` ইত্যাদি।

```python
print(math.floor(5.80))     # 5 → নিচের পূর্ণ সংখ্যা
print(math.floor(-5.60))    # -6

print(math.trunc(4.2))      # 4 → দশমিক বাদ
print(math.trunc(-4.2))     # -4
```

---

## 🎲 `random` Module

```python
import random
```

✅ `random` মডিউল ব্যবহার করা হয় র‌্যান্ডম সংখ্যা তৈরি করতে, যা সাধারণত গেম, সিমুলেশন বা ডেটা স্যাম্পলিং-এ ব্যবহৃত হয়।

```python
print(random.random())              # 0.0 - 1.0 এর মধ্যে float
print(random.randint(1, 10))        # 1 - 10 এর মধ্যে int
```

### ✅ `random.choice()`

```python
names = ['shahriar', 'emon', 'akash', 'hasan']
print(random.choice(names))         # list থেকে random item
```

### ✅ `random.shuffle()`

```python
random.shuffle(names)              # মূল list-টি inplace shuffle হয়
print(names)
```

🔴 ভুল যেটা হইছিল:
```python
print(random.choice())  # ❌ Error: sequence দিতে হবে
```

---

## 🔁 `set` ডেটা টাইপ ও অপারেশন

```python
setone = {1, 2, 3, 4}

print(setone & {1, 3})          # Intersection
print(setone | {1, 3})          # Union
print(setone - {1, 2, 3, 4})    # Difference
```

✅ `set` ব্যবহার করে আমরা গণিতের সেট অপারেশন করতে পারি — যেগুলো খুব দ্রুত ও দক্ষতার সাথে কাজ করে।

---

## 🧮 `fractions` Module

```python
from fractions import Fraction
myFra = Fraction(2, 7)
print(myFra)  # Output: 2/7
```

✅ `Fraction()` ফাংশন দিয়ে ভগ্নাংশ (রাশি) তৈরি করা যায় যেটা নির্ভুল গাণিতিক মান ধরে রাখে।

---

## 💰 `decimal` Module

```python
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Output: 0.3
```

✅ `Decimal` float এর তুলনায় আরো নিখুঁত এবং নির্ভুল গাণিতিক হিসাব করতে দেয়। বিশেষ করে ফিন্যান্সিয়াল ডোমেইনে এটা গুরুত্বপূর্ণ।

---

## 🧠 Extra ব্যাখ্যা

### 1. `repr()`:
একটি object এর **official** representation দেয়, যেটা ডেভেলপারদের জন্য।

```python
repr("hello")  # Output: "'hello'"
```

### 2. `str()`:
একটি object এর **user-friendly** রূপে রূপান্তর করে।

```python
str("hello")  # Output: "hello"
```

### 3. `print()`:
Python-এর বিল্ট-ইন ফাংশন, যেটা স্ক্রিনে output দেখায়।

```python
print("hello")  # Output: hello
```

---

## ✅ উপসংহার

এই নোটটি Python-এ গণিত, কনভার্সন, র‌্যান্ডম, সেট অপারেশন, ফ্র্যাকশন, ও দশমিক গণনা সম্পর্কে পরিষ্কার ধারণা দেবে। প্রতিটি ফাংশনের উদ্দেশ্য ও ব্যবহারিক দৃষ্টিভঙ্গি দিয়ে উপস্থাপন করা হয়েছে।

