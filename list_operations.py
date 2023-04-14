# list operations
# lists are ordered. changeable and allowing duplicate values
thislist = [-1,"a",2,"like"]


# some basic operations

# negative indexing
thislist = [-1,"a",2,"like"]
thislist[-1]

# check existence
thislist = [-1,"a",2,"like"]
'a' in thislist 

# insert(index, object) 
thislist = [-1,"a",2,"like"]
thislist.insert(2, 'yes') 
thislist

# append value to a list
thislist = [-1,"a",2,"like"]
thislist.append("orange")
thislist

# extend list
thislist = [-1,"a",2,"like"]
thislist.extend(["a","b"])
thislist
# actually you can add any iterables into extend()
thislist = [-1,"a",2,"like"]
thislist.extend(('a','b'))
thislist



# operations
#1. remove items
thislist = [-1,"a",2,"like"]
thislist.remove(2)
thislist

#2. remove by index
thislist = [-1,"a",2,"like"]
thislist.pop(2)
thislist

thislist.pop() # this op removes the last one

#3. use del keyword to remove items:
thislist = [-1,"a",2,"like"]
del thislist[0]
thislist# just remove the value of index 0

thislist = [-1,"a",2,"like"]
del thislist#remove the whole list
thislist #thislist is not found



# looping a list

#1. loop through a list
thislist = [-1,"a",2,"like"]
for x in thislist:
  print(x)

#2. loop through index
thislist = [-1,"a",2,"like"]
for x in range(len(thislist)):
  print(thislist[x])
  
#3. loop through while
i=0
while i<len(thislist):
  print(thislist[i])
  i+=1

#4. loop through list comprehension 
thislist = [-1,"a",2,"like"]

[print(x) for x in thislist]
# list comprehension format: [expression for item in iterable if condition==True]
[3+item for item in [3,2,1] if 2==2]

#5. sort a list
thislist = [-1,"a",2,"like"]
thislist.sort(reverse=True, key=str) #desc, to be noticed that if you want to order it desc or asc, the elements in the list should be numeric, like this one raised an error. Or you can add key='str'

#6. copy a list
thislist = [-1,"a",2,"like"]
#if do this, list2 will only be a reference for thislist, changes made in list2 will automaticaly be made in thislist
list2=thislist
# make a copy
list2=thislist.copy()
# or
#list2=list('a','b','c')# this one seems not work

#7. join list
#method 1, use "+"
thislist = [-1,"a",2,"like"]
thislist2 = [0,1,5,6]

a=thislist+thislist2
print(a)
#method 2, use append, append one value per time
thislist = [-1,"a",2,"like"]
thislist2 = [0,1,5,6]

a=[]
for x in thislist2:
  a=thislist.append(x)
  
#method3, use extend(), direcly join the whole list, no need for loop
thislist.extend(thislist2)


# list methods(con't), more

#add an element at the end of the list
thislist = [-1,"a",2,"like"]
thislist.append(1)
thislist

#clear all the elements from the list
thislist = [-1,"a",2,"like"]
thislist.clear()
thislist

#copy, returns a copy of a list
thislist.copy()

#count the # of times that value appears in the list, count(value)
thislist = [-1,"a",2,"like"]
thislist.count(-1)

#extend the list with adding an iterable, extend(iterable)
thislist = [-1,"a",2,"like"]
thislist.extend((1,2,'a'))
thislist

#index(elmnt), returns the position at the first occurrence of the specified value
thislist = [-1,"a",2,"like"]
thislist.index(2)

#insert(pos, elmnt), insert an elmnt at pos
thislist = [-1,"a",2,"like"]
thislist.insert(2,3)
thislist

# pops out an element at pos
thislist = [-1,"a",2,"like"]
thislist.pop(2)
thislist

# remove the first occurrence of the element with the specified value
thislist = [-1,"a",2,"like"]
thislist.remove(2)
thislist

# reverse the order of the list
thislist = [-1,"a",2,"like"]
thislist.reverse()
thislist

# sort the list, sort(key, reverse), reverse=True for desc
thislist = [-1,"a",2,"like"]
thislist.sort(key=str, reverse=True)
thislist
