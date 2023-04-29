#1.matrix multiplication, dot product on matrics
a=np.array([[1,2,3],[3,4,2]])
b=np.array([[1,2],[4,5],[7,8]])
np.dot(a,b)
# or use @
a@b

#2. matrix multipilication with a diagonal matrix
# matrix multiplication is like row x column, so that means the first column times a, second column times b, third column times c

#3. transpose with multiplication
#LIVE EVIL!
# (LIVE).T = E.T @ V.T @ I.T @ L.T

#4. rotation matrix
# a matrix helps to change the original vector's direction and norm(scale)
# the matrix that cannot lead to rotation is the eigenvector of that matrix, you also can get the eigenvalue from there
#AV=lambda*V, lambda is the eigenvalue, and V is the eigenvector

#5. work with identity matrix
#A@I = A
#A+I != A
#A+0 =A

#6. methods to create a symmetric matrix
#method 1:A+A.T = S
a = np.array([[1,2],[2,3]])
a+a.T#a should be square matrix
#method 2: A.T @ A
a = np.array([[1,2,3],[3,4,2]])
a.T @ a #proof: a.T @ a = (a.T @ a).T

#7. use a.T @ a can get the covariance matrix of a 

#8. element wise multiplication, also called hadamard product
#hadamard product has two methods
#method 1;
np.multiply(a,a)
#method 2
a*a
#hadamard is element wise multiplication, not matrix multiplication '@'

#7. multiplication of two symmetric matrices
# if the matrices are symmetrical and diagnols are constand, then their multiplication is a symmetric matrix
a = np.array([[1,2],[2,1]])
b = np.array([[3,1],[1,3]])
a@b

#8. frobenius dot product
#step1. matrix multiplication
#step2. sum all elements
#method1, call the linalg.norm func
np.linalg.norm(a,ord='fro')
#method2, compute the squared error of the trace of ata
np.sqrt(np.trace(a.T@a))
