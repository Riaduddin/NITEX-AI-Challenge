import numpy as np

def data_processing(data):
    input_data = data / 255
    test=np.array(input_data).reshape((input_data.shape[0], 28, 28, 1))
    test_norm = test.astype('float32')
    return test_norm