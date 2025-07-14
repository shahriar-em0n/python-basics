# পাইথন স্ট্রিং ও লিস্ট সংক্রান্ত নোটস (Tea Project)

এই প্রজেক্টে আমরা স্ট্রিং, স্লাইসিং, ফাংশন, ফরম্যাটিং এবং লিস্টের বিভিন্ন ফিচার ব্যবহার করেছি।

---

## 🧠 স্ট্রিং প্রিন্ট এবং স্টোর

```python
name = "Shahriar"
print(name)
```

➡️ একটি স্ট্রিং ভেরিয়েবলে রেখে প্রিন্ট করা হয়।

---

## 🍵 স্ট্রিং থেকে অক্ষর ও স্লাইস

```python
tea = "Masala tea"
first_tea = tea[0]
slice_tea = tea[0:6]
```

➡️ `tea[0]` দিয়ে প্রথম অক্ষর বের করা হয়েছে।  
➡️ `tea[0:6]` দিয়ে ০ থেকে ৫ পর্যন্ত অক্ষর গুলো বের করা হয়েছে (৬ বাদ)।

---

## 🔢 স্ট্রিং স্লাইসিং অনুশীলন

```python
num_list = "0123456789"
slice_num = num_list[1:5]
slice_num_two = num_list[0:]
slice_num_three = num_list[:5]
slice_num_four = num_list[0:7:2]
slice_num_six = num_list[-0:7]
slice_num_seven = num_list[-0:-7]
```

➡️ `[:]` দিয়ে পুরো স্ট্রিং বা এর অংশ নেওয়া যায়।  
➡️ `num_list[0:7:2]` প্রতি দুই ঘর পর পর অক্ষর নেয়।  
➡️ `-0` আসলে `0`-এর সমান।

---

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
➡️ `len()` দিয়ে স্ট্রিং বা লিস্টের দৈর্ঘ্য মাপা যায়।

---

## 🔐 ব্যাকস্ল্যাশ `\` ও কোটেশন মার্ক

```python
say = "He said , \"White tea is awesome\""
```

➡️ `\"` দিয়ে কোটেশনের ভেতরে কোটেশন লেখা যায়।

---