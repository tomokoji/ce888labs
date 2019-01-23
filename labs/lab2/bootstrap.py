"""
==========================================================================
                         b o o t s t r a p . p y
---------------------------------------------------------------------------
This code is provided by the module supervisor and edited as part of 
requirments of CE888 Data Science and Decision Making.

This code implements the bootstrap algorithm.

Author          : Tomoko Ayakawa
Created on      : 21 Jan 2019
Last modified on: 23 Jan 2019
===========================================================================
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

min_iteration = 100
max_iteration = 100000
skip = 1000

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

def get_lower_upper (data):
    boots = []
    
    count = 1
    for i in range(min_iteration, max_iteration, skip):
        num = (max_iteration - min_iteration) // skip + 1
        print ("\r Progress: %d/%d" % (count, num), end = "")
        
        boot = boostrap(data, data.shape[0], i)
        boots.append([i, boot[0], "mean"])
        boots.append([i, boot[1], "lower"])
        boots.append([i, boot[2], "upper"])
        
        count += 1

    df_boot = pd.DataFrame(boots, columns=\
                           ['Boostrap Iterations', 'Mean', "Value"])
    sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], \
                          data=df_boot, fit_reg=False, hue="Value")

    #sns_plot.axes[0, 0].set_ylim(0,)
    sns_plot.axes[0, 0].set_xlim(0, max_iteration)
    
    return boot[1], boot[2]
    
def menu ():
    print ("Select which exercise to do\n" \
           " 0) The Bootstrap(1)_salaries.csv\n" \
           " 1) The Bootstrap(2)_vehicles.csv")
    ans = input (">>> ")
    
    if ans not in ["0", "1"]: ans = None
    else: ans = int(ans)
    
    return (ans)

if __name__ == "__main__":
    mode = menu ()
    
    if mode == 0:
        df = pd.read_csv('./salaries.csv')
        data = df.values.T[1]
        get_lower_upper(data)
        
        plt.savefig("bootstrap_confidence.png", bbox_inches='tight')
        plt.savefig("bootstrap_confidence.pdf", bbox_inches='tight')
        
    elif mode == 1:
        df = pd.read_csv('./vehicles.csv')
        
        for header in df.columns:
            print (header)
            data = df[header].dropna()
            
            lower, upper = get_lower_upper(data)
            print ("\n- Lower bound with %d iteration: %.5f\n" \
                   "- Upper bound with %d iteration: %.5f\n" \
                   % (max_iteration, lower, max_iteration, upper))
            
            plt.savefig ('bootstrap2_%s.png' % header)	