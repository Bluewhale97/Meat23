from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition, manifold

class sklearn.manifold.LocallyLinearEmbedding()

##Params
# n_neighbors: integer for k neighbors 
# n_components
# reg: a float for the parameters of standardization
# eigen_solver: string for the algo to get eigenvalues 'auto': algo picks one, 'arpack': use Arnoldi solver, 'dense': use a algo that can directly get the eigenvalue like LAPACK
# tol: float for threshold of convergence when solving eigenvalues, but it is not used while using 'dense' solver
# max_iter: float for max iteration, useless while sover is 'dense'
# method: 'standard': use standard LLE, 'hessian': use Hessian eignmap, 'modified': use modified LLE, 'ltsa': use local tangent space alignment
# hessian_tol: float for threshold value of method='hessian'
# modified_tol: float for threshold value of method='modified'
# neighbors_algorithm: a string for find nearest 'ball_tree': use balltree, 'kd_tree' use KDTree and 'brute' for force brute. 'auto' is finding a fit algorithm automatically
# random_state: integer, RandomState instance or None

##Attributes
# embedding_vectors_: provide the embedding matrix in lower space
# reconstruction_error_

##Methods
#fit()
#transform()
#fit_transform()

def test_LLE(data):
  X,y=data
  for n in [4,3,2,1]:
    lle=manifold.LocallyLinearEmbedding(n_components=n)
    lle.fit(X)
    print('reconstruction_error(n_components=%d):%s'% (n, lle.reconstruction_error_))
    
    
 test_LLE(data=load_data())# reconstruction error is a neutral metric so big this doesn't mean bad or good


# plot to see its distribution
def plot_lle(data):
  X,y=data
  Ks=[1,5,25,y.size-1]
  fig=plt.figure()
  for i,k in enumerate(Ks):
      lle=manifold.LocallyLinearEmbedding(n_components=2,n_neighbors=k)
      X_r=lle.fit_transform(X)
  
      ax=fig.add_subplot(2,2,i+1)
      colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  
      for label, color in zip(np.unique(y), colors):
           position=y==label
           ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
      ax.set_xlabel("X[0]")
      ax.set_ylabel("Y[0]")
      ax.legend(loc='best')
  ax.set_title("lle,k=%d"%k)
  plt.show()
  
  
  plot_lle(data=load_data())
  
  
  # now have a case for just 1 dimension
def plot_lle_k_d1(data):
  X,y=data
  Ks=[1,5,25,y.size-1]
  
  fig=plt.figure()
  for i,k in enumerate(Ks):
    lle=manifold.LocallyLinearEmbedding(n_components=1, n_neighbors=k)
    X_r=lle.fit_transform(X)
    
    ax=fig.add_subplot(2,2,i+1)
    colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  
    for label, color in zip(np.unique(y), colors):
         position=y==label
         ax.scatter(X_r[position,0],np.zeros_like(X_r[position]), label="target=%d"%label, color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel("Y[0]")
    ax.legend(loc='best')
  ax.set_title("lle")
  plt.show()
  
  
  plot_lle_k_d1(data=load_data())
  
  
  
