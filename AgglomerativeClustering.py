# import libaries 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture

# this func returns clusters of Gaussian distribution
def create_data(centers, num=100, std=.7):
  X, labels_true = make_blobs(n_samples=num, centers=centers, cluster_std=std)
  return X, labels_true


# AgglomerativeClustering
# class sklearn.cluster.AgglomerativeClustering()

## Params:
# n_clusters: number of clusters
# connectivity: an array or callable or None 
# affinity: a string or a callable, for computing distance. It could be 'euclidean', 'l1', 'l2', 'manhattan', 'cosine', 'preconputed'. If linkage='ward' then affinity must be 'euclidean'
# memory: by default, do not save the result in memory
# n_components: deprecated
# compute_full_tree: if True, then create a complete tree after training n_clusters
# linkage: 'ward' for single-linkage, using dmin. 'complete' using complete-linkage, using dmax and 'average' using average-linkage, davd
# pooling_func: a callble, it should be values of features

## Attributes:
# labels_: labels of samples
# n_leaves_: the number of leaf nodes on each layer
# n_components_: the estimated value of connectivity
# children_: the number of child nodes of non-leaf nodes

## Methods
# fit()
# fit_predict(X)


#testing AgglomerativeClustering
def test_agg(*data):
  X, labels_true=data
  clst=cluster.AgglomerativeClustering()
  predicted_labels=clst.fit_predict(X)
  print("ARI:%s"% adjusted_rand_score(labels_true,predicted_labels))
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_agg(X,labels_true)

# ARI:0.33266533066132264

# Consider the impact from number of clusters
def test_agg_nclusters(*data):
  X,labels_true=data
  nums=range(1,50)
  ARIs=[]
  for num in nums:
    clst=cluster.AgglomerativeClustering(n_clusters=num)
    predicted_labels=clst.fit_predict(X)
    ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(nums,ARIs,marker='+')
  ax.set_xlabel('n_clusters')
  ax.set_ylabel('ARI')
  fig.suptitle("agg_n_clusters")
  plt.show()
  

centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_agg_nclusters(X,labels_true)

# n_cluster=4, max ARI


# Consider the impact from the methods of linkage
def test_agg_linkage(*data):
  X,labels_true=data
  nums=range(1,50)
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  linkages=['ward','complete','average']
  markers="+o*"

  for i,linkage in enumerate(linkages):
    ARIs=[]
    for num in nums:
      clst=cluster.AgglomerativeClustering(n_clusters=num, linkage=linkage)
      predicted_labels=clst.fit_predict(X)
      ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
    ax.plot(nums,ARIs,marker=markers[i],label="linkage:%s"%linkage)
  ax.set_xlabel('n_clusters')
  ax.set_ylabel('ARI')
  ax.legend(loc='best')
  fig.suptitle("agg_linkage")
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_agg_linkage(X,labels_true)
# ward has biggest cap, the number of clusters happened to be the actual number of clusters
