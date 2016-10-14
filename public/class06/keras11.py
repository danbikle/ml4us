# ~/ml4us/public/class06/keras11.py

# This script should demo keras.

# Demo:
# ~/anaconda3/bin/python keras10.py

# Ref:
# https://github.com/fchollet/keras#getting-started-30-seconds-to-keras
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
import pdb

from keras.models import Sequential

model = Sequential()

# Stacking layers is as easy as .add():

from keras.layers import Dense, Activation

model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
model.add(Dense(3, init='normal', activation='sigmoid'))

# Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# I should read the CSV file:
import pandas as pd
import numpy  as np

iris1_df = pd.read_csv('iris.csv', header=None, names=['f1','f2','f3','f4','label'])
X_train  = iris1_df[['f1','f2','f3','f4']]
y_l = []
for y_s in iris1_df.label:
    if y_s == 'Iris-setosa':
        y_l.append([1,0,0])
    elif y_s == 'Iris-versicolor':
        y_l.append([0,1,0])
    else:
        y_l.append([0,0,1])

Y_train = np.array(y_l)

# Line below fails:
# *** IndexError: indices are out-of-bounds
model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)

'bye'
