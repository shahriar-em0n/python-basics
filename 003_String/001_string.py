# String is a sequence of characters within quotes

str1 = "Shahriar"

''' 
String:  s   h   a   h   r   i   a   r
Index:  [0] [1] [2] [3] [4] [5] [6] [7]  <--position of index
Neg idx:-7  -6  -5  -4  -3  -2  -1  -0  
'''

print(str1)

print(str1[0], str1[1], str1[2], str1[3], str1[4], str1[5], str1[6], str1[7])

print(str1[0], str1[1], str1[2], str1[3], str1[4], str1[5], str1[6], str1[7])


name1 = "python"
name2 = 'python'

print(name1 == name2)

message = "Don't worry about errors."
print(message)

message = 'Don\'t worry about errors.'  #  don\'t "\" scape
print(message)

message = "She said, \"python is amazing!\"" 
print(message)


poem = '''A Necessary Autumn Inside Each
~Rumi~

You and I have spoken all these words,
but as for the way we have to go,
words are no preparation.
There is no getting ready, other than grace....
Inside each of us, there’s continual autumn.
Our leaves fall and are blown out over the water.
A crow sits in the blackened limbs
and talks about what’s gone....
There’s a necessary dying,
and then Jesus is breathing again.
Very little grows on jagged rock.
Be ground. Be crumbled, so wildflowers
will come up where you are.
You’ve been stony for too many years.
Try something different.
Surrender.'''

print(poem)

# in python \ means scape 
# when we print \ this than give \\ double backslash


path = "C:\\User\\Vipul\\Documents"
print(path)


# string concatenation

a = "1"
b = "2"
print(a + b)

c, d = "1", "3"
print(c + d)

a1 = a + b
b2 = c + d
print(a1 + b2)

first_name = "Mohammad"  
last_name = "Shahriar"
print(first_name + last_name) # without space

first_name = "Mohammad"  
last_name = "Shahriar"
print(first_name +" "+ last_name) # with space


# type convertion

age = 20
message = "My age is " + str(age)
print(message)

city = "Chittagong"
temp = 13
weather_report = "The temp in" + " "+ city + " is " + str(temp) + " " + "Degrees"
print(weather_report)


new_report = f"The Temp in {city} is {temp} degrees"

print(new_report)

a , b = 5, 10
print(f"the sum of {a} and {b} is {a + b}")

# This is a curly brace: {} -- print thsi
print(f"This is a curly brace: {{}}")

star = "*"
print((star * 5 + "\n") * 5)

 
a = "python" 
print(a * 0)
print(a)
# print(a * -1)

# print pypythonthon
print("py" * 2 + "thon" * 2)


#len
a = "zython"
print(len(a))

print(len("Hello\nworld"))

print("heart len is ",len("❤️"))
print("\u2764")
print("\uFE0F")

print("\u2764\uFE0F")


# string conditon check

msg = "Help!"
print(len(msg) >= 5)

print("apple" == "apple")
print("apple" == "Apple")
print("apple" == "orange")
print("apple" != "orange")
print("a" < "b")
print("apple" < "banana")
print("apple" < "Banana")
print("apple" > "Apple")
print("apple" < "ape")

# print ascii

print(ord('p'))
print(ord('a'))

print(chr(97))


# String Indexing and slicing
# string[start:end]
# start - inclusive
# end - exclusive

text = "Python"
slice = text[0:4]
 
# print(text[0:3])
print(slice)

language = "Python programming"

# String :  P   y   t   h   o   n  ␠    p   r   o  g  r  a  m  m  i  n  g
# Index  :  0   1   2   3   4   5   6   7   8   9  10 11 12 13 14 15 16 17
# Neg    : -18 -17 -16 -15 -14 -13 -12 -11 -10 -9  -8 -7 -6 -5 -4 -3 -2 -1



Slice1 = language[0:7]
print("First slicing", Slice1)

Slice1 = language[:7]
print("First slicing", Slice1)

Slice2 = language[7:18]
print("Sec slicing - ",Slice2)

Slice2 = language[7:]
print("Sec slicing - ",Slice2)

# pro index

pro = language[7:10]
print(pro)

#neg indx pro
neg_pro = language[-11:-8]
print("neg pro - ",neg_pro)

#thon
thon = language[2:6]
print("Pos thon - ",thon)

neg_thon = language[-16:-11]
print("neg thon -", neg_thon)

program = language[7:15]
print("pos - ", program)

neg_program = language[-11:-3]
print("neg pro - ",neg_program)

# string[start:end : step]
 
ex1 = language[0:6:2]
print("ex1 - ", ex1)

neg_ex1 = language[-18:-12:2]
print("Neg - ",neg_ex1)

neg_ex2 = language[:-12:2]
print("Neg - ",neg_ex2)


# reverse string

reverse = language[::-1]
print(reverse)


#Sstring method
up = language.upper()
print(up) 

low = language.lower()
print(low)

txt = "Hello Shahriar How are you"
cap = txt.title()
print(cap)

txt2 = "shahriar you are joss"
capita = txt2.capitalize()
print(capita) 

space = "       starting space          "
print(space)
print(space.strip())
print(space.lstrip())
print(space.rstrip())

# find any string

find_string = "Hello Shahriar, Who are you Shahriar"
print(txt.find("Shahriar")) 
print(find_string.find("Who", 6))

print(find_string.count("Shahriar")) 

email = "shahriar12gmail.com"
print(email.find("@"))

email = "shahriar12@gmail.com"
print(email.find("@"))

replace = text.replace("Python" ,"world")
print(replace)

banana = "banana banana banana"
print(banana.replace("banana", "Apple"))