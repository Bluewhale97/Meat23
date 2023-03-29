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

# GaussianNB

## Params
# gaussianNB does not have parameters

## Attributes
# class_prior_: the proba of every class
# class_count_: the sample size of every class
# theta_: an array (n_classes, n_features), the miu uk for every feature on every class
# sigma_: an array (n_classes, n_features), the std of every feature on every class

## Methods
# fit(X,y)
# partial_fit(X,y): for big dataset, split the dataset into subdataset
# predict(X): return predicted value
# predict_log_proba(X): return an array for log value of every class
# predict_proba(X): return the accuracy of (X,y)


# test gaussian classifier
def test_Gaussian(data):
  X_train, X_test, y_train, y_test=data
  cls=naive_bayes.GaussianNB()
  cls.fit(X_train, y_train)
  print('Training Score:%.2f'%cls.score(X_train, y_train))
  print('Testing score:%.2f'%cls.score(X_test, y_test))
  
test_Gaussian(data=load_data())

