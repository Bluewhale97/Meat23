sklean.tree.DecisionTreeClassifier

## Parameters
# criterion: string for evaluation metrics 'gini' or 'entropy'
# splitter: string for splitting rule, either 'best', or 'random'
# max_features: integer for the # of max features, float calls for max_features*n_features, 'auto' or 'sqrt' then max_features=sqrt(n_features). log2 then max_features = log2(n_features), None then max_features = n_features
# max_depth: integer or None, None means unlimited depth. If the max_leaf_nodes is non-none, ignore max_depth
# min_samples_split: minimum sample size of every splitting node
# min_samples_leaf: integer, minimum sample size of every leaf node
# min_weight_fraction_leaf: minimum weight for every sample in leaf node
# max_leaf_nodes: integer or None, for the max number of leaf nodes, None means unlimited, if not None, max_depth will be ignored
# class_weight: dict, dict list or string, or None, None means every class weigh 1, 'balanced' means every class is frequency/total. If sample_weight provides weight, then these weights are all going to multiply with sample_weight
# random_state
# presort: bool for early sorting, True slows down the training for big set, but faster for smaller dataset

## Attributes
# classes_:label value of classes
# feature_importances_: gini importance
# max_features_:concluded max_features
# n_classes_: the number of classes
# n_features_: fit features
# n_outputs_: output 
# tree_: tree object

## Methods:
# fit(X,y)
# predict(X)
# predict_log_proba(X)
# predict_proba(X)
# score(X,y)

# import packages
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

def load_data():
  iris=datasets.load_iris()
  X_train=iris.data
  y_train=iris.target
  return train_test_split(X_train, y_train, test_size=.25, random_state=0, stratify=y_train)

def test_dtClassifier(data):
  X_train, X_test, y_train, y_test=data
  clf=DecisionTreeClassifier()
  clf.fit(X_train, y_train)
  
  print("training score:%f"%(clf.score(X_train, y_train)))
  print("testing score:%f"%(clf.score(X_test, y_test)))
  
test_dtClassifier(data=load_data())

# testing impact from different criterions
def test_dt_criterion(data):
  X_train, X_test, y_train, y_test=data
  criterions=['gini','entropy']
  for criterion in criterions:
    clf = DecisionTreeClassifier(criterion=criterion)
    clf.fit(X_train, y_train)
    print("cirterion:%s"%criterion)
    print("training score:%f"%(clf.score(X_train, y_train)))
    print("testing score:%f"%(clf.score(X_test,y_test)))
    
    
test_dt_criterion(data=load_data())

# testing the splitter
def test_dt_splitter(data):
  X_train, X_test, y_train, y_test=data
  splitters =['best','random']
  for splitter in splitters:
    clf = DecisionTreeClassifier(splitter=splitter)
    clf.fit(X_train, y_train)
    print("splitter:%s"%splitter)
    print("training score:%f"%(clf.score(X_train, y_train)))
    print("testing score:%f"%(clf.score(X_test,y_test)))
    
test_dt_splitter(data=load_data())

# testing the impact from max depth
def test_dt_depth(data,maxdepth):
  X_train, X_test, y_train, y_test=data
  depths=np.arange(1,maxdepth)
  training_scores=[]
  testing_scores=[]
  for depth in depths:
    clf = DecisionTreeClassifier(max_depth=depth)
    clf.fit(X_train, y_train)
    training_scores.append(clf.score(X_train,y_train))
    testing_scores.append(clf.score(X_test,y_test))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(depths, training_scores, label='training score',marker='o')
  ax.plot(depths, testing_scores, label='testing score', marker='*')
  ax.set_xlabel('maxdepth')
  ax.set_ylabel('score')
  ax.set_title("Decision Tree Classification")
  ax.legend(framealpha=.5, loc='best')
  plt.show()
  
  
test_dt_depth(data=load_data(), maxdepth=10)

