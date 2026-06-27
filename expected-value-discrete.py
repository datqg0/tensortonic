import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    sum =0.0;
    ept=0.0
    for i in range (len(x)):
        ept +=x[i]*p[i]
        sum+=p[i]
    if(sum!=1) :
        raise ValueError("invalid value")
    return ept
