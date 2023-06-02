# 1. project in R2
#how to compute the distance of two vectors?
# distance is :b-beta*a
# get beta: a.T (b-beta*a)=0, then beta = a.T * b / a.T * a

# 2. project in RN
# A.T(b-Ax)=0, x is a vector of scalar beta
# Ix= inverse of (A.T @ A) * (A.T @ b)

a=np.array([[1,0],[0,3]])
b=np.array([1,1])
#method1
np.linalg.inv(a.T @ a) @ (a.T @ b)
#method2
np.linalg.pinv(a) 
#method3
np.linalg.solve(a.T @ a, a.T @ b)

#when a matrix is invertible, its left inverse equals to right inverse and inverse

#2. decomposition?
# for a vector w projecting to vector v, find a sub-vector is parpendicular with v and another sub vector is parrallel with v
# how to get the sub vector that is parrelel with v?
# this vector = ((the inverse of v.T @ v) multiply (w.T @ v)) @ v
# then the parpendicular vector is w-parrallel vector

#to be noticed that the methodology of decomposition of a vector is different from matrix decomposition
# inverse of v.T @ v is same as 1/dot(v,v)
# then use np.dot(v,w)/np.dot(v,v) to get the beta

#3. orthogonal matrices(properties in sqaured matrix)
# use letter Q, all columns are pairwise orthogonal
# each column has magnitude 1
#dot<Qi, Qj> = o when i!=j
#Q.T @ Q = I = inverse of Q @ Q then Q.T = inverse of Q

#4. when a orthogonal matrix is rectangular
# either Q.T @ Q = Q-1 @ Q or Q @ Q.T = Q @ Q-1 but not entire

# 5. Gram-Schmidt procedure
# use ((the inverse of v.T @ v) multiply (w.T @ v)) @ v to get pairwise orthogonals
a = np.array([[1,1,-2],[3,-1,1]])
a1 = (1/(1+9)) * np.array([[1,3]])
a2 = np.array([[1,-1]]) - (1*1+3*-1)/(1+3**2) * np.array([[1,3]])
a3=[0,0]

# 6. QR decomposition
# get the orthogonal matrix of A then use Q.T @ A to get R
# R is always orthogonal because the later column is always orthogonal with ealier column
a = np.array([[1,1,-2],[3,-1,1]])
Q,R= np.linalg.qr(a,'complete')
Q,R

#7. Matrix inverse via QR decomposition
#A=Q@R
#A's inverse = inverse of R @ inverse of Q
# inverse of R is easier to compute, because its upper triangular matrix
