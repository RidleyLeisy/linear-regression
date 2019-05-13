#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Our goal is create a function for a and B. Remember that a and B are defined as...


# ![a_partial8.png](attachment:a_partial8.png)

# ![new_b_6.png](attachment:new_b_6.png)

# ### Let's create three functions


def get_b(x, y):
    
    numerator = np.sum((x*y) - ((y.mean())*x))
    denominator =  np.sum((x**2) - (x.mean()*x))
    b = numerator / denominator
    
    return b


def get_a(x, y):
    
    a = np.mean(y) - get_b(x,y)*np.mean(x)
    
    return a


def predict_value(x_pred, x_known, y_known):
    
    y_pred = get_a(x_known, y_known) + get_b(x_known, y_known) * x_pred
    
    return y_pred

