from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def load_classification_data():
  digits=datasets.load_digits()
  X_train=digits.data
  y_train=digits.target
  return train_test_split(digits.data, digits.target,
                         test_size=.25, random_state=0, stratify=y_train)
                         
def create_regression_data(n):
  X = 5*np.random.rand(n,1)
  y = np.sin(X).ravel()
  y[::5] += 1*(0.5-np.random.rand(int(n/5)))
  return train_test_split(X,y,test_size=.25,random_state=0)

## KNN Classifier

sklearn.neighbors.KNeighborsClassifier()

## Params:
# n_neighbors; k
# weights: string or callable object, 'uniform': same weight for every neighbor. 'distance': the weight is 1/distance, so the closer the node is, the bigger the voting weight is ,[callable]: callable object, the array of distance
# algorithm: a string, calls for different algos. 'ball_tree': BallTree, 'kd_tree': KDTree, 'brute': brute-force search, 'auto':autoselect
# leaf_size: integer, the size of leaf nodes for BallTree or KDTree, it can impact onthe searching speed and the buildups of trees
# metric: a string, the method for calculating distance, the default is 'minkowski'
# p: integer, exponent of Minkowski, if p=1, manhattan L2 distance, if p=2, Euclidean distance L1
# n_jobs: parallization, -1 means assigning all the tasks into available CPUs

## Methods
# fit(X,y)
# predict(X)
# score(X,y)
# predict_proba(X)
# kneigbors([X, n_neighbors, return_distance]), if return_distance = True, return the distances as well
# Kneighbors_grah([X, n_neighbors, mode]): the connectivity gragh of sample X

def test_KNeighborsClassifier(data):
  X_train, X_test, y_train, y_test=data
  clf=neighbors.KNeighborsClassifier()
  clf.fit(X_train, y_train)
  print("Training Score:%f"%clf.score(X_train, y_train))
  print("Testing Score:%f"%clf.score(X_test,y_test))
  
  
test_KNeighborsClassifier(load_classification_data())

# test the impact from k and the voting strategy
def testKNN_k_w(data):
  X_train, X_test, y_train, y_test=data
  Ks = np.linspace(1, y_train.size, num=100, endpoint=False, dtype='int')
  weights=['uniform','distance']
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  for weight in weights:
    training_scores=[]
    testing_scores=[]
    for K in Ks:
      clf=neighbors.KNeighborsClassifier(weights=weight, n_neighbors=K)
      clf.fit(X_train, y_train)
      testing_scores.append(clf.score(X_test, y_test))
      training_scores.append(clf.score(X_train, y_train))
    ax.plot(Ks, testing_scores, label='testing score:weight=%s'%weight)
    ax.plot(Ks, training_scores, label="training score:weight=%s"%weight)
  ax.legend(loc='best')
  ax.set_xlabel("K")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.05)
  ax.set_title("KNeighbosClassifier")
  plt.show()

testKNN_k_w(data=load_classification_data())
# you can see, in uniform, with the increase of K, the performace is downside, this is because some instances that are far from sample x can get into the k instances
# but using distance, the impact from K is fewer than using uniform



# discuss the impact from p
def test_KNN_classifier_p(data):
  X_train, X_test, y_train, y_test=data
  Ks=np.linspace(1,y_train.size, endpoint=False,dtype='int')
  Ps=[1,2,10]
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  for P in Ps:
    training_scores=[]
    testing_scores=[]
    for K in Ks:
      clf=neighbors.KNeighborsClassifier(p=P, n_neighbors=K)
      clf.fit(X_train, y_train)
      testing_scores.append(clf.score(X_test, y_test))
      training_scores.append(clf.score(X_train, y_train))
    ax.plot(Ks, testing_scores, label='testing score:p=%d'%P)
    ax.plot(Ks, training_scores, label="training score:p=%d"%P)
  ax.legend(loc='best')
  ax.set_xlabel("K")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.05)
  ax.set_title("KNeighbosClassifier")
  plt.show()
  


test_KNN_classifier_p(data=load_classification_data())# no big impact from p





