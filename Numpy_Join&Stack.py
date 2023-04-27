#DBTITLE 1, Numpy array joining
#put two or more arrays in a single array in SQL we join tables based on key, whereas in Numpy we join arrays by axes, using concatenate() along with the axies, if axis is not explicitly passed, it is taken as 0

#1. join 2 arrays
a1=[[1,2,3]]
a2=[[4,5,6]]
np.concatenate((a1,a2),axis=0)#pass your arrays into a tuple object, axis=o means concatenating through the 1st dimension, the detail steps is like stripping the first bracket, and combine the elements in the first dimension, so this can be [[1,2,3],[4,5,6]]

#2. stack 2 arrays
#almost same with joining method, but it is doing along with a new axis
#this can be confusing, so how to understand it?
#for example, if axis=1, that means step1: create a new axis very out of the first parenthesis. step2: because axis=1, so go to the second bracket, or you can understand as the first bracket before creating a new one, like in this example, the second bracket is "["[1,2,3]], this one. And stack an array over the another one, so the finally array is [[[1,2,3],[4,5,6]]]
# if the axis=2, that means that you need to find the 3rd bracket, and do stripping,  the final result can be [[[1,4],[2,5],[3,6]]]
a1=[[1,2,3]]
a2=[[4,5,6]]
np.stack((a1,a2),axis=1)

# hstack() to stack along rows(heights), it see the arrays as in the same row
# in my understanding, hstack() only strip no more than 2 bracket, for example if an array is 4 dimensions, when you do hstack() to stack along rows
# it will give you [[[[1,2,3]],[[4,5,6]]]]
# but if just 2 dimensions, it can be [[1,2,3,4,5,6]]
a1=[[1,2,3]]
a2=[[4,5,6]]
np.hstack((a1,a2))

#vstack() to stack along columns(vertical), the way it does is: step 1: strip one bracket 2: combine the two arrays/element in this dimension
a1=[[[[1,2,3]]]]
a2=[[[[4,5,6]]]]
np.vstack((a1,a2))


#dstack() to stack by height(depth)
np.dstack((a1,a2))#the way dstack does is: strip 3 bracket, 2: combine the elements/arrays in that dimension
