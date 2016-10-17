# ~/ml4us/public/class06/keras10.py

# This script should demo keras.

# Demo:
# ~/anaconda3/bin/python keras10.py

# Ref:
# https://github.com/fchollet/keras#getting-started-30-seconds-to-keras

from keras.models import Sequential

model = Sequential()

# Stacking layers is as easy as .add():

from keras.layers import Dense, Activation

model.add(Dense(output_dim=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(output_dim=10))
model.add(Activation("softmax"))

# Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])


