# ~/ml4us/public/class06/keras11.py

# This script should demo keras.

# Demo:
# ~/anaconda3/bin/python keras10.py

# Ref:
# https://github.com/fchollet/keras#getting-started-30-seconds-to-keras
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/

from keras.models import Sequential

model = Sequential()

# Stacking layers is as easy as .add():

from keras.layers import Dense, Activation

model.add(Dense(output_dim=4, input_dim=4))
model.add(Activation("relu"))
model.add(Dense(output_dim=3))
model.add(Activation("softmax"))

# Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# I should read the CSV file:
import pandas as pd
import numpy  as np
import pdb
iris1_df = pd.read_csv('iris.csv', header=None, names=['f1','f2','f3','f4','label'])

c1_df = iris1_df.copy()[(iris1_df.label == 'Iris-setosa')]
c2_df = iris1_df.copy()[(iris1_df.label == 'Iris-versicolor')]
c3_df = iris1_df.copy()[(iris1_df.label == 'Iris-virginica')]

# I should change the label from a string to an integer:
c1_df['label'] = 1
c2_df['label'] = 2
c3_df['label'] = 3
iris2_df = pd.concat([c1_df,c2_df,c3_df])
print(iris2_df.head())
print(iris2_df.tail())

'bye'
