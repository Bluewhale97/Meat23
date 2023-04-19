from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition, manifold

#KernelPCA
class sklearn.decomposition.KernelPCA()

##Params
#n_components: integer for the number of dimensions after dimensionality reduction. If None, no change
#kernel: str for kernelization function. 
  #1. "linear": linear kernel, k(x,z)=x*z; 
  #2."poly": polynomial kernel, k(x,z)=(y(x*z+1)+r)^p, p is degree, y is gamma, and r is coef0
  #3. 'rbf': this one is the default kernel, which is a gaussian kernel function, k(x,z)=exp(-y(x-z)^2), y is gamma
  #4. 'sigmoid': K(x,z)=tanh(y(x*z)+r), y is gmma, r is coef0
  #5. 'precomputed': provide kernel matrix or a callable object for computing kernel matrix
# degree: a integer for power of polynomial function
# gamma: float, when kernel is 'rbf', 'poly', 'sigmoid', gamma is the coef y
# coef0: float, for the noise, only used for 'poly' and 'sigmoid'
# kernel_params: usable while kernel is a callable object. It is not used if the kernel is the strings like 'poly', 'rbf', 'sigmoid', 'linear'
# alpha: integer, the hyperparameter of ridge regression, used for fit_inverse_transform=True
# fit_inverse_transform: bool, True to compute the matrix from eigen vectors matrix to original matrix
# eigen_solver: string for computing eigen_solver 'auto': select one automatically; 'dense':dense eigenvector solver; 'arpack': arpack eigenvector solver, it can be used in the case of n_features<<n_samples
# tol: float for threshold of arpack
# max_iter: integer for the biggest iterations of arpack. If None then select automatically
# remove_zero_eig: remove the eigen values of 0. If n_components=None, then remove all the eigen values of 0


##Attributes
#eigenvalues_: eigenvalues of kernel PCA
#eigenvectors_: eigen vectors of kernel PCA
# dual_coef_: inverse convertion matrix


##Methods
#fit()
#transform(X)
#fit_transform()
#inverse_transform()


def load_data():
  iris=datasets.load_iris()
  return iris.data,iris.target
  



def test_KPCA(data):
  X,y=data
  kernels=['linear','poly','rbf','sigmoid']
  for kernel in kernels:
    kpca=decomposition.KernelPCA(n_components=None, kernel=kernel)
    kpca.fit(X)
    print('kernel=%s --> lamdas:%s'% (kernel, kpca.eigenvalues_))
    
    
test_KPCA(data=load_data())


def plot_KPCA(data):
  X,y=data
  kernels=['linear','poly','rbf','sigmoid']
  fig=plt.figure()
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  
  for i, kernel in enumerate(kernels):
    kpca=decomposition.KernelPCA(n_components=2,kernel=kernel)
    kpca.fit(X)
    X_r=kpca.transform(X)
    ax=fig.add_subplot(2,2,i+1)
    for label, color in zip(np.unique(y), colors):
        position=y==label
        ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel("Y[0]")
    ax.legend(loc='best')
    ax.set_title("kernel=%s"%kernel)
  plt.suptitle("KPCA")
  plt.show()
 
 
 plot_KPCA(data=load_data()) # the distribution is different by using different methods
 
 
 
    
 # now discuss params of poly kernel
def plot_KPCA_poly(data):
  X,y=data
  fig=plt.figure()
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  params=[(3,1,1),(3,10,1),(3,10,10),(10,1,1),(10,10,1),(10,1,10),(10,10,10)]
  for i,(p,gamma,r) in enumerate(params):
    kpca=decomposition.KernelPCA(n_components=2,kernel='poly',gamma=gamma,degree=p,coef0=r)
    kpca.fit(X)
    X_r=kpca.transform(X)
    ax=fig.add_subplot(2,4,i+1)
    for label, color in zip(np.unique(y), colors):
        position=y==label
        ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel("Y[0]")
    ax.legend(loc='best')
    ax.set_title(r"$(%s (x \cdot z+1)+%s)^{%s}$"%(gamma,r,p))
  plt.suptitle("KPCA-Poly")
  plt.show()
  
  
plot_KPCA_poly(data=load_data())# the distribution of data is different


# now discuss the params of 'rbf'
def plot_KPCA_rbf(data):
  X,y=data
  fig=plt.figure()
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  Gammas=[.5,1,4,10]
  for i,gamma in enumerate(Gammas):
    kpca=decomposition.KernelPCA(n_components=2,kernel='rbf',gamma=gamma)
    kpca.fit(X)
    X_r=kpca.transform(X)
    ax=fig.add_subplot(2,2,i+1)
    for label, color in zip(np.unique(y), colors):
        position=y==label
        ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel('Y[0]')
    ax.legend(loc='best')
    ax.set_title(r"$\exp(-%s||x-z||^x)$"%gamma)
  plt.suptitle("KPCA-rbf")
  plt.show()
  
  
  plot_KPCA_rbf(data=load_data())
  
  
  
  
  #now discuss params of sigmoid
def plot_KPCA_sigmoid(data):
  X,y=data
  fig=plt.figure()
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  params=[(.01,.1),(.01,.2),(.1,.1),(.1,.2),(.2,.1),(.2,.2)]
  for i,(gamma,r) in enumerate(params):
    kpca=decomposition.KernelPCA(n_components=2,kernel='sigmoid',gamma=gamma, coef0=r)
    kpca.fit(X)
    X_r=kpca.transform(X)
    ax=fig.add_subplot(3,2,i+1)
    for label, color in zip(np.unique(y), colors):
        position=y==label
        ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel('Y[0]')
    ax.legend(loc='best')
    ax.set_title(r"$\tanh(%s(x\cdot z)+%s)$"%(gamma,r))
  plt.suptitle("KPCA-sigmoid")
  plt.show()
  
  plot_KPCA_sigmoid(data=load_data())# be careful to choose y, because if y is big, lots of output values would be 1 and make the kernel matrix not invertible
  

  



 
