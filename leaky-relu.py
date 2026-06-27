import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    """ Write code here
    shape = np.shape(x)
    np_arr = np.array(x,dtype=float);
    np_arr = np_arr.flatten();
    for i in range (len(np_arr)):
        tmp=np_arr[i];
        if(tmp<0):
            tmp=tmp*alpha
        np_arr[i]=tmp;
    x = np_arr.reshape(shape)
    return x"""
    x = np.asarray(x,dtype=float)
    return np.where(x<0,alpha*x,x)