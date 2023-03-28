# DecisionTreeRegressor
class sklearn.tree.DecisionTreeRegressor()

## Params
# criterion: string for the rule of splitting evaluation, the default is 'mse' mean squared error(only this one)
# splitter: string can be 'best' or 'random', to methods of split, 'best' for choosing the best splitting whereas 'random' choosing randomly
# max_features: can be integer, float or string or None, it is for considering the number of features when finding the best split. 'integer' calls for only considering features no more than max_features, 'float' calls for only considering max_features * n_features. And if the string is 'auto' or 'sqrt' or None then max_features = n_features. If 'log2', then max_features = log2(n_features)
# max_depth: integer or None, for the max depth of the tree, if None, then no limit to the tree's depth(assume every leaf node is pure, that means every leaf node only has one class, or less than size of min_samples_split), if max_leaf_nodes is non-none, ignore this param
# min_samples_split: min sample size for internal nodes
# min_samples_leaf: min sample size for leaf nodes
# max_leaf_nodes: integer or None, for the max amount of leaf nodes. If None, no limit, if not None, then ignore max_depth
# class_weight: a dictionary, dictionary list or string 'balanced' or None, assign the weights to classes. E.g. {class_label: weight}. If None, every class has weight 1, if 'balanced', the weight of every class is the 1/frequency in the sample
# random_state
# presort: bool for whether needing to sort the data in advance to get the best splitter. If True, for big dataset, it slows down the training but for smaller dataset, it makes learning faster


## Attributes:
# feature_importances: called gini importance, higher the importance, more important the feature is 
# max_features_: the concluded max_features_
# n_features_: the number of features after fit
# n_outputs_: output size after fit
# tree_: a tree object

## Methods:
# fit(X,y)
# predict(X)
# score(X,y)

# Import Required Packages
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def create_data(n):
  np.random.seed(0)
  X = 5*np.random.rand(n,1)
  y = np.sin(X).ravel()
  noise_num = (int)(n/5)
  y[::5] += 3* (.5 -np.random.rand(noise_num))# every 5 points add 1 noise
  return train_test_split(X, y, test_size=.25, random_state=1)

# test DecisionTreeRegressor
data = create_data(100000)
X_train, X_test, y_train, y_test = data
regr = DecisionTreeRegressor()
regr.fit(X_train, y_train)
print('training score:%f'%(regr.score(X_train,y_train)))
print("Tetsing score:%f"%(regr.score(X_test,y_test)))

# plotting
fig =plt.figure()
ax=fig.add_subplot(1,1,1)
X=np.arange(0.0,5.0,0.01)[:,np.newaxis]
Y=regr.predict(X)
ax.scatter(X_train, y_train, label="train sample", c='g')
ax.scatter(X_test, y_test, label="test sample", c='r')
ax.plot(X, Y, label='predict_value', linewidth=2, alpha=0.5)
ax.set_xlabel('data')
ax.set_ylabel('target')
ax.set_title("Decision Tree Regression")
ax.legend(framealpha=.5)
plt.show()

# we can see it fits very well for training dataset but bad for testing set

# test splitter as random or best
def test_dt_splitter(data):
  X_train,X_test,y_train,y_test=data
  splitters=['best','random']
  for splitter in splitters:
    regr=DecisionTreeRegressor(splitter=splitter)
    regr.fit(X_train, y_train)
    print("Splitter %s"%splitter)
    print("Training socre:%f"%(regr.score(X_train, y_train)))
    print("Testing score:%f"%(regr.score(X_test, y_test)))

test_dt_splitter(data=create_data(100))

# test the depth of tree
# deeper the tree is, more complex the model is
def test_dt_depth(data, maxdepth):
  X_train, X_test, y_train, y_test=data
  depths=np.arange(1,maxdepth)
  training_scores=[]
  testing_scores=[]
  for depth in depths:
    regr = DecisionTreeRegressor(max_depth=depth)
    regr.fit(X_train, y_train)
    training_scores.append(regr.score(X_train, y_train))
    testing_scores.append(regr.score(X_test, y_test))
  fig=plt.figure()
  ax=fig.add_subplot(1,1,1)
  ax.plot(depths, training_scores, label='training score')
  ax.plot(depths, testing_scores, label='testing score')
  ax.set_xlabel('maxdepth')
  ax.set_ylabel('score')
  ax.set_title('Decision Tree Regression')
  ax.legend(framealpha=.5)
  plt.show()
  
  test_dt_depth(data=create_data(100), maxdepth=20)

# technically, the tree's depth at maximum is log2(100) this is why it is not further splitted while max depth is bigger than 6.65
