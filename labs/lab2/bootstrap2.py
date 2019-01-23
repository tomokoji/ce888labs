"""
==========================================================================
                         b o o t s t r a p . p y
---------------------------------------------------------------------------
This code is provided by the module supervisor and edited as part of 
requirments of CE888 Data Science and Decision Making.

This code implements the bootstrap algorithm.

Author          : Tomoko Ayakawa
Created on      : 21 Jan 2019
Last modified on: 21 Jan 2019
===========================================================================
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import bootstrap 

def get_lower_upper (data):
    boots = []
    max_iteration = 100000
    for i in range(100, max_iteration, 1000):
        boot = bootstrap.boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=\
                           ['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], \
                          data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0,)
    sns_plot.axes[0, 0].set_xlim(0, max_iteration)

if __name__ == '__main__':
    # read a csv file
    df = pd.read_csv('./vehicles.csv')

    fig = plt.figure (figsize = (7, 10))    
    
    i = 1
    for header in df.columns:
        plt.subplot (2,1,i)
        data = df[header].dropna()
        get_lower_upper(data)
        i += 1
 
    # save a picture file
    plt.savefig ('bootstrap2_FleetComparison.png')