# 🐍 পাইথন স্ট্রিং ও লিস্ট ফাংশনের বিস্তারিত বাংলা ব্যাখ্যা

এই অধ্যায়ে আমরা পাইথনের গুরুত্বপূর্ণ কিছু ফাংশন ব্যাখ্যা করব, যেগুলো তুমি ব্যবহার করেছিলে তোমার "tea" প্রজেক্টে। প্রতিটি ফাংশনের কাজ এবং উদাহরণ সহজ ভাষায় বোঝানো হয়েছে।

---

## 1️⃣ `.lower()` ফাংশন

🔹 কাজ: কোনো স্ট্রিং-এর সব অক্ষর ছোট (small/capital -> small) অক্ষরে রূপান্তর করে।  
🔹 উদাহরণ:

```python
text = "Black Tea"
print(text.lower())  # ফলাফল: black tea
```

✳️ এটা তখনই কাজে লাগে যখন তুমি case-insensitive কম্পারিজন করতে চাও।

---

## 2️⃣ `.upper()` ফাংশন

🔹 কাজ: স্ট্রিং-এর সব অক্ষর বড় অক্ষরে (uppercase) রূপান্তর করে।

```python
text = "green tea"
print(text.upper())  # ফলাফল: GREEN TEA
## 🔤 স্ট্রিং ফাংশনস

```python
tea1 = "black tea"
print(tea1.lower())
print(tea1.upper())
```

➡️ `.lower()` স্ট্রিং ছোট অক্ষরে করে, `.upper()` বড় অক্ষরে।

---

## 🚿 `.strip()` ব্যবহার

```python
tea2 = "     milk tea     "
tea2.strip()
```

➡️ শুরু ও শেষের ফাকা জায়গা মুছে ফেলে।

---

## 🔄 `.replace()` ব্যবহার

```python
tea3 = "green tea"
tea3.replace("green tea", "black tea")
```

➡️ স্ট্রিং-এর নির্দিষ্ট অংশ অন্য কিছু দিয়ে বদলানো।

---

## ✂️ `.split()` ব্যবহার

```python
tea4 = "Pu-erh Tea, Oolong Tea, White Tea, Milk Oolong"
tea4.split(", ")
```

➡️ কমা ও স্পেস দিয়ে স্ট্রিংকে আলাদা করে লিস্ট বানানো হয়।

---

## 🔍 `.find()` ও `.count()` ব্যবহার

```python
tea5 = "rong cha"
tea5.find("cha")

tea6 = "tea tea tea white white white"
tea6.count("tea")
tea6.count("white")
```

➡️ `.find()` একটি শব্দ কোথায় আছে তা বলে।  
➡️ `.count()` কয়বার আছে তা বলে।

---

## 📦 `.format()` এবং ফরম্যাটিং

```python
order = "I orderd {} cups of {} tea"
order.format(quantity, tea_type)
```

➡️ `{}` দিয়ে প্লেসহোল্ডার তৈরি করে পরে `.format()` দিয়ে ভ্যালু বসানো হয়।

---

## 📜 লিস্ট, `.join()` এবং `len()`

```python
tea_variety = ["Lemon", "Masala", "White", "Milk"]
" ".join(tea_variety)
"-".join(tea_variety)
", ".join(tea_variety)
len(tea)
## 🔤 স্ট্রিং ফাংশনস

```python
tea1 = "black tea"
print(tea1.lower())
print(tea1.upper())
```

➡️ `.lower()` স্ট্রিং ছোট অক্ষরে করে, `.upper()` বড় অক্ষরে।

---

## 🚿 `.strip()` ব্যবহার

```python
tea2 = "     milk tea     "
tea2.strip()
```

➡️ শুরু ও শেষের ফাকা জায়গা মুছে ফেলে।

---

## 🔄 `.replace()` ব্যবহার

```python
tea3 = "green tea"
tea3.replace("green tea", "black tea")
```

➡️ স্ট্রিং-এর নির্দিষ্ট অংশ অন্য কিছু দিয়ে বদলানো।

---

## ✂️ `.split()` ব্যবহার

```python
tea4 = "Pu-erh Tea, Oolong Tea, White Tea, Milk Oolong"
tea4.split(", ")
```

➡️ কমা ও স্পেস দিয়ে স্ট্রিংকে আলাদা করে লিস্ট বানানো হয়।

---

## 🔍 `.find()` ও `.count()` ব্যবহার

```python
tea5 = "rong cha"
tea5.find("cha")

tea6 = "tea tea tea white white white"
tea6.count("tea")
tea6.count("white")
```

➡️ `.find()` একটি শব্দ কোথায় আছে তা বলে।  
➡️ `.count()` কয়বার আছে তা বলে।

---

## 📦 `.format()` এবং ফরম্যাটিং

```python
order = "I orderd {} cups of {} tea"
order.format(quantity, tea_type)
```

➡️ `{}` দিয়ে প্লেসহোল্ডার তৈরি করে পরে `.format()` দিয়ে ভ্যালু বসানো হয়।

---

## 📜 লিস্ট, `.join()` এবং `len()`

```python
tea_variety = ["Lemon", "Masala", "White", "Milk"]
" ".join(tea_variety)
"-".join(tea_variety)
", ".join(tea_variety)
len(tea)
```

➡️ `.join()` লিস্টের আইটেমগুলোকে একত্রে স্ট্রিং বানায়।  
➡️ `len()` দিয়ে স্ট্রিং বা লিস্টের দৈর্ঘ্য মাপা যায়।```

➡️ `.join()` লিস্টের আইটেমগুলোকে একত্রে স্ট্রিং বানায়।  
➡️ `len()` দিয়ে স্ট্রিং বা লিস্টের দৈর্ঘ্য মাপা যায়।```

---

## 3️⃣ `.strip()` ফাংশন

🔹 কাজ: স্ট্রিং-এর শুরু ও শেষের ফাঁকা জায়গা (spaces) মুছে ফেলে।

```python
text = "   milk tea   "
print(text.strip())  # ফলাফল: "milk tea"
```

➡️ মাঝের ফাঁকা জায়গা কিন্তু ঠিক থাকবে, শুধু শুরু আর শেষেরটা যাবে।

---

## 4️⃣ `.replace()` ফাংশন

🔹 কাজ: স্ট্রিং-এর নির্দিষ্ট অংশকে অন্য কিছুর সাথে বদলানো।

```python
text = "green tea"
print(text.replace("green", "black"))  # ফলাফল: black tea
```

✳️ এটা কাজে লাগে যখন কোন নির্দিষ্ট শব্দকে অটোমেটিকভাবে বদলাতে হয়।

---

## 5️⃣ `.split()` ফাংশন

🔹 কাজ: স্ট্রিংকে একটা লিস্টে ভেঙে ফেলে, কোনো নির্দিষ্ট সিম্বল বা স্পেসের উপর ভিত্তি করে।

```python
text = "Milk Tea, Green Tea, Black Tea"
print(text.split(", "))  # ফলাফল: ['Milk Tea', 'Green Tea', 'Black Tea']
```

➡️ ডিফল্টভাবে `split()` স্পেস দিয়ে ভাগ করে।

---

## 6️⃣ `.find()` ফাংশন

🔹 কাজ: কোনো স্ট্রিং-এর মধ্যে নির্দিষ্ট একটি শব্দ বা অক্ষর কোথায় আছে তার অবস্থান (index) জানায়।

```python
text = "rong cha"
print(text.find("cha"))  # ফলাফল: 5
```

➡️ যদি না পায়, তাহলে `-1` রিটার্ন করে।

---

## 7️⃣ `.count()` ফাংশন

🔹 কাজ: কতবার একটি নির্দিষ্ট শব্দ বা অক্ষর স্ট্রিং-এ এসেছে তা গোনে।

```python
text = "tea tea tea white white white"
print(text.count("tea"))   # ফলাফল: 3
print(text.count("white")) # ফলাফল: 3
```

---

## 8️⃣ `.format()` ফাংশন

🔹 কাজ: স্ট্রিং-এর মধ্যে `{}` এর জায়গায় ভ্যালু বসায়।

```python
order = "I ordered {} cups of {} tea"
print(order.format(2, "lemon"))  # ফলাফল: I ordered 2 cups of lemon tea
```

➡️ এটা ভ্যারিয়েবল দিয়ে ডাইনামিক টেক্সট বানানোর জন্য খুবই দরকারি।

---

## 9️⃣ `.join()` ফাংশন

🔹 কাজ: লিস্টের সব এলিমেন্টকে একটি স্ট্রিং-এ পরিণত করে, মাঝখানে নির্দিষ্ট সিম্বল বসিয়ে।

```python
flavors = ["Lemon", "Milk", "Masala"]
print(", ".join(flavors))  # ফলাফল: Lemon, Milk, Masala
```

---

## 🔟 `len()` ফাংশন

🔹 কাজ: কোনো স্ট্রিং, লিস্ট বা অন্য iterable ডেটার দৈর্ঘ্য বা কতগুলো আইটেম আছে তা বলে।

```python
text = "Masala tea"
print(len(text))  # ফলাফল: 11
```

---

## 🔚 উপসংহার

এই ফাংশনগুলো তোমাকে স্ট্রিং এবং লিস্ট নিয়ে অনেক কাজ করতে সাহায্য করবে — যেমন ইউজারের ইনপুট প্রসেসিং, রিপোর্ট তৈরি, ডেটা ফরম্যাটিং, এবং আরও অনেক কিছু।

---