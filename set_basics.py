# set intro
# set is unchangeable, inordered, and not allowing to have duplicates 
# to be noticed, True and 1 are considered as the same thing in sets, so it would be treated as duplicates

# set operations

# 1.length of set
thisset = {1,"a"}
len(thisset)

# 2.constructor of sets
# you can either
thisset = {1,'a'}
# or use set() constructor and pass in an iterable
thisset = set((1,"a"))

# 3.we can not access a item in a set by index because it is inordered and not indexed
# a way to access a item in a set:
# for loop
thisset = {1,'a'}
for i in thisset:
  print(i)
  
# 4. add new items
thisset = {1,'a'}
thisset.add(('s',2))# add an element, this element can be a tuple too
thisset.update({1,2,'fsde'})#add several elements from an iterable
thisset

#5. remove items
# either use remove
thisset.remove(1)
# or discard
thisset.discard('a')
# or use pop
thisset = {1,'a'}
thisset.pop()# pop out the last one
thisset

# clear() can clear all the items in the set
thisset.clear()
thisset

# 6. delete set
del thisset

#7. loop set
thisset = {1,'a'}
for x in thisset:
  print(x)

#8. join set
thisset.update({1,2,"afe"})
thisset


# set operations

#1. add()
thisset = {1,'a'}
thisset.add('a')#add(elmnt)

#2. clear()
thisset = {1,'a'}
thisset.clear() # clear all the elmnts

#3. copy()
thisset = {1,'a'}
set2=thisset.copy()
set2

#4. difference between two set
{1,2,"b"}.difference({12,31,'a','c',1}) # difference(set), return the elmnts that first set has but second set does not have

#5. remove the common elmnts between two sets, difference_update(set)
# returns the first set without sharing elmnts
thisset={1,2,"b"}
thisset2={12,31,'a','c',1}
thisset.difference_update({12,31,'a','c',1})
thisset

#6. set.isdisjoint(set), no sharing elmnt(s) in two sets, return True
thisset={2,"b"}
thisset2={12,31,'a','c',1}
thisset.isdisjoint(thisset2)

#7. discard(value), remove a specified value from a set
thisset={2,"b"}
thisset.discard(2)
thisset

#8. set,intersection(set1, set2, set3, setn)
# return common items within sets, can be used for multiple sets
thisset={2,"b"}
thisset2={2,'c'}
thisset3={231,21,2,'d'}
thisset.intersection(thisset2, thisset3)

#9. remove the items that is not present in both the sets
thisset={2,"b"}
thisset2={2,'c'}
thisset3={231,21,2,'d'}
thisset.intersection_update(thisset2, thisset3)
thisset
# to be noticed, intersection_update() and intersection() are different, because the intersection() method returns a new set but intersection_upddate() removes the unwanted items from the original set


#10. subset()
#set1.issubset(set2) to know if set1 is a subset of set2
thisset={2,"b"}
thisset2={2,'c'}
thisset.issubset(thisset2)

#11. superset()
# set1.superset(set2) to know if set1 is superset of set2
thisset={2,"b"}
thisset2={2}
thisset.issuperset(thisset2)

#12. pop() method
thisset = {2,'b'}
thisset.pop() #pop the last element

#13. remove() to remove a specific item
thisset={2,"b"}
thisset.remove('b')
thisset

#14. return a set that includes all items from both sets except common items,  set1.symmetric_difference(set2)
thisset={2,"b"}
thisset2={2,'c'}
thisset.symmetric_difference(thisset2)

#15. symmetric_difference_update() updates the original set by removing items that are present in both sets and insert the other items in
# set.symmetric_difference_update(set2)
thisset={2,"b"}
thisset2={2,'c'}
thisset.symmetric_difference_update(thisset2)
thisset

#16. return a set that contains all items from both sets, duplicates are excluded
# actually you can union multiple sets, set.union(set1, set2, ... setn)
thisset={2,"b"}
thisset2={2,'c'}
thisset.union(thisset2)

#17. update() can be used for joining two sets, or adding items from another iterable
thisset={2,"b"}
thisset.update([1,2,"ds","1s"])
thisset
