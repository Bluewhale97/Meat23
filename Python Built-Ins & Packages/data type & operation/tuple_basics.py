## DBTITLE 1, Tuple intro

# tuple: ordered(have a defined order and the order will not change), unchangeable(cant change, add, or remove  items after it created), and allow duplicate values(since it is indexed, it can have same value), tuple can store any types of data

#tuple length
thistp = (1,2,3,'a','c',{}) # or use tuple()
len(thistp)

# to compare with tuple, lists are changeable, ordered(indexed) and allowing duplicates; sets are not changeable, not ordered and not allowing duplicated
# dictionaries are ordered, changeable but not allowing duplicates; lists are changeable, allowing duplicates and ordered.
# as of py 3.7 and above dicts been ordered. Although sets are not changeable, but actually you can add/remove items as your demands

# access tuple ietm
thistp[1]
thistp[-1]#negative indexing
thistp[2:5]
thistp[4]
thistp[2:]


# check existence
1 in thistp

# access tuple ietm
thistp[1]
thistp[-1]#negative indexing
thistp[2:5]
thistp[4]
thistp[2:]


# check existence
1 in thistp


# Tuple operations

# add items
# tuple is unchangeable, so ye can either convert it or create a new tuple
#1. convert
thistp=()
y=list(thistp)
y.append('orange')
thistp2=tuple(y)
thistp2
#2. create a new tuple
thistp = (1,2,3,'a','c',{})
y=('orange',)# ('orange') is a string
thistp + y

#delete tuple fully
del thistp

# pack/unpack tuples
# to pack it
thistp = (1,'a',2)
#unpack it
(green, *yellow, red) = (1,2,3,'a','b')# if the # of vars is less than # ofvalues, add * then it will add an list to that var
yellow

# loop tuples
#1. for loop
thistp = (1,'a',2)
for i in thistp:
  print(i)

for i in range(len(thistp)):
  print(thistp[i])
  
#2. while loop
i=0
while i in range(len(thistp)):
  print(thistp[i])
  i+=1

# join tuple
# using +
thistp = (1,'a',2)
thistp2 = (1,'a',2)
thistp + thistp2
# using * for multiplication
thistp*2 #return (1, 'a', 2, 1, 'a', 2)

# tuple methods
thistp = (1, 'a', 2, 1, 'a', 2)
thistp.count(1) #count(value), the number of the value in the tuple
thistp.index(1) # index(value), the first occ of the value
