# DBTITLE 1, py iterations

#1. if elif else
#if...else
#if...elif...else

#shorthand, this technique is known as ternary operators or conditional expressions
a=1
b=2
c=3
print(a) if a>b else print(c)

print(a) if a>b else print(c) if a==b else print(a+b)

#if statements cannot be empty, but if you for some reason have an if without content, put in the pass statement 
if b>a:
  pass




#2. while loops

#while loop
i=1
while i<4:
  print(i)
  i+=1
#while with a break
i=1
while i<4:
  if i==3:
    break#break the loop
  i+=1
#while with continue, the function of continue is to jump to the next iteration, do not execute following codes
i=0
while i<6:
  i+=1
  if i==3:
    continue
  print(i)

#3. for loops
# for an iterable
fruits = ('banana','orange')
for x in fruits:
  print(x)
  
# for a string
for x in 'bababa':
  print(x)
# for+break
for x in 'bababa':
  if x=='a':
    break
  print(x)
# for+continue
for x in 'bababa':
  if x=='b':
    continue
  print(x)
  
#DBTITLE 1,
# the definition of iterators in python
#an iterator is an object that contains a countable number of values, we can go through all the values
#technically, an iterator implements the iterator protocal, consists of the methods like __iter__(), __next__()

#diff iterator v.s. iterable
#like list, tuple, dict, they are iterables, or iterable containers which you can get an iterator from 
#example to get iterator
mytuple=(1,'a','c',2)
myit = iter(mytuple)
myit#<tuple_iterator at 0x7fe03f990370>
next(myit)
next(myit)
next(myit)

#string also is an iterable, particularly
mystr='banana'
it_str = iter(mystr)
next(it_str)

for x in mystr:
  print(x)
  
  
  
  
 #how to create an object/class an an iterator
# you can create an iter by __init__(), but only always return the iterator object itself

#create a iterator starting from 1 and each step increase by one
class my_iter:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x= self.a
    self.a+=1
    return x

myfunc = my_iter()
iter1 = iter(my_iter())
next(iter1)
next(iter1)
next(iter1)
next(iter1)

#to prevent running it forever, you an add StopIteratio nstatement in your __next__() method:
class my_iter:
  def __iter__(self):
    self.a=1
    return self
  def __next__(self):
    x=self.a
    if x<=20:
      self.a+=1
      return x
myfunc = my_iter()
it2 = iter(myfunc)
next(it2)
next(it2)
next(it2)
next(it2)



