"""
==========================================================================
                           p o w e r . p y
---------------------------------------------------------------------------
This code is written as part of requirments of CE888 Data Science and 
Decision Making.

This code does power analysis on Current and New Fleets.

Author          : Tomoko Ayakawa
Created on      : 25 Jan 2019
Last modified on: 25 Jan 2019
===========================================================================
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def power(sample1, sample2, reps, size, alpha): 
    a = 1
    
    return (1.00)

if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    
    crr = df[df.columns[0]].dropna()
    new = df[df.columns[1]].dropna()
    
    print (crr)
    print (new)
    
    p_value = power(sample1, sample2, reps, size, alpha)
    
    print ("p-value is %.5f" % p_value)