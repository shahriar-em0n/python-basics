txt = "Python programming"

# P  y  t  h  o  n     p  r  o  g  r  a  m  m  i  n  g
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17

print(txt[17])
print(txt[7:18])
print(txt[7:10])
print(txt[-11:-8])
print(txt[:6:2])
print(txt[::-2])
print(txt[::-1])

## string methods

print(txt.upper())
print(txt.lower())
print(txt.split())

text = "hello shahriar kemon acho"
print(text.capitalize())
print(text.title())

text1 = "        hello my name is shahriar          "
print(text1)
print(text1.strip())
print(text1.lstrip())
print(text1.rstrip())

print(text.find("shahriar"))

text2 = "Hello my name is shahriar"

print(text2.replace("shahriar", "Kuddus"))

tt = "Hello"
print(tt.isalpha())
tt2 = "551"
print(tt2.isdigit())

t2 = "python is amazin, python is fun"
print(t2.find("is"))
print(t2.count("is"))
print(t2.index("is"))

email = "Shahriar@12gmai.com"
print(email.lower())
print(email.lower().find("@"))

test = "apple, banana, orange, grape"
print(test.split(","))


# format method

name = "Shahriar"
message = "Hello, My name is {} and my age is {}".format(name, 20)
print(message)

message2 = "Hello, Guys i am %s and I am %d year old" %(name, 20)
print(message2.capitalize())  

s = "hello"
print(id(s))

ques = "       python programming SKILLS    "
# final = ques.replace("SKILLS", "Expert").title().split()
# print(final) 
print(ques.strip().title().replace("Skills", "Expert"))

s1 = "Python programming lanuage"
print(s1[0::2])
print(s1[1::2])

print("Rvers : ",s1[::-1])

print(s1[-19:-8])

print(s1[0]+s1[7]+s1[19])

tes = "mississippi"
print("i",tes.count("i"))
print("s",tes.count("s"))
print("p",tes.count("p"))
print("m",tes.count("m"))