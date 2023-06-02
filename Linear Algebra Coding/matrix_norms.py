#1. Frobenius norm is also called Euclidean norm
# norm(A) = square root of the trace of A.T @ A
a = np.array([[1,2,3],[2,1,4]])
np.linalg.norm(a,ord='fro')

#2. Induced p-norm, find the largest eigen value and let it^(1/p)
#||A||p = sup ||Ax||p / ||x||p, how much A scales vector x, need to find the eigen values
# if A is pure rotation matrix, then ||A||p =1
# if p =2, it is called induced 2-norm:
np.linalg.norm(a, ord=2)
#another method is 
np.sqrt(np.max(np.linalg.eig(a.T @ a )[0]))#index 0 for eigen values, then find the max eigen value and sqrt it

#3. shatten p-norm
#||a||p = (the sum of (singular values**p))**(1/p)
#first step gets singular values
sv=np.linalg.svd(a)[1]
#then sum the exponentialized singular values
np.sum(sv**3)**(1/3)

#4. hadamard division
# the denominetor matrix should not contain zero
