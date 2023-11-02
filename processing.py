import numpy as np

def data_processing(data):
    """preprocessing the data
        return the data reshape (28,28,1)
    """
    #ranging all value 0 to 1
    input_data = data / 255

    #reshape
    test=np.array(input_data).reshape((input_data.shape[0], 28, 28, 1))
    test_norm = test.astype('float32')
    
    return test_norm