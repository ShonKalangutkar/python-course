#Strings in python are surrounded by either single quotation marks, or double quotation marks.
##Assigning a string to a variable is done with the variable name followed by an equal sign and the string
a = "shon"
print(a)

#You can assign a multiline string to a variable by using three quotes
# a = """Lorem, ipsum dolor sit amet consectetur adipisicing elit. Delectus doloribus rerum facere maiores officia corrupti laborum sapiente eveniet perferendis maxime!"""
# print(a)

# #Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string

a = "Hello, World!"
print(a[1])

#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))


#To check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
txt = "The best things in life are free!"
print("expensive" not in txt)

#we can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])

#By leaving out the start index, the range will start at the first character
b = "Hello, World!"
print(b[:5])

#Same for the end
b = "Hello, World!"
print(b[3:])

#Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])

#Python has a set of built-in methods that you can use on strings
#for uppercase
a = "Hello, World!"
print(a.upper())

#For lowercase
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())

#The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))  

#The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(","))

#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is Shon, I am {age}"
print(txt)

#Placeholders and modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value
price = 59
txt = f"The price is {price} dollars"
print(txt)  

# placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#A placeholder can contain Python code, like math operations
txt = f"The price is {20 * 59} dollars"
print(txt)