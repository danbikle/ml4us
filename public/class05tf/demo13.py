# demo13.py

# This script should help me study ...
# https://www.tensorflow.org/versions/r0.11/get_started/index.html
# Demo:
# ~/anaconda3/bin/python demo13.py

import tensorflow as tf
import numpy      as np

# Create phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(5).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the mean squared errors.
loss      = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train     = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.initialize_all_variables()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# I should create lists to collect artifacts of optimizer:
w_l = []
b_l = []
l_l = []

import pdb
# Fit the line.
for step in range(9):
    tf_W = sess.run(W)
    tf_b = sess.run(b)
    tf_y = sess.run(y)
    tf_loss = sess.run(loss)
    w_l.append(tf_W[0])
    b_l.append(tf_b[0])
    l_l.append(tf_loss)
    # Now I should change W,b:
    sess.run(train)


# I should create lists to collect artifacts of optimizer:
dw_l = []
db_l = []
dl_l = []
for i_i in range(len(w_l)-1):
  dw_l.append(w_l[i_i+1]-w_l[i_i])
  db_l.append(b_l[i_i+1]-b_l[i_i])
  dl_l.append(l_l[i_i+1]   -l_l[i_i])
# I should collect dL/dW, dL/db:
gw_a = np.array(dl_l)/np.array(dw_l)
gb_a = np.array(dl_l)/np.array(db_l)

# I should plot w_l:
import matplotlib
import matplotlib.pyplot as plt
plt.plot(range(len(w_l)),w_l)
#plt.show()

# I should plot b_l:
plt.plot(range(len(b_l)),b_l)
plt.grid(True)
plt.show()
plt.close()

# I should plot l_l:
plt.plot(range(len(l_l)),l_l)
plt.grid(True)
plt.show()
plt.close()

'bye'
