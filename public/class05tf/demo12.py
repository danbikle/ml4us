# demo12.py

# This script should help me study ...
# https://www.tensorflow.org/versions/r0.11/get_started/index.html

import tensorflow as tf
import numpy      as np

# Create phony x, y data points in NumPy, y = x * 0.1 + 0.3
x_data = np.random.rand(5).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
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

import pdb

x_data
y_data
tf_W = sess.run(W)
tf_b = sess.run(b)
tf_y = sess.run(y)
tf_loss = sess.run(loss)

def my_loss(y0_a, y1_a):
    diff_a = y0_a - y1_a
    sq_a   = [e_f*e_f for e_f in diff_a]
    return np.mean(sq_a)
print('my_loss:')
print(my_loss(y_data,tf_y))

print('tf_loss:')
print(tf_loss)

# I should create lists to collect artifacts of optimizer:
w_l = []
b_l = []
l_l = []

# Fit the line.
for step in range(5):
    sess.run(train)
    tf_W = sess.run(W)
    tf_b = sess.run(b)
    tf_y = sess.run(y)
    tf_loss = sess.run(loss)
    w_l.append(tf_W)
    b_l.append(tf_b)
    l_l.append(tf_loss)
print('W:')
print([f_f[0] for f_f in w_l])
print('b:')
print([f_f[0] for f_f in b_l])
print('loss:')
print(l_l)

# I should create lists to collect artifacts of optimizer:
dw_l = []
db_l = []
dl_l = []
for i_i in range(len(w_l)-1):
  print(i_i)
  dw_l.append(w_l[i_i+1][0]-w_l[i_i][0])
  db_l.append(b_l[i_i+1][0]-b_l[i_i][0])
  dl_l.append(l_l[i_i+1]   -l_l[i_i])
print(dw_l)
print(db_l)
print(dl_l)
gw_a = np.array(dl_l)/np.array(dw_l)
gb_a = np.array(dl_l)/np.array(db_l)
print(gw_a)
print(gb_a)

'bye'
