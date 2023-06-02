#vector basics

#1. terminology: linear algebra and matrix algebra
# same, but linear algebra is more for theory and proofs whereas matrix algebra is for applications

# 2. what is vector
#ordered list of numbers 
#their dimensionality is the number of elements

#3. row vector and column vectors
#(1,2), (1,2).T

#4. properties
#no starting point, but has 'head' and 'tail'
#standard position is a position of the vector started in origin

#5. vector valued function
(sin(x),xcos(x),x)

#6. create vectors in python
#2-d
v2=[-1,3]
np.array(v2)
#3-d
v3 = [4,-3,2]
v3a=np.array(v3)
#row to col
np.transpose(v3)#no need for v3 to be array
v3a.T#need v3 as an array

#7. addition
v1=np.array([-3,1])
v2=np.array([1,2])
v3=v1+v2
v4=v1-v2
print(v3,v4)

#8. what is scalar
#single number
#some naming conventions
#symbol A,M, C for matrix
#v,u,w for vector
#a,beta, lambda for scalar

#9. vector-scalar multiplication
lamda=3
v=np.array([-3,2,1])
lamda*v

#10. dot product on vectors
#dot product on vector, the output is a scalar
#method 1
np.sum(np.multiply(v1,v2))
#method 2:
np.dot(v1,v2)
#method 3
np.matmul(v1,v2)
#method 4
sum=0
for i in list([0,1]):
  sum=sum+v1[i]*v2[i]
sum

#11. vectors are not associative, but distributive and commutative
#not associative
v1=np.array([1,2,3,4,5])
v2=np.array([2,3,1,4,0])
v3=np.array([1,9,231,1,4])
result1=np.dot(v1,v2)*v3
result2=v1*np.dot(v2,v3)
print(result1,result2)

#distributive
result3=np.dot(v1,v2+v3)
result4=np.dot(v1,v2)+np.dot(v1,v3)
print(result3, result4)#same

#commutative:ab=ba
result5=np.dot(v1,v2)
result6=np.dot(v2,v1)
print(result5,result6)

#special case when a.T(b.T*c)=(a.T*b).T*c
#a=b=c or one of them is zero vector

#12. vector length
#||v||=sqrt(v.T*v)
#is also called magnitude or norm
v1=np.array([1,2,3,4,5])
#method1:
value1=np.sqrt(np.dot(v1,v1))
value2=np.linalg.norm(v1)
print(value1,value2)

#13. the dot product in geometric
#np.dot(v1,v2) is like ||v1||*||v2||*cos(theta)

#14. element wise multiplication, also called hadamard multiplication
v1=np.array([1,2,3,4,5])
v2=np.array([2,3,1,4,0])
v3=np.array([1,9,231,1,4])

np.multiply(v1,v2)

#15. outer product
np.outer(v1,v2)

#16. cross product
#defined only for two 3d vectors, result is another 3d vector
np.cross([1,2,3],[3,21,1])#2*1-3*63 as a cross
