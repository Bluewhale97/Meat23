# complex vector operation
#1. dot product
v1=np.array([1+3j, 5+4j, 2, 0])
v2=np.array([1,2-2j,3,53])
np.dot(v1,v2)

#2. hermitian transpose (conjugate transpose), to flip the sign of complex parts, help compute the norm
np.dot(v1,v1)#5+46j, how to compute norm?
np.sum(np.transpose(v1.conjugate())*v1)
