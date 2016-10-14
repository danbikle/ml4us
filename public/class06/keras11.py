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

c1_df = iris1_df.copy()[(iris1_df.label == 'Iris-setosa'    )]
c2_df = iris1_df.copy()[(iris1_df.label == 'Iris-versicolor')]
c3_df = iris1_df.copy()[(iris1_df.label == 'Iris-virginica' )]

# I should change the label from a string to an integer:

c1_df['label'] = 1
c2_df['label'] = 2
c3_df['label'] = 3

iris2_df = pd.concat([c1_df,c2_df,c3_df])

X_train = iris2_df[['f1','f2','f3','f4']]

# from keras.utils import np_utils
# Y_train = np_utils.to_categorical(iris2_df.label,nb_classes=3)
y_l = []
for y_i in iris2_df.label:
    if y_i == 1:
        y_l.append([1,0,0])
    elif y_i == 2:
        y_l.append([0,1,0])
    else:
        y_l.append([0,0,1])

        
pdb.set_trace()
Y_train= np.array(y_l)
#model.fit(X_train, Y_train, nb_epoch=5, batch_size=32)

'bye'
