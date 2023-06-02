from sklearn import datasets, naive_bayes
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# digit datasets, 1797 samples, every image is 8x8 hand-written digit
# use sklearn to convert the image into 64-dimension vectors

def show_digits():
  digits = datasets.load_digits()
  fig=plt.figure()
  print("vector from images 0:", digits.data[0])
  for i in range(25):
    ax=fig.add_subplot(5,5,i+1)
    ax.imshow(digits.images[i], cmap=plt.cm.gray_r, interpolation='nearest')
  plt.show()
  
  
show_digits()

def load_data():
  digits=datasets.load_digits()
  return train_test_split(digits.data, digits.target,
                         test_size=.25, random_state=0)


## BernoulliNB

sklearn.naive_bayes.BernoulliNB

## Params:
# alpha: the alpha value, can be float, for laplacian smoothing
# binarize: float or NOne, if None, means that the original data is already binarized, if Float, then this float value is being as the bound, more than it as 1, less than it as 0
# fit_prior: bool. True then do not go to learn P(y=ck). Flase, go to learn P(y=ck)
# class_prior: assign the prior proba for every class.


## Attributes:
# class_log_prior_: an array for log value of prior_prob of every class
# feature_log_prob_: an array, (n_classes, n_features), the prior_prob of every feature on every class
# class_count_: an array, (n_classes,), the number of samples in each class
# feature_count_: the sample size of every feature on every class

## Methods:
# fit(X,y)
# partial_fit(X,y): for big dataset, like mini-batch
# predict(X)
# predict_log_proba(X)
# predict_proba(X)
# score(X,y)


def test_BernoulliNB(data):
  X_train, X_test, y_train, y_test=data
  cls=naive_bayes.BernoulliNB()
  cls.fit(X_train, y_train)
  print("Training Score:%.2f"%cls.score(X_train,y_train))
  print("Testing Score:%.2f"%cls.score(X_test,y_test))
  
test_BernoulliNB(data=load_data())

# test the impact from different alpha
def test_BernoulliNB_alpha(data):
  X_train, X_test, y_train, y_test=data
  alphas=np.logspace(-2,5,num=200)
  train_scores=[]
  test_scores=[]
  for alpha in alphas:
    cls=naive_bayes.BernoulliNB(alpha=alpha)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test,y_test))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(alphas,train_scores,label="Training_score")
  ax.plot(alphas,test_scores, label="Testing_score")
  ax.set_xlabel(r"$\alpha$")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.0)
  ax.set_title("BernoulliNB")
  ax.set_xscale("log")
  plt.show()
  
test_BernoulliNB_alpha(data=load_data())

# test the impact from binarized params
def test_BernoulliNB_binarize(data):
  X_train, X_test, y_train, y_test=data
  min_x=min(np.min(X_train.ravel()), np.min(X_test.ravel()))-0.1
  max_x=max(np.max(X_train.ravel()), np.max(X_test.ravel()))-0.1
  binarizes = np.linspace(min_x,max_x,endpoint=True,num=100)
  train_scores=[]
  test_scores=[]
  for binarize in binarizes:
    cls=naive_bayes.BernoulliNB(binarize=binarize)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test,y_test))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(binarizes,train_scores,label="Training_score")
  ax.plot(binarizes,test_scores, label="Testing_score")
  ax.set_xlabel("binarize")
  ax.set_ylabel("score")
  ax.set_ylim(0,1.0)
  ax.set_title("BernoulliNB")
  ax.legend("best")
  plt.show()

  
test_BernoulliNB_binarize(data=load_data())

# set the binarize as (max+min)/2, generally
