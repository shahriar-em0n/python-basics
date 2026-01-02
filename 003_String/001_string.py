# String is a sequence of characters within quotes

str1 = "Shahriar"

#  s   h   a   h   r   i   a   r
# [0] [1] [2] [3] [4] [5] c[6] [7]  <--position of index

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