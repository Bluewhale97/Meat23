from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition, manifold

# MDS
class sklearn.manifold.MDS()

##Params
#metric: bool, True then measure it using distance, otherwise use SMACOF
# n_components
# n_init: a integer, the times of initialization. Becaused while using SMACOF, it needs different initial values, then choose the best as the final initial values
# max_iter: the max iteration to get the result, while using SMACOF
# eps: float, threshold of convergence
# n_jobs: -1 means assigning jobs to all the CPUs
# random_state: integer or an instance of RamdomState or None, None means using default random seed, a integer means the seed of that integer, and RandomState instance is an assigned generator of ramdomization
# dissimilarity: a string to define dissimilarity, using 'euclidean' or 'precomputed', 'precomputed' means that user provide the distance matrix

## Attributes
#embedding_: provide an embedding matrix for original dataset
#stress_: float for the sum of dissimilarity

## Methods
#fit()
#fit_transform()


def test_MDS(data):
  X,y=data
  for n in [4,3,2,1]:
    mds=manifold.MDS(n_components=n)
    mds.fit(X)
    print('stress(n_components=%d):%s'% (n, str(mds.stress_)))
    
test_MDS(data=load_data())# stree is a neutral metric so big this doesn't mean bad or good


# plot to see its distribution
def plot_MDS(data):
  X,y=data
  mds=manifold.MDS(n_components=2)
  X_r=mds.fit_transform(X)
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  
  for label, color in zip(np.unique(y), colors):
        position=y==label
        ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
  ax.set_xlabel("X[0]")
  ax.set_ylabel("Y[0]")
  ax.legend(loc='best')
  ax.set_title("MDS")
  plt.show()
  
  
plot_MDS(data=load_data())




 
