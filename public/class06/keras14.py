# keras14.py

# This script should classify observations of S&P500 one-day percent gain.
# The two classes are above average and below average.
# Demo:
# ./keras_theano.bash keras14.py

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
import numpy  as np
import pdb
