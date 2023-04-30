#1. diagonalization
#AV1 = lambda1 V1
#AV2 = lambda2 V2
#AVn = lambdan Vn

#A = V@ lambda @ inverse of V 
# eigendecomposition = diagonalization

#2 one of uses of eigendecomposition
# A**4 = V @ lambda**4 @ inverse of V
a= np.array([[1,0,0],[0,1,0],[0,0,1]])
d1,v = np.linalg.eig(a)
#then a**4
d2 = np.diag(d1)
v @ np.linalg.matrix_power(d2,3) @ np.linalg.inv(v)

#3. k**2 @ x=lambda^2 @ X
#K2X = KKX =K lambda X= lambda KX = lambda lambda X = lambda^2 X

#4. distinct lambda has dependent eigenvectors

#5. singular matrix eigen decomposition
a=np.array([[1,2],[1,2]])
np.linalg.det(a) #determinant is 0 then a is singular matrix
np.linalg.eig(a)#the determinant equals the product of all eigenvalues, and one of eigen value is 0 so determinant is 0

#6. generalized eigendecomposition
#SV = lambda R V
#previous R is I
#the uses of this is like to compare signal data with noise data, R is the noise added
# now (S-lambda R) @ V = 0
import scipy.linalg
scipy.linalg.eig(a,np.array([[1,0],[0,1]]))
