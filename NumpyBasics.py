#DBTITLE 1, Numpy Intro
# a lib shorts for "numerical python"
# have funcs working in domain of linear algebra, fourier transform and matrices
# created by Travis Oliphant

#why use?
#aims to provide array objects that is up to 50x faster than traditional python lists
# numpy array is very easy to be used 

#why faster than lists?
#store at one continuous place in memory unlike list, this action is called locality of reference in computer science
#work with latest CPU architectures

#which languages are numpy written in?
#written in python
#but most of parts that require fast computation are written in c/c++

#some basics

#to check the version of your numpy
import numpy as np
print(np.__version__)

#create ndarray object
a=np.array([1,2,3,4,5]) #pass an iterable, or array-like object

#index array
a=np.array([1,2,3,4,5])
a[0]

#index nested array, like 2-D array
arr = np.array([[1,2,3],[4,5,6]])
arr[1][2]

#3-D array indexing
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[2,4,1],[2,4,1],[6,5,3]]])
arr[1][2][1]

#negative index
a=np.array([1,2,3,4,5])
a[1]

#array slicing
arr[1:5] #index 1 to index 5, exclusively
arr[2:] # from index 2 to end
arr[:4] # from start to index 4, exclusively
#arr[-3,-1]#from the index -3 to index -1, exclusively

#STEP: determine steps of the slicing
#jump 2 steps
a=np.array([1,2,3,4,5])
a[1::2]#from the value of index 1 to the end, but jump 2 steps every time
a[::2]#walk through all values, jump 2 steps

#2-D array
a=np.array([[1,2,3,4,5],[6,1,2,1,9]])
a[1,2:4]#array([2,1])


#numpy data types: 
# you know python has some datatypes like strings, integer, float, boolean, complex
# numpy has more types, from basic types of python, like complex float, unsigned integer, timedelta, datatime, object, unicode string, fixed chunk of memory for other type(void)

#1.check the datatype of an array object
a=np.array([[1,2,3,4,5],[2,13,4,1,0]])
type(a) # if you use type, it will just give you the type of this py object
a.dtype #it can tell you the type of your elements in your array

#2.use dtype argument to create type of array
a=np.array([100,2,3,4,5],dtype='S')#'S' means string
a.dtype#'S3' means the max size of your element, like for example, this element is a string, with 3 digits, so it is S3 

#3.use dtype argument to create type of array
a=np.array([1,2,3,4,5], dtype='S4') #4 bytes integer

#4.when define the datatype of your array, some values cannot be converted it will raise ValueError Exception
#a=np.array([1,2,3,4,5,'a'], dtype='i')

#5.convert data type on existing array
a=np.array([1,2,3,4,5])
b=a.astype('S2')
b.dtype
a

#6. copy v.s. view
#make a copy
a=np.array([1,2,3,4,5])
x=a.copy()
#make a view
a=np.array([1,2,3,4,5])
x=a.view()
#check if array owns its data
x.base #if it has the value, means it has original one, os it is a view



#7.  use ndmin to create many dimensions of array
a=np.array([1,2,3,4,5],ndmin=4)
#the shape of your array
a.shape#(1,1,1,5), 1*1*1*5

#8. reshape your array
#from 1d to 2d
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
a.reshape(2,6)
#from 1d to 3d
a.reshape(2,2,3)
#need to do a math to count elements

#so, there is a question, is reshaped array a view or a copy?
a=np.array([1,2,3,4,5,6])
b=a.reshape(2,3)
b.base#so, an reshaped array is a view!

b=a.reshape(2,-1) #if you do not know the size of one another dimension, put -1, but you cant put -1 more than once

#9. flatten your array
a=np.array([[1,2],[3,4]])
a.reshape(-1)



#DBTITLE 1, array iterations
#1.1D array
a=np.array([1,2,3,4,5])
for x in a:
  print(x)
#2.2D array
a=np.array([[1,2],[4,5]])
for x in a:
  for y in x:
    print(y)
#3.3D array:
# for x in a:
#   for y in x:
#     for z in y:
#       print(z)
# the another way is using nditer(), to iterate through 3D array
a=np.array([[[[1,2,3,4],[1,3,4,5]]]])
for x in np.nditer(a):
  print(x)#seems its function is equal to flatten your array using np.reshape(-1)

#4.change dtypes while iterating array, have a argument flags=['buffered'], because you need more spaces
for x in np.nditer(a, flags=['buffered'], op_dtypes=['S']):
  print(x)

#5.you also can iterate by steps
for x in np.nditer(a[::2]):
  print(x)

#6. enumerate iteration using ndenumerate():
#enumeration means mentioning sequence number of the element one by one, sometimes we need the corresponding index of the element while iterating, so this is the functionality of ndenumerate()

for index, x in np.ndenumerate(a):
  print(index, x)#this index is a tupe, contains the index of each dimension
  
  
  
