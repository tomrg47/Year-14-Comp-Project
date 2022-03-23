from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

#load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') #training
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')#testing
print(dftrain.head())
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')



