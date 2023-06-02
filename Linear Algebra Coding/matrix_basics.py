#Matrixs basics
#1. some terms
#bloacks: a part of the matrix
#diagnal and off-diagnal
# R(mxn) is not euqal to R(mn), e.g. R3x2 is not R2x3

#2. tensor v.s. matrix
# tensor : mxnxk
# matrix : mxn

#3. square matrix v.s. rectangular matrix
#while m=n => square matrix

#4. symmetric matrix, and skewed matrix
# a matrix is symmetrix while aij = aji, the diagnal can be any values
# a matrix is skew symmetric which aij = -aji

#5. identity matrix
#the diagnal values are all 1, and off-diagnal values are all zero
# it is always sqaured and symmetric matrix
# any matrix times identity matrix is themself

#6. zero matrix
# all the elements in this matrix is zero

#7. diagnal matrix: all zaros on the off-diagnals and non-zeros on the diagnal

#8. triangular matrix
#upper triangular, the matrix the left area below the diagnal is zero
#lower triangular, the matrix the right area upon the diagnal is zero

#9. concatenation: two matrix with same rows

#10. code these matrix types
S = np.random.randn(5,5)
R = np.random.randn(5,2)
I = np.eye(3)
Z = np.zeros((4,4))
D=np.diag([1,2,3,4,5])
print(S,'\n',R,'\n',I,'\n',Z,'\n',D)


#11. matrix addition and subtraction
#only for matrix having same number of elements and shapes
m1=np.array([[1,3],[2,3]])
m1 + np.eye(2)
#matrices are commutative A+B=B+A & associative A+(B+C)=(A+B)+C

#matrix shifting: A+lambda*I =C

#12. matrix scalar multiplication
lambda1=2
A=np.array([[1,2],[3,4]])
lambda1 * A == A * lambda1

#13. transposing a matrix
A.T.T == A

#14. for symmetrix matrix, itself is euqal to its transpose
S=np.array([[1,2],[2,1]])
S.T == S
# skew symmetric matrix has S.T = -S only for off-diagnal values

#15. the transpose of complex matrix
# change the signs of the imaginary part of off-diagnal values(do not change diagnal values), and transpose it 
c=np.array([[1,1+2j],[2,1-2j]])
c.T#array([[1.+0.j, 2.+0.j],[1.+2.j, 1.-2.j]])

#16. how to extract the diagnal of the matrix
np.diag(S)
np.trace(S)#trace=a11+a22+ann #the sum of diagnal values 

#17. broadcasting matrix
a=np.reshape(np.arange(1,13),(3,4),'F')#F by column, C by row, by row by default
r=[10,20,30,40]#list, for row
c=[100,200,300]#list, for column

a+r #python only for rows
#a+c, this doesnt work
print(a)
a+np.reshape(c,(len(c),1))

#18. code for A times B
S1=np.array([[1,0],[2,1]])
S2=np.array([[1,2],[2,1]])
np.multiply(S1,S2)


