#1. unit vector: length=1
#to scale your vector to be unit vector
v1=np.array([1,2,3,4,5])
v2=np.array([2,3,1,4,0])
v3=np.array([1,9,231,1,4])

v1/np.linalg.norm(v1)

#2. what is dimensions in a vector?
#numeric fields than can do arithmetic operations
#R: real numbers 
#C: complex numbers
#Z: integers(this is not a field), integer/integer can be a float, this is out of integer space, so it is not field

#3. subspace
v=np.array([1,2])
lambda1 = 1
lambda2=2
lambda3=3
lambda1*v
lambda2*v
lambda3*v #these three are in the same subspace

#4. create subspace from many vectors
w=np.array([2,0])
#you can use w and v to consist of many different vectors but they are all in the same subspace
v+w
#! a vector subspace must be closed under addition and scalar multiplication and contain the zero vector!
#more vectors doesnt mean more dimensions in subspace becuase some vectors can be in the same subspace

#5. subset vs subspace
#subset is a set of points
#for example, (x>0,y>0) can be a subset but not a subspace, because origin is not icluded
# x^2+y^x =1 can be a subset, but not a subspace, like 10*[1,0]=[10,0] out of the subspace
# y=4x can be either a subset or a subspace
# y=4x+1 is not a subspce, the origin is not included

#origin should be included and can be write down in this form alpha*v+beta*w 

#6. span
#span and subspace are same thing
#span({v1,v2,v3,...,vn})=alpha1*v1+alpha2*v2+...+alphan*vn

#7. linear independence
#if a vector can be lambda times another vector, that means this vector and that another vector are dependent

#8. basis
#independent vectors construct a span
#any one of vectors cant be considered as others
R3 = [[0,0,1],[0,1,0],[1,0,0]]
#why basis should have independent vectors only?
#otherwise a vector can be described as many combinations of vectors
