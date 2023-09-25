# DBTITLE 1, Python built-in attributes, methods

# python has no command for declaring a var, do not need to declare with an particular type but we can specify data type
x=str(3)
y=int(3)
z=float(3)

# naming methods
# 1. start with a letter or underscore so it cannot start with a number
# 2. only contain alpha-numeric characters and understore, they are case sensitive

# Camel Case
myVariableName
# Pascal Case
MyVariableName
# Snake Case
my_variable_name

# or combinations of any of them

# assign multiple values
# different values
x,y,z = 1,2,3
# same values
x=y=z=1
# unpack from a list or tuple
x,y,z = ("a","b","c")

# output vars
print(x,y,z)

# global/local variable

# global var outside a function, but local variable in functions
# we can create a globle variable inside a function as well
def fun_game():
  global n
  n=3
  return 1

fun_game() 

n+3==6


# built-in data types

# text type: str
# numeric types: int, float, complex
# sequence types: list, tuple, range
# mapping type: dict
# set types: set, frozen set
# boolean type: bool
# binary types: bytes, bytearray, memoryview
# None type: NoneType

#1. to define a complex object:
a = 5+7j # actually your computer automatically recognize it as complex, j is designed particularily for complex number, but you also can use a=complex(5+7j) as well

a.real # real number
a.imag # imagination

#2. to define a frozenset, which is immutable object often used as a key in dict or element of other sets

student = {"name": "stanley", "age":24}
key = frozenset(student) # this object "key" is non-subscriptable and mutable
#key[1]

# 3. binary types
x = b"Hello" # 5 bytes byte type, every byte has a letter
x = bytearray(5) # bytearray(b'\x00\x00\x00\x00\x00'), use bytearray() to assign 5 bytes space to x
x = memoryview(bytearray(5)) # you can know where is x, for example this one is at <memory at 0x7f6d8ea1fe80> 

# 4. string type
a = """  he is good, but i am that better"""
# slicing strings
a[2:5]
a[:5]
a[2:]
a[-5:-2] # -2, exclusively
# modify strings
a.upper() #upper case
a.lower() #lower case
a.strip() # remove the whitespace at the end and begining
a.replace("better", "the best") # replace a with b, "better" with "the best"
# format strings
txt = "my age is {age}"
age =13
txt.format(age=age)

txt = "my age is {1}, and i like {2} and {0}"
age = 13
like1 = "books"
like2 = "traveling"
txt.format(like2,age,like1)


# boolean
bool()




#DBTITLE 1, Range function
#range()#start from 0 and increment by 1
range(2,30,3)#start, end, increment by 3, this is a range object you need to put it in to an iterable, like list
list(range(2,30,3))

#array
#array is a built-in type but restricted to only contain same type elements, some people think array data structtype is not "native" in py, however we can use list method for array
#1. create an array
cars=['ford','volvo','bmw']
type(cars)
#2. asses elements in array
cars[1]
#3. length of an array
len(cars)
#4. looping
for x in cars:
  print(cars)
#5. adding
cars.append("Honda")
#6. removing
cars.pop(2)
cars
#or use remove
cars.remove("ford")
cars

# you can apply any list methods for arrays



#module
# module is the code library, a file containing a set of functions
#to create a module
#just save the code in a file with a file extension .py

#to use a module
import pandas as pd
#to use a function in a module
#pd.function_name()

#modules can contain functions as well as all types of vars
#so you can get access to a dict from a module like
#a=pd.person

#you can rename your module by using 'as'

#list all the funcs in a module
dir(pd)

#import a part of funcs/vars from a module
#import funcs from pandas 


#datetime
#datetime is not a datatype in python but a module named datetime can work with dates objects
import datetime
x=datetime.datetime.now()
x#684042 is the microseconds

#you can use datetime() class
a=datetime.datetime(2020,5,17)

#use strftime() method to format date objects into readable strings, only on erequired param
a.strftime("%B%D")
