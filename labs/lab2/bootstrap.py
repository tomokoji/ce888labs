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
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
    # <---INSERT YOUR CODE HERE--->

    means = []
    for i in range (iterations):
        # create a random array 
        randn = np.random.randint(sample_size - 1, size=(1, sample_size))
        boot_samples = [sample[i] for i in randn]
    
        # store the means
        means.append (np.mean (boot_samples))
    
    # obtain the mean, 5% & 95% percentile of the boot sample means    
    means = np.array (means)
    data_mean = np.mean (means)
    lower = np.percentile (means, 5)
    upper = np.percentile (means, 95)
    
    return data_mean, lower, upper


if __name__ == "__main__":
    df = pd.read_csv('./salaries.csv')

    data = df.values.T[1]
    boots = []
    for i in range(100, 100000, 1000):
        boot = boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])

    df_boot = pd.DataFrame(boots, columns=\
                           ['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], \
                          data=df_boot, fit_reg=False, hue="Value")

    sns_plot.axes[0, 0].set_ylim(0,)
    sns_plot.axes[0, 0].set_xlim(0, 100000)

    sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
    sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')


    #print ("Mean: %f")%(np.mean(data))
    #print ("Var: %f")%(np.var(data))
	


	