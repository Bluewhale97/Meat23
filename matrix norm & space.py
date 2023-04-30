#1. the definition of rank of a matrix
# the max rank = min(m,n) 
# rank is a property of a matrix
# when a is mxm square matrix and rank(a) =m, means full rank
# when a is mxn, rank(a)=m, means full column rank
# when a is mxn, rank(a)=n, means full row rank

# you can understand the rank as the dimensionality of the information
# the rank of a matrix is the largest number of columns or rows that can form a linearly independent set

#2. methods to compute rank:
#method 1, compute the number of columns in a linearly independent set or the span of the matrix, you have to do guesswork, visual inspection
#method 2, apply row reduction to reduce matrix to echelon form and count the number of pivots
#method 3, compute the singular value decomposition and count the number of non-zero singular values
#method 4, compute the eigen decomposition and count the number of non-zero eigenvalues

#3. difficulty in computing rank of a matrix
#precision, rounding errors
#general computing rounding error is 10e-15
#the question is like for 50x50 rank-46 matrix, is lambda=10e-13 real or 0? if it is real, then if non-zero eigenvalues are actually 50? how to decide?

#we should allow a bit noise when computing it

#4. compute rank
a=np.array([[1,2],[4,2],[1,0]])
np.linalg.matrix_rank(a)

#5. rank(a+b)<= rank(a) + rank(b)
# rank(ab)<=min{rank(a), rank(b)}
#rank(a)=rank(a.T @ a) = rank(a.T) = rank(a @ a.T)

#6. how to make a matrix full rank by shifting
# a should be a squared matrix
a=np.array([[1,2,3],[2,4,6],[2,3,0]])
print(np.linalg.matrix_rank(a))
a_shift = a + np.eye(3)
print(np.linalg.matrix_rank(a_shift))


#7. column space of a matrix
#c(a)=span({a1,a2,...,an})

#the row space of a is the columns space of a.T

#8. the uses of column space
#if a vector is belonging to c(a), then you can get the coefficient, ax=b, compute x
#if not, you can compute how close is it to c(a), a-b

#9. null space
#the set of all vectors {v} such that Av = 0, if have a vector v makes Av=0, then there are many v, then we call it null space
#null space is like a black hole, once gets into the null space you are zeroed out and you cant escape

#10. left null space and right null space
# N(A.T): v makes A.T @ v, v is not zero matrix/vector, this is left null space
# N(A): right null space also called null space

#11. a@N(a)=0, then a perpendicular with v=N(a)
# the null space is perpendicular with the span/space of a

#12. geometrically, a matrix's column space is orthogonal with its left null space, then N(A.T) contain all the places except the area of C(A)
# for mxn matrix, dim(C(A)) + dim(N(A.T)) = m
# dim(R(A)) + dim(N(A)) = n, R(A) is also equal to C(A.T)
