from PIL import Image
import numpy as np
import os
from sklearn.model_selection import train_test_split
from image_utils import to_array

def load_oreilley():
    data1, label1 = to_array("keras_or_images_gr", [0,1])
    data2, label2 = to_array("keras_ng_images_gr", [1,0])
    data = np.array(data1 + data2)
    label = np.array(label1 + label2)
    return train_test_split(data, label)
