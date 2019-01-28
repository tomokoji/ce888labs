"""
==========================================================================
                           p o w e r . p y
---------------------------------------------------------------------------
This code is written as part of requirments of CE888 Data Science and 
Decision Making.

This code does power analysis over two 1D arrays.

Author          : Tomoko Ayakawa
Created on      : 25 Jan 2019
Last modified on: 28 Jan 2019
===========================================================================
"""

import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np

def power(sample1, sample2, reps, size, alpha): 
    count = 0 # counter for p-value < 1-alpha

    for i in range (reps):
        # print progress
        print ("\rBootstrap iteration: %d/%d" % (i, reps), end = "")
        
        # generate new samples
        new_samples = []
        for s in [sample1, sample2]:
            new_samples.append(np.random.choice
                               (s, size=s.shape, replace=True))
        
        #print ("New samples", new_samples)
        
        p_value = permutation (new_samples, 1000, size)
        if p_value < (1 - alpha):
            count += 1
    
    power = count / reps
    
    return (power)

def permutation (new_samples, iteration, size):
    count = 0 # counter for t_perm > t_obs (size)
    
    for i in range (iteration):       
        # concatenete the two samples and permutate it
        new = np.hstack(new_samples)
        new = np.random.choice(new, size=new.shape, replace=False)
        
        # split the permutated array
        new_1 = new[:len(new_samples[0])]
        new_2 = new[-len(new_samples[1]):]
        
        # compare the two samples        
        t_perm = np.mean (new_2) - np.mean (new_1)
        if t_perm > size:
            count += 1
    
    p_value = count / iteration
    
    return (p_value)


def mode ():
    print ("Select how to read two arrays:\n" \
           " 0) Read from a csv file\n" \
           " 1) Enter the arrays")
    ans = input (">>> ")
    
    if ans not in ["0", "1"]:
        ans = 9
    else:
        ans = int (ans)
    
    return (ans)

def read_arrays (mode):
    if mode == 0:
        fname = input ("Enter the file path (e.g: ./vehicles.csv): ")  
        df = pd.read_csv(fname)    

        s1 = df[df.columns[0]].dropna()
        s2 = df[df.columns[1]].dropna()
    else:
        s1 = input ("Enter the first array (comma separated): ")
        s2 = input ("Enter the second array (comma separated) : ")
        
        # convert inputs to float map->list->arrays
        s1 = np.array(list (map (float, np.array(s1.split(",")))))
        s2 = np.array(list (map (float, np.array(s2.split(",")))))

    return (s1, s2)


if __name__ == "__main__":
    mode = mode ()

    if mode != 9:
        s1, s2 = read_arrays (mode)

        # enter arguments
        iteration = input ("Enter the iteration times (e.g: 10000): ")
        alpha = input ("Enter the significance level (false positive rate)" \
                       "in the range of 0-1 (e.g: 0.05): ")
        
        iteration = int (iteration)
        size = np.mean (s2) - np.mean (s1) 
        alpha = float (alpha)
        
        # call power analysis function
        power = power (s1, s2, iteration, size, alpha)
        
        print ("\np-value was smaller than specificity (1-alpha) " \
               "for %.2f%% of the times" % (power * 100))