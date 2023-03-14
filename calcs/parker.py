import pandas as pd
import matplotlib as plt
import numpy as np
<<<<<<< HEAD
from zlib import crc32
=======
>>>>>>> ff41db6 (Moving functions to a library)


# Function that makes a dataset of randoms
def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
 
<<<<<<< HEAD

# Function that makes a dataset of randoms
=======
 
>>>>>>> ff41db6 (Moving functions to a library)
def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32


<<<<<<< HEAD
# Function that makes a dataset of randoms
def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


# Function that makes a sctter matrix plot
def scatter_matrix(data):
    pd.plotting.scatter_matrix(data, alpha=0.2, figsize=(12, 12), diagonal='kde')
    plt.show()
=======
def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]
>>>>>>> ff41db6 (Moving functions to a library)
