#1.svd singular value decomposition

# A = U @ epsilon @ V.T
# A.T @ A = V @ epsilon^2 @ V.T =V @ epsilon^2 @ inverse of V, because V is orthogonal
# A.T @ A @ V = V @ epsilon^2
# first step get epsilon^2, this is the eigen value of A.T @ A
# then get V, the orthogonal basis for column space of A

# A = U @ epsilon @ V.T
# A @ A.T = U epsilon^2 U.T
# A @ A.T @ U = U epsilon^2 becuase U is orthogonal
# then get U, the orthogonal basis for row space of A 
U,S,V = np.linalg.svd(a)#V is actually V's transpose

#2. spectral theory
# if you want to make rainbow, more colors you have, the more are the thing made from there colors like rainbow

# like in PCA, the more lambdas oe components you choose, the matrix is more like original matrix


#3. percent variance of singular values
# simply, sigma i = 100*singma i/ the sum of sigma, then sigma is in percent

#4. moore-penrose pseudoinverse
# you can use svd to compute moore-penrose pseudo-inverse
# the inverse of A = the inverse of (U epsilon V.T)

#5. compare with SVD, pseudo inverse and left inverse
# pseudo inverse is more stable than left inverse 
