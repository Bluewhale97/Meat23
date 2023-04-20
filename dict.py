# dict intro
# dictionaries are changeable, ordered(since py 3.7) and not allowing duplicates

#1.access items 
thisdict = {"a":1, "b":"stan", "c":{}}
#either use bracket
thisdict['a']
# or get()
thisdict.get('a')

#2. get all keys
thisdict.keys()

#3. get all items
thisdict.values()

#4. get all key-value pairs
thisdict.items()

#5. check if key exists:
'a' in thisdict.keys()

# dict operations
#1. change items
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict['a']=2
# or use update()
thisdict.update({"a":2,"b":'asa'})#update multiple items

#2. add items:
thisdict['color']='red'
# or use update()
thisdict.update({'color':'red','age':30})

#3. remove items
#use pop
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.pop("a")
thisdict

#use del
del thisdict['b']

#use clear(), this can clear the list but it doesnt release the spaces, it doesnt work for value, just list
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.clear()

#4. loop dicts
thisdict = {"a":1, "b":"stan", "c":{}}
for x in thisdict:
  print(x)
for x in thisdict.items():
  print(x)
for x in thisdict.keys():
  print(x)
for x in thisdict.values():
  print(x)
  
#5. copy dicts
#either use copy function
thisdict = {"a":1, "b":"stan", "c":{}}
dict2=thisdict.copy()
#use dict2=thisdict, then dict2 will be a reference of thisdict
thisdict = {"a":1, "b":"stan", "c":{}}
dict2=thisdict
dict2.clear()
thisdict#see here, thisdict has been cleared 

#6. nested dictionary indexing
#simpy by []
thisdict = {"a":1, "b":"stan", "c":{1,2}}
thisdict["c"].pop() #to be noticed, set doesnt have order or index so it will randomly pick an element


#some dictionary methods
#1.clear(), use this one to clear your list
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.clear()
thisdict

#2. copy(), use this to copy your list not reference
thisdict = {"a":1, "b":"stan", "c":{}}
dict2=thisdict.copy()
dict2

#3. fromkey(keys, value), return a specfied dict with keys and values
# this like create multiple (key, value) per time
x = {'key1','key2','key3'}
y=2
dict.fromkeys(x,y)#y should be a value and assign this value to every key, this value can be int, str, float, or any other types like tuple, dict, set

#4. get(keyname, value), get the value of the item with the specified key, value param is option, it will return this value if the specified key does not exist, it will erturn the key value if the key does exist
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.get('a',2)# see, if value=2, it will still return the real value 1
thisdict.get('as',1)#see, key 'as' doesnt exist, so return this optional value

#5. items()
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.items()#get pairs of key,value

#6. keys()
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.keys()#get keys of this dict

#7. pop(keyname, defaultvalue), keyname is required for dict. defaultvalue is optional, it will be returned if the specified key do not exist
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.pop('as',1)#not exist so return default value
thisdict.pop('b')#exist, so return the real value

#8. popitem() to remove the last pair of items
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.popitem()

#9. setdefault(): returns the values of the item with the specified key. If the key does not exist, insert the key with the specified value. The default value is None
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.setdefault('as','ass')#it added
thisdict

thisdict.setdefault('great')
thisdict

#10. update dictionary with pairs of key, value. update(iterable)
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.update({"as":"ass","good":'god'})

#11. get the values of a dict
thisdict = {"a":1, "b":"stan", "c":{}}
thisdict.values()
