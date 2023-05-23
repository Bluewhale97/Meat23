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
# classsklearn.mixture.GaussianMixture()

## Params:
# n_components: for the number of sub-models, default as 1
# covariance_type: string, covariance type, 'spherical': spherical type the covar of every sub model is a fixed value. 'tied': every sub model shares a same covar matrix. 'diag': every submodel has a diagnol covar matrix. 'full': every sub model has their own
# random_state: integer or RandomState instance or None
# reg_covar: float, adding to diagnoals of covar matrix, making sure covar are positives
# tol: float for threshold of convergence
# n_init: number of initialization round, or initial mean vectors
# weights-init: a procession like (n_components,) as the initial weights
# means_init: array, (n_components, n_features), initial mean values
# precision_init: precisions as the inverse of covar, the shape depends on the covariance_type
# init_params: a string could be 'kmeans' or 'random', for strategies of initial weights
# verbose: integer, if 0 do not output log info, 1 output periodically, more than 1 prints out more frequently
# warm_start: boolean, True utilizing former results as the begining of this round
# verbose_interval: integer for the intervals of outputing logs

## Attributes:
# weights_: array, shape is (n_components,)
# means_: array, shape is (n_components, n_features)

## Methods
# fit()
# fit_predict(X)
# predict(X)
# predict_proba(X)
# sample([n_samples,random_state]): according to trained model, produce samples
# score(X,y)
# score_samples(X)


#testing GMM
def test_GMM(*data):
  X, labels_true=data
  clst=mixture.GaussianMixture()
  predicted_labels=clst.fit_predict(X)
  print("ARI:%s"% adjusted_rand_score(labels_true,predicted_labels))
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_GMM(X,labels_true)

# the default GMM only has 1 cluster, so the ARI is 0
# ARI:0.33266533066132264

# Consider the impact from number of clusters
def test_GMM_ncomponents(*data):
  X,labels_true=data
  nums=range(1,50)
  ARIs=[]
  for num in nums:
    clst=mixture.GaussianMixture(n_components=num)
    predicted_labels=clst.fit_predict(X)
    ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(nums,ARIs,marker='+')
  ax.set_xlabel('n_components')
  ax.set_ylabel('ARI')
  fig.suptitle("GMM")
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_GMM_ncomponents(X,labels_true)

# n_cluster=4, max ARI


# Consider the impact from types of covar
def test_GMM_cov_type(*data):
  X,labels_true=data
  nums=range(1,50)

  cov_types=['spherical','tied','diag','full']
  markers='+o*s'
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)

  for i,cov_type in enumerate(cov_types):
    ARIs=[]
    for num in nums:
      clst=mixture.GaussianMixture(n_components=num, covariance_type=cov_type)
      predicted_labels=clst.fit_predict(X)
      ARIs.append( adjusted_rand_score(labels_true,predicted_labels))
    ax.plot(nums,ARIs,marker=markers[i],label="covariance_type:%s"%cov_type)
  ax.set_xlabel('n_components')
  ax.set_ylabel('ARI')
  ax.legend(loc='best')
  fig.suptitle("GMM")
  plt.show()
  
  
centers=[[1,1],[2,2],[1,2],[10,20]]
X, labels_true=create_data(centers,1000,0.5)
test_GMM_cov_type(X,labels_true)
# no big difference among cov types

