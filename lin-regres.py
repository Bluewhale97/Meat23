#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 
#sklearn.model_selection.train_test_split
def load_data():
  diabetes = datasets.load_diabetes()
  return train_test_split(diabetes.data, diabetes.target,test_size=.25, random_state=0)


#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 
#sklearn.model_selection.train_test_split
def load_data():
  diabetes = datasets.load_diabetes()
  return train_test_split(diabetes.data, diabetes.target,test_size=.25, random_state=0)

df = load_data()

def test_LinearRegression(data):
  X_train, X_test, y_train, y_test= data
  regr = linear_model.LinearRegression()
  regr.fit(X_train, y_train)
  print("Coefficients:%s, intercept %.2f"%(regr.coef_,regr.intercept_))
  print("Residual sum of squares: %.2f"%np.mean((regr.predict(X_test) - y_test)**2))
  print('Score:%.2f'% regr.score(X_test, y_test))
 
test_LinearRegression(df)
