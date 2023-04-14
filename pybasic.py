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
