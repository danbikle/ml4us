"""
demo11.py

This script should compare TensorFlow to scikit-learn
Ref:
http://ml4.us/cclasses/class05tf13

Demo:
python demo11.py
"""

import tensorflow as tf
import numpy as np

# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
#init = tf.initialize_all_variables()
init  = tf.global_variables_initializer() # better than above line.

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# Learns best fit is W: [0.1], b: [0.3]
print('TensorFlow calculates W to be:')
print(sess.run(W))
print('TensorFlow calculates b to be:')
print(sess.run(b))

# I should use scikit-learn to fit a line to x_data and y_data.

# Start by reshaping x_data to have rows and one column:
x_data1col_a = x_data.reshape((len(x_data) ,1))

# I should use the scikit-learn API now:
from sklearn import linear_model
linr_model = linear_model.LinearRegression()
linr_model.fit(x_data1col_a, y_data)
# That was easy. I needed only 3 lines of syntax.

print('scikit-learn calculates W to be:')
print(linr_model.coef_[0])
print('scikit-learn calculates b to be:')
print(linr_model.intercept_)

'bye'
