#In python we dont need to declare variables type we can just declare them
x = 5  #this variable is INT type 
y = "shon" #this variable is STR type
print(x)
print(y)


#We can also specify the data by using casting
x = str(5)    # like x will be '5'
y = int(5)    # and y will be 5
z = float(5)  # and z will be 5.0
print(x,y,z)

#we can get the data type of a variable with the type() function.
x = 5
y = "shon"
print(type(x))  #<class 'int'>
print(type(y))  #<class 'str'>

#Variable names are case-sensitive.
AGE = 5 #this would be  different from 
age = 26 #from this
print(AGE, age)

#we cannot start a variable name with a Nummbers, hyphens and spaces are not allowed in between
My_name = "shon"
MyName = "shon"
My_Name = "shon"
My_name2 = "shon"
#these are allowed  
# 2myname = "shon"
# 2-myname = "shon"
# my name = "shon"
# these are not allowed

#we can assign the same value to multiple variables

A = B = C = "Yellow"
print(A)
print(B)
print(C)

# If we have a collection of values in a list tuple Python allows you to extract the values into variables this is called unpacking.
fruits = ["apple", "banana", "cherry"]
U, H, I = fruits
print(U)
print(H)
print(I)

# # Global Variables
# these are the Variables that are created outside of a function
# Global variables can be used by everyone, both inside of functions and outside
O = "Variable"

def myfunc():
  print("This is Global " + O)

myfunc()

# If we create a variable with the same name inside a function this variable will be local and can only be used inside the function The global variable with the same name will remain as it was global and with the original value.

R = "Global"

def myfunc():
  R = "Local"
  print("this variable is " + R)

myfunc()

print("this variable is " + R)

# To create a global variable inside a function, you can use the global keyword.
# Also, use the global keyword if you want to change a global variable inside a function.