#DBTITLE 1, Numpy filtering and sorting

#1. Numpy array sorting
#this func works on any dimensions of arrays, like 2-D
arr = np.array([[1,2],[7,5],[2,1]])
np.sort(arr)

#2. array filter, this operation only works for 1-D array
arr = np.array([1,2,3])
x = [True, False, True]
arr[x]

# DBTITLE 1, Numpy randomization
#what is random number: means something that cant be predicted logically
#random numbers generated through a generation algorithm that is called pseudo random

#can we truely make random numbers?
#yes, generating random numbers from our computer requires to get the random data from some outside source

#1. to generate a random integer from 0 to 100
np.random.randint(100)

#2. rand() to return a random float between 0 and 1
x=np.random.rand()
x

# generate random array
#3. 5 random integers from 0 to 100
np.random.randint(100,size=(5)) #1-D array containing 5 elements
#randint(low, high, size)

#4. make a random 2-D array, from 0 to 100
np.random.randint(100,size=(3,5))

#5. make a random 1-D array, float from 0 to 1
#rand(d0,d1,d2,...,dn)
np.random.rand(5)#5 means the size is five

#6. make a 3x5 2-D array
np.random.rand(3,5)

#7. generate values based on an array, using choice function
choice= [1,2,3,8,9]
x=np.random.choice(choice, size=(3,5))
x

#8. random distribution
choice = [1,2,8,9]
prob = [0.1,0.6,0.2,0.1]#prob should be summed to 1
x=np.random.choice(choice, p=prob, size=(3,5))
x

#9. random permutations of elements: arrangement of elements
#method 1: shuffle()
np.random.shuffle(x)
x#output x instead of the object np.random.shuffle(x), it will direclt work on x

#method 2: permutation()
np.random.permutation(x)
x


