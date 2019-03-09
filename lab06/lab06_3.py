'''
This module prints information about the Boston Housing Price dataset.

@author: slg27
@date: March 9, 2019
'''

import numpy as np
from keras.datasets import boston_housing

(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()

# part 1 - Print the number of training and testing examples
print(f'number of training data examples: {len(train_data)}',
      f'number of testing data examples: {len(test_labels)}')

# part 2 - Print the rank (i.e., number of axes/dimensions), shape and data type of the examples
print(
    f'training data \
        \n\tdimensions: {train_data.ndim} \
        \n\tshape: {train_data.shape} \
        \n\tdata type: {train_data.dtype}\n\n',
    f'testing data \
        \n\tdimensions: {test_labels.ndim} \
        \n\tshape: {test_labels.shape} \
        \n\tdata type: {test_labels.dtype}\n',
)
