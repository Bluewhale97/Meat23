from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, decomposition, manifold

def load_data():
  iris=datasets.load_iris()
  return iris.data,iris.target

#PCA
class sklearn.decomposition.PCA()
##params
# n_components: integer for the dimensions after deductions. If None, then n_components = min(n_samples, n_features). If 'mle', use Minka's MLE to guess the dimensions after deducations; If n_components is between 0 and 1 as a float, the dimension is the percent of original dimension
# copy: bool, False then use original data to train, and it will cover the original prediction result
# whiten: bool, True then divide the eigen vectors with n_samples*eigen values, to make sure to covriance of non-correlated output is 1

##Attributes
#components_
#explained_variance_ratio: the proportion of explained variance of every component
# mean_ : a array for the mean of every feature
# n_components_ : integer for how many elements for every component

##Methods:
# fit()
# transform(X): do dimensionality reduction
# fit_transform(X,y): train and do dimensionality reduction
# inverse_transform(X): arise dimensionality, force the data inversing back to original space


## to be noticed, decomposition.PCA based on scipy.linalg and use SVD for decomposition, so it is not good for high sparsity matrix, and big-scale data because it needs to pull all the data together to the memory 


def test_PCA(data):
  X,y=data
  pca=decomposition.PCA(n_components=None)
  pca.fit(X)
  print('explained variance ratio :%s'%str(pca.explained_variance_ratio_))
  
data=load_data()
test_PCA(data=data)



def plot_PCA(data):
  X,y=data
  pca=decomposition.PCA(n_components=2)
  pca.fit(X)
  X_r=pca.transform(X)
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  colors=((1,0,0),(0,1,0),(0,0,1),(.5,.5,0),(0,.5,.5),(.5,0,.5),(.4,.6,0),(.6,.4,0),(0,.6,.4),(.5,.3,.2),)
  for label, color in zip(np.unique(y), colors):
    position=y==label
    ax.scatter(X_r[position,0],X_r[position,1], label="target=%d"%label, color=color)
  ax.set_xlabel("X[0]")
  ax.set_ylabel("Y[0]")
  ax.legend(loc='best')
  ax.set_title("PCA")
  plt.show()
  
 

plot_PCA(data=load_data())



# incremental PCA can be used for big dataset, it load batchs of data into the memory 
class sklearn.decomposition.IncrementalPCA()

##params
#n_components: integer for number of dimensions
#batch_size: integer or None, the sample size of batchs, only used while passing fit()/partial_fit(). If None, algo will guess it:)
#copy: bool, False then directly use original dataset to train
#whiten: bool, True then divide the eigen vectors with n_samples*eigen values, to make sure to covriance of non-correlated output is 1

##attributes
#components_: the components
# explained_variance_; explained variance of every component
# explained_variance_ratio: explained variance of every component by proportion
# mean_: array, the mean value of every feature. So it updates for every time calling partial_fit()
# var_: array, the variance of every feature, it updates every time of calling partial_fit()
# n_samples_seen_: a integer for how many samples have operated, it also updates every time when calling partial_fit()

##methods
#fit(X): train the model, use batch_size samples
#partial_fit(): continue to train the model, continually use the batch_size samples
#transform(X): run to reduce dimensions
#fit_transform(): train the model and reduce dimensions
# inverse_transform(X): raise dimensions to original space




