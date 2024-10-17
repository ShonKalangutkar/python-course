# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

#we can get the data type of any object by using the type() function:
x = 5
print(type(x)) #<class 'int'>
x = "Hello World"
print(type(x)) #<class 'str'>
x = 20.5
print(type(x)) #<class 'float'>
x = 1j
print(type(x)) # <class 'complex'>
x = ["apple", "banana", "cherry"]
print(type(x)) #<class 'list'>
x = ("apple", "banana", "cherry")
print(type(x)) #<class 'tuple'>
x = range(6)
print(type(x)) #<class 'range'>
x = {"name" : "John", "age" : 36}
print(type(x)) #<class 'dict'>
x = {"apple", "banana", "cherry"}
print(type(x))#<class 'set'>
x = frozenset({"apple", "banana", "cherry"})    
print(type(x)) #<class 'frozenset'>
x = True
print(type(x)) #<class 'bool'>
x = b"Hello"
print(type(x)) #<class 'bytes'>
x = bytearray(5)
print(type(x)) ##<class 'bytearray'>
x = memoryview(bytes(5))
print(type(x)) # <class 'memoryview'>
x = None
print(type(x)) #<class 'NoneType'>