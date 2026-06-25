import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    
    e=math.e
    shape = np.shape(x)
    arr = np.asarray(x,dtype=float)
    #first way
    #rr = arr.flatten();
    #for i in range(len(arr)):
    #    arr[i]=1/(1+e**(-arr[i]))
    #arr = arr.reshape(shape)
    #return arr
    #second way 
    return 1 / (1 + np.exp(-arr))