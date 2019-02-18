"""
===========================================================================
                              v e h i c l e s . p y
---------------------------------------------------------------------------
This code is written as part of requirments of CE888 Data Science and
Decision Making.

This code reads a csv file and create histograms and scatterplots.

Author          : Tomoko Ayakawa
Created on      : 21 Jan 2019
Last modified on: 25 Jan 2019
===========================================================================
"""

# import labraries
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def histogram (data, name):
    sns.distplot(data, bins=20, kde=False, rug=True, \
                 label=name).get_figure()

    axes = plt.gca()
    axes.set_xlabel('Value') 
    axes.set_ylabel('Count')
    axes.legend ()
    
def scatter (data, name):
    x = pd.DataFrame (np.arange (len (data)))
    
    axes2.scatter (x, data, label=name)
    axes2.set_xlabel('Data Id')
    axes2.set_ylabel('Values')
    axes2.legend ()
    
if __name__ == '__main__':
    # read a csv file
    df = pd.read_csv('./vehicles.csv')

    fig = plt.figure (figsize = (7, 10))    
    # histogram
    plt.subplot (2,1,1)
    for header in df.columns:
        # remove empty values by .dropna()
        histogram (df[header].dropna(), header)

    # scatter plot
    axes2 = plt.subplot (2,1,2)
    for header in df.columns:
        scatter (df [header].dropna (), header)       

    # save a picture file
    plt.savefig ('charts/vehicles_plot.png')
    