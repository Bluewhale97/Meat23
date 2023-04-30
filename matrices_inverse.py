# 1. matrix inverse
# matrix inverse is subject to LIVE EVIL! too
# a matrix is invertible if it is squared and full rank
a=np.array([[1,2],[4,0]])
np.linalg.inv(a)

#2. steps of getting inverse
# to compute to determinant, if that is not 0, that has inverse, not 0 means it is full rank and squared

#3. MCA algorithm: to compute the inverse of A
# M: the minor matrix, also called a matrix of determinants
# C: the M hadamard-multiplies with hi,j=(-1)^(i+j)
# inverse of A = C*det(A)

#4. get inverse via row reduction
#rref([A|I]) => (I|inverse of A), the downside is that sometimes A is not invertible, so we cannot use rref for it
# why rref works?
# to solve Ax=b is equal to get rref of [A|b] and then get x
# A@inverse of A = I is euqal to get rref of [A|I] and then get (I|inverse of A)

#5. rectangular matrices can have left-inverse and right inverse
# for example, a matrix mxn, rank is n, than A.T@A has full rank, rank is n
# left inverse: (A.T @ A).inv @ A.T
# right inverse A.T @ (A @ A.T).inv

#it is very important to check the determinant of the matrix then it is good to compute inverse, left inverse check column rank and right inverse check 
a=np.array([[1,2,3],[4,7,0],[5,7,9]])
np.linalg.matrix_rank(a.T @ a) # when rank of A is less than n (n ≤ m), actually we cannot get the left inverse, but python gives Moore-Penrose pseudo-inverse for it.
#to compute moore-penrose pseudo inverse
np.linalg.pinv(a) 
# Moore-Penrose pseudo inverse is only for 2d matrices, i guess there are more types of pseudo inverses that are used in linalg.pinv, that makes higher dimension matrices get their inverse
