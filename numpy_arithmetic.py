# DBTITLE 1, Numpy ufuncs
#ufunc is universal functions that operates on the ndarray object
# it implements vectorization in numpy, faster than iterating
# it provides broadcasting and additional methods like reduce, accumulate
# it has additional arguments like: where(boolean array for where occurs what), dtype for return type of element, out for output array

#1. to compare with iterating with ufunc
#iterating
x=[1,2,3,4]
y=[4,5,6,7]
z=[]
for i, j in zip(x,y):
  z.append(i+j)
z
#ufunc
z=np.add(x,y)
z

#2. create own func:
#define a function then add it to numpy ufunc library with the frompyfunc() method
def myad(x,y):
  return(x+y)
myadd= np.frompyfunc(myad,2,1)#2 means the # of input arguments(arrays), 1 means # of output arrays

myadd(x,y)

#3. check if a func is ufunc: a ufunc should return <'class 'numpy.ufunc'>
type(np.add)#np ufunc
type(myadd)#np ufunc
type(np.concatenate)#builtin function
#you also cal
type(np.add)==np.ufunc#return True for np ufunc

#4. simple arithmetics: +-*/
#you can define arithmentic confitionally where the arithmetic operation should happen
#there are some predefined np.ufunc
arr1=[1,2,3,4]
arr2=[5,6,7,8]
np.add(arr1,arr2)
np.subtract(arr1,arr2)
np.multiply(arr1,arr2)
np.divide(arr1,arr2)
np.power(arr1,arr2)
np.remainder(arr1,arr2)#equal to mod()
np.divmod(arr1,arr2)#return quotients and mods of two arrays
np.absolute(arr1) #or abs()

#5. rounding decimals:truncation, fix, rounding, floor, ceil
#remove decimals and return float number close to zero
np.trunc([-3.1])
#rounding down to n decimal place
np.around([3.143212],2)
#rounding up to n decimal place
np.floor(arr1)
#ceiling
np.ceil(arr1)

#6. perfrom log
np.log2(arr1)#base 2
np.log10(arr1)#base 10
np.log(arr1)#base e

#use math.log() as ufunc
from math import log
log_u = np.frompyfunc(log,2,1)
log_u([225],[15])

#6. summations: addition between two arguments whereas summation happens over n elements
np.add(arr1,arr2)#sum over an axis
np.sum([arr1,arr2])#summing all elements

#7. products: prod()
np.prod(arr1)#one array
np.prod([arr1,arr2], axis=1)#products on a specific axis

#cummulative product
np.cumprod(arr1)#[1,1x2,1x2x3,1x2x3x4]

#8. differences
np.diff(arr1)#begin at the second element, [2-1,3-2,4-3]
np.diff(arr1,n=2)#repeat computing difference,get [1,1,1] at the first time then get [0,0] 


#9. numpy LCM Lowest common multiple
#find it of two numbers
np.lcm(2,21)

#find in two arrays
arr1=[1,2,3,4]
arr2=[5,6,7,8]
np.lcm(arr1,arr2) 

#find in an array
np.lcm.reduce(arr1)

#10. GCD, greatest common denominator, also known as highest common factor (HCF)
#finding GCD/HCF
#for 2 numbers
np.gcd(28,352)
#for an array
np.gcd.reduce(arr2)

#11. trigonometic functions: sin(), cos(), tan() take values in radians and produce the corresponding sin, cos, and tan values
#for a number 
np.sin(np.pi/2)
#for an array
np.sin(arr1)

#12. convertion between radians and degrees
#degree to radian
deg=np.array([90,180])
np.deg2rad(deg)
#radian to degree
np.rad2deg(3.14)

#13. find angles
#for numbers
a=np.arcsin(1) #this is decimal form, so you need to convert it from radian to degree
np.rad2deg(a)

#for array
np.arcsin([1,0.5])

#14. find hypotenues
base=3
perp=4
x=np.hypot(base,perp)
x

#15. hyperbolic function
#sinh(), cosh(), tanh(), you can use them to find angles
np.arcsinh(1.)

#16. create a set array in a numpy
np.unique(arr1)

#17. find union between 2 arrays
np.union1d(arr1,arr2)

#18. find intersection of two arrays
np.intersect1d(arr1,arr2,assume_unique=True)#should be alwasy true when dealing with set, it can speed up computation

#19. find diff
np.setdiff1d(arr1,arr2, assume_unique=True)# this finds values in set1 but not in set2

#20. find symmetric diff
np.setxor1d(arr1, arr2, assume_unique=True)#all the values that set 1 and set2 dont share
