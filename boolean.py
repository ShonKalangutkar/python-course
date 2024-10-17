#Booleans represent one of two values: True or False
#In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer

print(10 > 9)
print(10 == 9)
print(10 < 9)

#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(5))

#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))