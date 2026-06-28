import numpy as np
import math

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    if(len(x)!=len(y)):
        raise ValueError("wrong data")
    sum=0;
    for i in range (len(x)):
        sum+=(abs(x[i]-y[i])*abs(x[i]-y[i]))
    return math.sqrt(sum)