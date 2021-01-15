## Cell to be converted to a .py file and submitted

import pandas as pd
import numpy as np
import pandas_datareader as pdr

# Code problem 1

def oos_rsquared(y, yhat, mu):

    resid_oos = y - yhat
    oos_sse = resid_oos @ resid_oos
    oos_tss = ((y - mu)**2).sum()
    oos_r2 = 1- oos_sse/ oos_tss
    
    return oos_r2

# Code problem 2

def oos_residuals(y, x, beta, first, last):
    
    y = y[first:last]
    x = x[first:last]
    resid = y - x @ beta

    return resid
