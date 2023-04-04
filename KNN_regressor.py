from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def create_regression_data(n):
  X = 5*np.random.rand(n,1)
  y = np.sin(X).ravel()
  y[::5] += 1*(0.5-np.random.rand(int(n/5)))
  return train_test_split(X,y,test_size=.25,random_state=0)

## KNN Classifier

sklearn.neighbors.KNeighborsRegressor()

##Params
# n_neighbors: k
# weights: a string or a callable object. "uniform": the votings are the same for every neighbor. "dsitance": the voting weights = 1/distance, [callable]: input the distances of every neighbor
# algorithm: a string, 'ball_tree', 'kd_tree','brute' or 'auto'
# leaf_size: a integer about the size of leaf nodes, BallTree or KDTree only
# metric: string for the measure of distance, default is 'minkowski'
# p: the exponent on 'Minkowski'. If p=1, L2 manhattan otherwise L1 Euclidean
# n_jobs: integer for parallization, -1 means assigning jobs into all the CPUs

##Methods
# fit(X,y)
# predict(X)
# score(X,y)
# kneighbors([X, n_neighbors. return_distance]), return the distances while return_distance=True
# kneighbors_graph([X, n_neighbors, mode]), the connectivity gragh of the sample


def test_KNN_reg(data):
  X_train, X_test, y_train, y_test=data
  regr=neighbors.KNeighborsRegressor()
  regr.fit(X_train, y_train)
  print("Training Score:%f"%regr.score(X_train, y_train))
  print("Testing Score:%f"%regr.score(X_test, y_test))
  
test_KNN_reg(data=create_regression_data(1000))

# test the impact from k and w(voting strategies)
def test_KNN_reg_k_w(data):
  X_train, X_test, y_train, y_test=data
  Ks=np.linspace(1,y_train.size,num=100,endpoint=False, dtype='int')
  weights=['uniform','distance']
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  for weight in weights:
    training_scores=[]
    testing_scores=[]
    for K in Ks:
      regr=neighbors.KNeighborsRegressor(weights=weight,n_neighbors=K)
      regr.fit(X_train, y_train)
      testing_scores.append(regr.score(X_test,y_test))
      training_scores.append(regr.score(X_train,y_train))
    ax.plot(Ks, testing_scores, label='testing score:weight=%s'%weight)
    ax.plot(Ks, training_scores, label='training score:weight=%s'%weight)
  ax.legend(loc='best')
  ax.set_xlabel("K")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.05)
  ax.set_title("KNeighborsRegressor")
  plt.show()
 

test_KNN_reg_k_w(data=create_regression_data(1000))


# testing the impact from p
def test_KNN_reg_p(data):
  X_train, X_test, y_train, y_test=data
  Ks=np.linspace(1,y_train.size,num=100,endpoint=False, dtype='int')
  Ps=[1,2,10]
  
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  for P in Ps:
    training_scores=[]
    testing_scores=[]
    for K in Ks:
      regr=neighbors.KNeighborsRegressor(p=P,n_neighbors=K)
      regr.fit(X_train, y_train)
      testing_scores.append(regr.score(X_test,y_test))
      training_scores.append(regr.score(X_train,y_train))
    ax.plot(Ks, testing_scores, label='testing score:p=%s'%P)
    ax.plot(Ks, training_scores, label='training score:p=%s'%P)
  ax.legend(loc='best')
  ax.set_xlabel("K")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.05)
  ax.set_title("KNeighborsRegressor")
  plt.show()
  

 test_KNN_reg_p(data=create_regression_data(1000))
