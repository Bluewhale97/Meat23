# import libaries 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import cluster
from sklearn.metrics import adjusted_rand_score
from sklearn import mixture

# K means clustering
# class sklearn.cluster.KMeans()

#Params:
# n_clusters: the number of clusters
# init: a string for strategies of initial mean vector, 'k-means++': choosing means far from each other, 'random': randomly pick K samples as mean vector. Or provide an array=(n_clusters.n_features). Basically k means can always be converged, but the degree of convergence highly depends on the initial mean vector, sometimes it can be converged into local optimum. So generally use multiple different mean vectors and choose the best one, so mean initialization can solve the problem of convergence to some degree
# n_init: integer, iteration times of k means, every time chooses a different mean vector, the algo will choose the best one to return
# max_iter: every round, the max iteration, so the total iteration is max_iter*n_init
# precompute_distances: a string or boolean, for whether compute sample distance in advance, it requires more memory but the algo runs faster. 'auto': n_samples*n_clusters > 12 million then do not compute in advance. True: compute early, False: always not compute early
# tol: a float for the threshold of convergence
# n_jobs: positive float for the number of CPUs, -1 means using all of available CPU
# verbose: an integer if 0 then do not output log info, 1 then print out the log info periodically, if more than 1 then print out more frequently
# random_state: integer or an instance of RandomState or None. If integer, then it has designated seed, if instance then assign the generator, if None then use the default generator
# copy_x: boolean, for precompute_distances=True, if True, then when precomputing distances, do not change the original data, False change the original data to save memory. When algo ends, return original data but it may have some precision errors because of float 

#Attributes:
# cluster_centers_: provide the mean vector
# labels_: gives the label of each sample, for which the sample belongs to
# inertia_: provide the sum of distance of each sample from its closest cluster

#Methods:
#fit()
#fit_predict(X): equals to call the fit method then call predict method
#predict(x): directly predict
#score(): return the score of the model

# create a function to make data
# centers: array for centroids, e.g. [[1,1],[2,2],[10,20]]
# num: sample size
# std: standard deviation of each cluster

# this func returns clusters of Gaussian distribution
def create_data(centers, num=100, std=.7):
  X, labels_true = make_blobs(n_samples=num, centers=centers, cluster_std=std)
  return X, labels_true



def test_Kmeans(*data):
  X, labels_true=data
  clst=cluster.KMeans()
  clst.fit(X)
  predicted_labels=clst.predict(X)
  print("APR:%s"% adjusted_rand_score(labels_true, predicted_labels))
  print("Sum center distance %s"%clst.inertia_)
  
  
# call test_Kmeans()
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_Kmeans(X,labels_true)
# APR:0.36627378787377785
# Sum center distance 236.56867382446345


# now consider the impact from the number of clusters
def test_Kmeans_nclusters(*data):
  X, labels_true = data
  nums=range(1,50)
  ARIs=[]
  Distances=[]
  for num in nums:
    clst=cluster.KMeans(n_clusters=num)
    clst.fit(X)
    predicted_labels=clst.predict(X)
    ARIs.append(adjusted_rand_score(labels_true, predicted_labels))
    Distances.append(clst.inertia_)
  fig=plt.figure()
  ax=fig.add_subplot(1,2,1)
  ax.plot(nums, ARIs, marker='+')
  ax.set_xlabel('n_clusters')
  ax.set_ylabel('ARI')
  ax=fig.add_subplot(1,2,2)
  ax.plot(nums, Distances, marker='o')
  ax.set_xlabel('n_cluster')
  ax.set_ylabel('inertia_')
  fig.suptitle('KMeans')
  plt.show()
  
  
  
# call test_Kmeans_nclusters
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_Kmeans_nclusters(X,labels_true)
# when n_cluster=4, ARI is the biggest
# when n_cluster=1, inertia_ is the biggest


# Consider the impact from the times of running(iteration rounds) and the strategies of initial mean vectors
def test_Kmeans_n_init(*data):
  X, labels_true=data
  nums=range(1,50)
  fig=plt.figure()
  ARIs_k=[]
  Distances_k=[]
  ARIs_r=[]
  Distances_r=[]
  for num in nums:
    clst=cluster.KMeans(n_init=num,init='k-means++')
    clst.fit(X)
    predicted_labels=clst.predict(X)
    ARIs_k.append(adjusted_rand_score(labels_true,predicted_labels))
    Distances_k.append(clst.inertia_)

    clst=cluster.KMeans(n_init=num,init='random')
    clst.fit(X)
    predicted_labels=clst.predict(X)
    ARIs_r.append(adjusted_rand_score(labels_true,predicted_labels))
    Distances_r.append(clst.inertia_)
  
  ax=fig.add_subplot(1,2,1)
  ax.plot(nums,ARIs_k,marker='+',label='K-means++')
  ax.plot(nums,ARIs_r,marker='+',label='random')
  ax.set_xlabel('n_init')
  ax.set_ylabel('ARI')
  ax.set_ylim(0,1)
  ax.legend(loc='best')
  ax=fig.add_subplot(1,2,2)
  ax.plot(nums,Distances_k,marker='o',label='K-means++')
  ax.plot(nums,Distances_r,marker='o',label='random')
  ax.set_xlabel('n_init')
  ax.set_ylabel('inertia_')
  ax.legend(loc='best')

  fig.suptitle('KMeans')
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_Kmeans_n_init(X,labels_true)
# highly dependent on o_init
# so k means++ and random has almost same impact




