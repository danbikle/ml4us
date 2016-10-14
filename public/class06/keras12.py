# keras12.py

# ref:
# http://blog.fastforwardlabs.com/post/139921712388/hello-world-in-keras-or-scikit-learn-versus

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.utils import np_utils

iris = sns.load_dataset("iris")
#sns.pairplot(iris, hue='species')
#plt.show()
X = iris.values[:, 0:4]
y = iris.values[:, 4]

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.5, random_state=0)

def one_hot_encode_object_array(arr):
  '''One hot encode a numpy array of objects (e.g. strings)'''
  uniques, ids = np.unique(arr, return_inverse=True)
  return np_utils.to_categorical(ids, len(uniques))

train_y_ohe = one_hot_encode_object_array(train_y)
test_y_ohe  = one_hot_encode_object_array(test_y)
model = Sequential()
model.add(Dense(4, input_shape=(4,)))
model.add(Activation('sigmoid'))
model.add(Dense(3))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(train_X, train_y_ohe, verbose=0, batch_size=1)

accuracy = model.evaluate(test_X, test_y_ohe, verbose=0)
print('accuracy:')
print(accuracy)

'bye'
