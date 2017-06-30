"""
# demo13.py

# This script should help me visualize behavior of optimizer.minimize(loss)
# Ref:
# http://ml4.us/cclasses/class05tf18

# Demo:
# ~/anaconda3/bin/python demo13.py
"""

import tensorflow as tf
import numpy      as np

# Create phony x, y data points in NumPy, y = x * 0.1 + 0.3 + noise
pts_i   = 20
noise_a = 0.05*np.random.rand(pts_i) # Notice this.
x_data  = np.random.rand(pts_i).astype(np.float32)
y_data  = x_data * 0.1 + 0.3 + noise_a

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
# I should visualize behavior of above call.

# Before starting, initialize the variables.  We will 'run' this first.
#init = tf.initialize_all_variables()
init  = tf.global_variables_initializer() # better than above line.

# Launch the graph.
sess = tf.Session()
sess.run(init)

# I should create lists to collect artifacts of optimizer:
w_l = []
b_l = []
l_l = []

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
print('I calculate W to be: '+str(tf_W))
print('I calculate b to be: '+str(tf_b))
print('yhat is '+str(tf_W[0])+' * x_data +'+str(tf_b[0]))

# I should create lists to collect artifacts of optimizer:
dw_l = []
db_l = []
dl_l = []
for i_i in range(len(w_l)-1):
  dw_l.append(w_l[i_i+1]-w_l[i_i])
  db_l.append(b_l[i_i+1]-b_l[i_i])
  dl_l.append(l_l[i_i+1]-l_l[i_i])
# I should make dw_l, db_l, dl_l same length as w_l
dw_l.append(0.0)
db_l.append(0.0)
dl_l.append(0.0)
# I should collect dL/dW, dL/db:
gw_a = np.array(dl_l)/np.array(dw_l)
gb_a = np.array(dl_l)/np.array(db_l)
gw_l = gw_a.tolist()
gb_l = gb_a.tolist()

import pandas as pd
opt_d           = {'W':w_l}
opt_df          = pd.DataFrame(opt_d)
opt_df['b']     = b_l
opt_df['loss']  = l_l
opt_df['dw']    = dw_l
opt_df['db']    = db_l
opt_df['dL']    = dl_l
opt_df['dL/dw'] = gw_l
opt_df['dL/db'] = gb_l

# I should plot artifacts of optimizer:
import matplotlib
matplotlib.use('Agg')
# Order is important here.
# Do not move the next import:
import matplotlib.pyplot as plt
plt.figure(figsize=(9,6))

opt_df[['W','b']].plot.line(title="W,b vs calls to optimizer")
plt.grid(True)
plt.savefig('w.png')
plt.close()

opt_df[1:].loss.plot.line(title="loss vs calls to optimizer")
plt.savefig('loss.png')
plt.close()

opt_df[['dw','db']].plot.line(title="dW,db vs calls to optimizer")
plt.grid(True)
plt.savefig('dwdb.png')
plt.close()

opt_df[['dL/dw','dL/db']].plot.line(title="dL/dW,dL/db vs calls to optimizer")
plt.grid(True)
plt.savefig('dldwdb.png')
plt.close()

# I should plot y_data vs x_data
plt.scatter(x_data,y_data,c='b')
# I should plot yhat too:
yhat_a = tf_W * x_data + tf_b
plt.plot(x_data,yhat_a,c='g')
plt.title('y_data vs x_data (blue) and yhat vs x_data (green)')
plt.grid(True)
plt.savefig('yvsx.png')
plt.close()

'bye'
