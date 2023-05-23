#Random clustering

# import libaries 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture

# create a function to make data
# centers: array for centroids, e.g. [[1,1],[2,2],[10,20]]
# num: sample size
# std: standard deviation of each cluster

# this func returns clusters of Gaussian distribution
def create_data(centers, num=100, std=.7):
  X, labels_true = make_blobs(n_samples=num, centers=centers, cluster_std=std)
  return X, labels_true

# Create plot func
def plot_data(*data):
  X, labels_true=data
  labels=np.unique(labels_true)
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  colors='rgbyckm'
  for i, label in enumerate(labels):
    position=labels_true==label
    ax.scatter(X[position,0], X[position,1], label='cluster %d'%label,
               color=colors[i%len(colors)])
  ax.legend(loc='best',framealpha=.5)
  ax.set_xlabel('X[0]')
  ax.set_ylabel('Y[1]')
  ax.set_title('data')
  plt.show()
  
  
X, labels_true=create_data([[1,1],[2,2],[1,2],[10,20]],1000,.5)
plot_data(X,labels_true)
