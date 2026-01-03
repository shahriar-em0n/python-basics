# Python String Mastery 

> **Topic:** Python String Mastery  
> **Based on your practice code** (indexing, slicing, formatting, methods, unicode, raw strings, immutability, etc.)

---

## Table of Contents
1. [What is a String?](#what-is-a-string)
2. [Quotes: single, double, triple](#quotes-single-double-triple)
3. [Escape sequences and backslashes](#escape-sequences-and-backslashes)
4. [Indexing: positive and negative](#indexing-positive-and-negative)
5. [Slicing: start:end:step](#slicing-startendstep)
6. [Concatenation and repetition](#concatenation-and-repetition)
7. [Type conversion + f-strings](#type-conversion--f-strings)
8. [Length (`len`) and Unicode gotchas](#length-len-and-unicode-gotchas)
9. [String comparisons + ASCII/Unicode order](#string-comparisons--asciiunicode-order)
10. [`ord()` and `chr()`](#ord-and-chr)
11. [Common string methods](#common-string-methods)
12. [`split()` and `join()`](#split-and-join)
13. [Formatting styles: f-string, `.format()`, `%`](#formatting-styles-f-string-format-)
14. [Strings are immutable](#strings-are-immutable)
15. [Raw strings (`r"..."`)](#raw-strings-r)
16. [Method chaining (your shortcut examples)](#method-chaining-your-shortcut-examples)
17. [Best practices (real-world)](#best-practices-real-world)
18. [Mini exercises](#mini-exercises)

---

## What is a String?

A **string** is a **sequence of characters** enclosed in quotes.

```python
str1 = "Shahriar"
print(str1)
```

In Python, strings are **immutable** (you can’t modify a character in-place), but you can create new strings from them.

---

## Quotes: single, double, triple

### Single vs Double quotes
Both create the same type: `str`.

```python
name1 = "python"
name2 = 'python'
print(name1 == name2)  # True
```

Use whichever improves readability.

### Triple quotes (multiline)
Triple quotes are perfect for **multiline text**:

```python
poem = '''Line 1
Line 2
Line 3'''
print(poem)
```

✅ Great for notes, docstrings, long messages.

---

## Escape sequences and backslashes

Backslash `\` is used for **escape sequences**, like `\n` (new line), `\t` (tab), or escaping quotes.

### Escaping quotes
``` python
message = "Don't worry about errors."   # no escaping needed (single quote inside double quotes)
print(message)

message = 'Don\'t worry about errors.'  # escape single quote inside single quotes
print(message)

message = "She said, \"python is amazing!\""
print(message)

```

### Windows path problem
Windows paths contain backslashes, so you either:
1) escape each backslash: `\\`
2) use raw strings: `r"..."`

```python
path = "C:\\User\\Vipul\\Documents"
print(path)
```

---

## Indexing: positive and negative

Given:
```python
s = "Shahriar"
```
Index positions look like:

| Character | S | h | a | h | r | i | a | r |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Negative index | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |

> Note: Python uses **-1 for the last character**. There is no real “-0 index” in practice (because `-0 == 0`).

Access characters:

```python
print(s[0], s[1], s[2])
print(s[-1])  # last char
```

✅ Use negative indices when you want items from the end.

---

## Slicing: start:end:step

**Rule:**
- `start` is **inclusive**
- `end` is **exclusive**
- `step` is jump size

```python
text = "Python"
print(text[0:4])   # 'Pyth'
print(text[:4])    # same
print(text[2:])    # 'thon'
```

### Big example from your code
```python
language = "Python programming"
print(language[:7])     # 'Python '
print(language[7:])     # 'programming'
print(language[7:10])   # 'pro'
print(language[-11:-8]) # also 'pro'
```

### Step slicing
```python
print(language[0:6:2])  # 'Pto'
```

### Reverse string
```python
print(language[::-1])
```

---

## Concatenation and repetition

### Concatenation with `+`
```python
a = "1"
b = "2"
print(a + b)  # '12'
```

⚠️ Remember: `"1" + "2"` becomes `"12"` (string), not number addition.

### Repetition with `*`
```python
star = "*"
print(star * 5)      # '*****'
print((star * 5 + "\n") * 5)  # 5 lines of stars
```

Edge case:
```python
a = "python"
print(a * 0)  # ''
```

---

## Type conversion + f-strings

If you want to join strings with numbers, convert numbers to strings (or use f-strings).

```python
age = 20
message = "My age is " + str(age)
print(message)
```

### f-string (recommended)
```python
city = "Chittagong"
temp = 13
print(f"The Temp in {city} is {temp} degrees")
```

### Print literal `{}` in f-string
```python
print(f"This is a curly brace: {{}}")
```

---

## Length (`len`) and Unicode gotchas

```python
a = "zython"
print(len(a))  # 6
print(len("Hello\nworld"))  # newline counts as 1 character
```

### Emoji length surprise
Your example:
```python
print("heart len is ", len("❤️"))
print("\u2764")
print("\uFE0F")
print("\u2764\uFE0F")
```

Why is it surprising?
- `"❤️"` is often **two Unicode code points**:
  - `\u2764` (heavy black heart)
  - `\uFE0F` (variation selector-16, forces emoji style)
So `len("❤️")` is usually `2`.

✅ This is normal in Unicode handling. Some “visible characters” can be composed of multiple code points.

---

## String comparisons + ASCII/Unicode order

Python compares strings **lexicographically** (character by character) using Unicode code points.

```python
print("apple" == "Apple")  # False
print("a" < "b")           # True
print("apple" < "banana")  # True
print("apple" < "Banana")  # usually False (uppercase letters come earlier)
```

✅ If you want case-insensitive compare:
```python
print("apple".lower() == "Apple".lower())
```

---

## `ord()` and `chr()`

- `ord(char)` → integer code point
- `chr(int)` → character

```python
print(ord('p'))     # e.g. 112
print(ord('a'))     # e.g. 97
print(chr(97))      # 'a'
```

---

## Common string methods

Using:
```python
language = "Python programming"
```

### Case methods
```python
print(language.upper())
print(language.lower())
print("hello world".title())      # Each word capitalized
print("hello world".capitalize()) # Only first letter of whole string
```

### Strip whitespace
```python
space = "       starting space          "
print(space.strip())   # both sides
print(space.lstrip())  # left
print(space.rstrip())  # right
```

### Find / count
```python
find_string = "Hello Shahriar, Who are you Shahriar"
print(find_string.find("Who", 6))      # search from index 6
print(find_string.count("Shahriar"))   # count occurrences
```

**Important behavior:**  
- `find()` returns `-1` if not found.
- Use `in` if you only need True/False.

```python
email = "shahriar12@gmail.com"
print("@" in email)     # True
```

### Replace
```python
banana = "banana banana banana"
print(banana.replace("banana", "Apple"))
```

⚠️ `replace` returns a **new** string (doesn’t modify original).

### Character type checks
```python
print("Python".isalpha())   # True
print("Python3".isalpha())  # False
print("2222".isdigit())     # True
print("2222".isalnum())     # True
print("  \n\t   ".isspace())# True
```

### startswith / endswith
```python
text5 = "Python is amazing"
print(text5.startswith("Python")) # True
print(text5.endswith("amazing"))  # True
print(text5.endswith("is", 0, 9)) # True (checks 'Python is')
```

---

## `split()` and `join()`

### split
```python
text6 = "apple, banana, orange, grape"
print(text6.split(","))  # returns list
```

### join
`join()` is the **best** way to combine many pieces.

```python
li = ['apple', ' banana', ' orange', ' grape']
print(",".join(li))
```

✅ Best practice: Prefer `join()` over repeated `+` in loops.

---

## Formatting styles: f-string, `.format()`, `%`

### 1) f-string (recommended, Python 3.6+)
```python
name = "Shahriar"
age = 20
print(f"My name is {name} and I am {age} years old")
```

### 2) `.format()`
```python
name = "Shahriar"
print("Hello, My name is {} and my age is {}".format(name, 20))
print("Hello, My name is {0} and my age is {1} - {0}".format(name, 20))
print("Hello, My name is {p1} and my age is {p2}".format(p1=name, p2=20))
```

### 3) Old `%` formatting (legacy)
```python
name = "Alice"
print("Hello, %s!" % name)

pi = 3.14159
print("Pi rounded to 2 decimal place : %.2f" % pi)
```

✅ Today, prefer **f-strings** unless you’re maintaining old code.

---

## Strings are immutable

Your immutability demo is perfect:

```python
s = "Hello"
print(id(s), s)

s = "M" + s[1:]
print(id(s), s)
```

`id(s)` changes because Python created a **new** string object.

---

## Raw strings (`r"..."`)

Raw strings treat backslashes as literal characters (mostly).

```python
rs = r"He\nllo"
print(rs)  # prints: He\nllo (not a newline)
```

### Windows paths
```python
file_path = r"C:\User\shahriar\Documents"
print(file_path)
```

### Raw string rules you mentioned (important)
- A raw string **cannot end with a single backslash** because it escapes the quote.
- Ending with `\\` is OK.

---

## Method chaining (your shortcut examples)

You did this nicely:

```python
text = "    python programming SKILL        "
clean = text.strip().title().replace("Skill", "Experties")
print(clean)
```

Chaining is clean, but don’t over-chain if it becomes hard to read.
When complex, break into steps with meaningful variable names.

---

## Best practices (real-world)

- ✅ Prefer **f-strings** for formatting.
- ✅ Prefer **`"sep".join(list_of_strings)`** for joining lots of strings (especially in loops).
- ✅ For file paths, prefer **`pathlib.Path`** over manual `\\` (cross-platform).
- ✅ Use `"substring" in text` for existence checks (clearer than `find() != -1`).
- ✅ Avoid naming variables `slice` because it shadows Python’s built-in `slice` type.

Example improvement:
```python
text = "Python"
part = text[:4]   # instead of slice = text[0:4]
```

---

## Mini exercises

1) **Extract** `"program"` from `"Python programming"` using slicing.  
2) Reverse `"Bangladesh"` using slicing.  
3) Given: `email = "abc@gmail.com"`  
   - Check if it contains `"@"` using `in`.  
4) Convert: `age = 22` → `"I am 22 years old"` using f-string.  
5) Given: `words = ["I", "love", "Python"]`  
   - Build `"I love Python"` using `join`.

---

### ✅ Quick cheat sheet
```python
s[i]           # indexing
s[a:b]         # slicing
s[a:b:c]       # slicing with step
s[::-1]        # reverse
len(s)         # length
s.upper()      # uppercase
s.strip()      # trim spaces
s.find("x")    # index or -1
s.replace("a","b")  # new string
s.split(",")   # list
",".join(list) # string
f"{x}"         # f-string formatting
```
