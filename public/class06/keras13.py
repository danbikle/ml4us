# keras13.py

# This script should classify data from observations of flowers.
# The classes of flowers are: setosa, virginica, versicolor
# ref:
# http://blog.fastforwardlabs.com/post/139921712388/hello-world-in-keras-or-scikit-learn-versus
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

# Demo:
# ./keras_theano.bash keras13.py

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

iris = sns.load_dataset("iris")
# I should use sns to visualize the features:
#sns.pairplot(iris, hue='species')
#plt.show()

X = iris.values[:, 0:4]
y = iris.values[:, 4]

# I should one-hot-encode setosa, virginica, versicolor:
y_l = []
for y_s in y:
  if y_s == 'setosa':
    y_l.append([1,0,0])
  elif y_s == 'virginica':
    y_l.append([0,1,0])
  else:
    y_l.append([0,0,1])
# I should split the data into train-data and test-data:    
train_X, test_X, train_y, test_y = train_test_split(X, y_l, train_size=0.5, random_state=0)

# I should use Keras API to create a neural network model:
model = Sequential()
model.add(Dense(4, input_shape=(4,)))
model.add(Activation('sigmoid'))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(train_X, train_y, verbose=0, batch_size=1)

accuracy = model.evaluate(test_X, test_y, verbose=0)
print('accuracy:')
print(accuracy)

print(model.predict(train_X[:4]))
print(train_y[:4])
print(model.predict(test_X[:5]))
print(test_y[:5])

'bye'
