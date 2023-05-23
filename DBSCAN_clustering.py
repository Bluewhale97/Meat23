# import libaries 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture

# DBSCAN
# class sklearn.cluster.DBSCAN()

## Params:
# eps: epsilon, for the size of neigborhood
# min_samples: MinPts: for core objects
# metric: a string or a callable, for computing distance, if string, must assign from metric.pairwise.calculate_distance
# algorithm: a string, to compute the distance of two points and find the nearest neighbor. 'auto': automatically find the good algo, 'ball_tree': use ball tree to find, 'kd_tree': use kd_tree to find, 'brute' use force brute to search
# leaf_size: integer, when algorithm=ball_tree or kd_tree, use leaf_size to assign the size of leaf nodes. This param impacts the construction of trees, the speed of finding nearest points and the memory of saving the tree
# random_state: deprecated

## Attributes:
# core_sample_indices_: the location of core sample in original data
# components_: core samples
# labels_: the label of every sample, -1 means noise


## Methods:
# fit()
# fit_predict()

def test_DBSCAN(*data):
  X, labels_true=data
  clst=cluster.DBSCAN()
  predicted_labels=clst.fit_predict(X)
  print("ARI:%s"% adjusted_rand_score(labels_true,predicted_labels))
  print('Core sample num:%d'%len(clst.core_sample_indices_))
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_DBSCAN(X,labels_true)

# ARI:0.3303004097727298
# Core sample num:992


# Consider the impact from epsilon
def test_DBSCAN_epsilon(*data):
  X,labels_true=data
  epsilons=np.logspace(-1,1.5)
  ARIs=[]
  Core_nums=[]
  for epsilon in epsilons:
    clst=cluster.DBSCAN(eps=epsilon)
    predicted_labels=clst.fit_predict(X)
    ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
    Core_nums.append(len(clst.core_sample_indices_))
  fig=plt.figure()
  ax=fig.add_subplot(1,2,1)
  ax.plot(epsilons,ARIs,marker='+')
  ax.set_xscale('log')
  ax.set_xlabel(r"$\epsilon$")
  ax.set_ylim(0,1)
  ax.set_ylabel('ARI')
  ax=fig.add_subplot(1,2,2)
  ax.plot(epsilons,Core_nums,marker='o')
  ax.set_xscale('log')
  ax.set_xlabel(r"$\epsilon$")
  ax.set_ylabel('Core_Nums')

  fig.suptitle("DBSCAN")
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_DBSCAN_epsilon(X,labels_true)

# when epsilon is very big, all of points in same neigborhood
# core samples will be more but get to be finally flattened 


# Consider the impact from MinPts
def test_DBSCAN_min_samples(*data):
  X,labels_true=data
  min_samples=range(1,100)
  ARIs=[]
  Core_nums=[]
  for num in min_samples:
    clst=cluster.DBSCAN(min_samples=num)
    predicted_labels=clst.fit_predict(X)
    ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
    Core_nums.append(len(clst.core_sample_indices_))
  fig=plt.figure()
  ax=fig.add_subplot(1,2,1)
  ax.plot(min_samples,ARIs,marker='+')
  ax.set_xlabel('min_samples')
  ax.set_ylim(0,1)
  ax.set_ylabel('ARI')
  ax=fig.add_subplot(1,2,2)
  ax.plot(min_samples,Core_nums,marker='o')
  ax.set_xlabel("min_samples")
  ax.set_ylabel('Core_Nums')

  fig.suptitle("DBSCAN")
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_DBSCAN_min_samples(X,labels_true)
# with the increase of MinPts, it is harder to become a core object because it requires more samples included, so the core samples are getting fewer
