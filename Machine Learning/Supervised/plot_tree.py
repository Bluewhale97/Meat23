#pip install graphviz

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


from sklearn import tree
X_train, X_test, y_train, y_test=load_data()
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

plt.figure(figsize=[100,100])
tree.plot_tree(clf)
plt.savefig('tree',format='png',bbox_inches = 'tight',dpi = 100)
