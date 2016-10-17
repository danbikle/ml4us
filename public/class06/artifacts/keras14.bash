#!/bin/bash

./keras_theano.bash keras14.py

# ref:
# https://github.com/transcranial/keras-js#usage
python encoder.py model.hdf5

exit
