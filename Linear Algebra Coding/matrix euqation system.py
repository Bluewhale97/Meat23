#system of equations

#1. system of Ax=b or alpha * beta =y, alpha is designed matrix, beta is regression coefficient and gamma is observed data
#does it always have solution?
#yes, because b belongs to the column space of A, but realistically, there are noises, so b can be sometimes not in the column space of A

#2. system of Ax=0
#we use this to find the null space of A
# matrix x is the null space of A or right null space of A
#sometimes A doesnt have null space, so there is no 0 in eigen values

#3. gaussian eliminaton
# convert equations to matrix equation
# augmente matrix
#manipulate into upper triangular matrix
#map this matrix to original euqation
#get the values of solution

#so the final gaussian elimination form should be a upper-triangular matrix

#4. echelon form and pivots
#zeros are below and left the matrix(pivots)

# reduced row echelon form RREF 
# all the pivots should have 0 above the pivots and each pivot should be 1 and the 0 below pivots should be bottom left(meet echelon form principle)

#5. any square full rank matrix has the identity matrix as its reduced row echelon form
a = np.array([[1,1,0],[0,1,1],[1,0,1]])
from sympy import Matrix
Matrix(a).rref()

#6. matrix space after row reduction
# the rank of A and row space, dim of row space and col space are not changed
# but the plane of column space is changed
#for example [[1,2],[3,7],[9,1]] => [[1,0],[0,1],[0,0]], they are two different planes

#7.determinants: det(A), only for squared matrices
# det(A)=0, if linearly dependent columns/rows are there, matrix is non-invertible while it is not full rank

