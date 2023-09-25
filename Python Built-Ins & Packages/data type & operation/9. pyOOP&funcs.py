#DBTITLE 1, Create a function
#use def, you can have arguments, a is the argument in fun1()
def fun1(a):
  return a+1+1
#call this func
fun1(2)


#difference between argument and parameter: they could be same thing: the info passed into a func, but from the function perspective, a param is a variable inside the parentheses in the function whereas arguments are the value sent to the function when it's called

#if you do not know how many arguments that will be passed you can add a * before the parameter name
def my_family(*kids):
  print("kids in my family are",kids[:])
my_family('a','b','c')


#lambda func
#syntax: lambda arguments: expression
#lambda a,b,c: (a+b)/2-c

#why use? :use as an anonymous function inside another function
#like if you want to use a formala like (a+b)/2-c
def myfunc(c):
  return lambda a,b: (a+b)/2-c
myab = myfunc(3)
myab(10,2)

#DBTITLE 1, py OOP
#everything in Python is an object, with its properties and methods
#a class is like an object constructor, or a 'blueprint' for creating objects
#create a class:
class Myobject:
  x
#create a object
pl=Myobject()

#_init_() function:
# all the classes have a function called _init_() which is always executed when the class is being initiated
# we can use _init_() function to assign values to object properties or other operations that are necessary to do when the object is being created
class person:
  def __init__(self,name, age):
    self.name=name
    self.age=age

p1=person('john','30')
p1.name

# __str__() can control what should be returned when the class object is represented as a string, if the __str__() is not set, the string representation of the object is returned

#__str__() not set
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

#string representation with __str__() func
#string representation with __str__() func
class Person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name} is {self.age}"

p2=Person('john',31)
print(p2)

#objects also contain methods, methods in objects are functions that belong to the object
#for example, create a function inside the object
class person:
  def __init__(self,name):
    self.name=name
  def Nameout(self):
    print('his name is',self.name)

p1=person('john')
p1.Nameout()

#what is self parameter? that is a reference to the current instance of the class, used to access variables that belong to the class, it does not have to be named as 'self', but it has to be the first parameter of any function in the class
class person:
  def __init__(a,name):
    a.name=name
  def Nameout(a):
    print('his name is',a.name)

p1=person('john')
p1.Nameout()

#modify object properties
#you can set the name to another like
p1.name = 'alice'
p1.Nameout()#see, its alice now

#delete the property
del p1.name
#p1.Nameout()#it arises an error because you just deleted the name 
del p1#delete the object
#p1#now it arises an error said that p1 is not defined because you just deleted the object

#how to pass statement
#you know, class definitions cannot be empty, but if you for some reason have a class with no content, put in 'pass'
class passagers:
  pass


#DBTITLE 1, py inheritance
#parent class is a class being inherited from other
#child class: is the class that inherits from other class

#creating a parent class is just like creating a class
class person:
  pass
#creating a child class:
class student(person):#student is a person at first, so parent_a is its parent class
  pass
#then use this child class to create an object
std1 = student()#because you do not define arguments in std or parent, you do not need to pass arguments here

# you can add a __init__() in your child class, it would no longer inherit parent's __init__() then, 'override'
class person:
  def __init__(ps, name, age):
    ps.name=name
    ps.age=age
  def nameout(ps):
    print(ps.name,1)
class student(person):
  def __init__(st,name):
    st.name=name

std1= student('john')
std1.nameout()

# you also can call your parent __init__() and use it in the child __init__(), but sure they have same arguments otherwise it will arise exceptions and your 'self parameter' should be the same name
class student(person):
  def __init__(ps,name,age):
    person.__init__(ps,name,age)

std2=student('john',11)

# use __super__() func: inherit all the methods & properties from its parent and reconstruct it in the child function
#the difference is that in your super(), you do not need to include self parameter
class student(person):
  def __init__(ps,name,age):
    super().__init__(name,age)
std3=student('stanley',23)

#in your child function/parent function, you can add a new parameter passing into self
class student(person):
  def __init__(ps,name,age):
    super().__init__(name,age)
    ps.a1 = 2019
    
std3=student('stanley',23)
std3.a1#so if a1 has been initiated like to be 2019, you do need to see it as an variable, but if it's as a variable, you have to define this argument

class student(person):
  def __init__(ps,name,age,a):
    super().__init__(name,age)
    ps.a1 = a
std4=student('pat',2,342)
std4.a1



