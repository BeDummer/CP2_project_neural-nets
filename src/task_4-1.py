#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.1

import numpy as np
import hopfield_func as hf

n = 100 #number of neurons
p = np.array([10, 20, 30]) #number of pictures
conv_error = 0.1 #definition, when a fixpoint is reached
max_iter = 1000; #maximum number of iterations (synchronous update)

for i_p in range(len(p)):
    #loop over different numbers of pictures
    picts = hf.rand_picts(n, p[i_p]) 
    w = hf.set_synapse(picts, p[i_p], n)
    errors = np.zeros((p[i_p],2))
    iters = np.zeros((p[i_p],1))
    
    for pic in range(p[i_p]):
        #loop over pictures
        s1 = picts[:, pic]
        s2 = update_async(s1, w)
        d_old = 0
        d = hamming(s1, s2)
        errors[pic, 0] = d
        count = 0
        
        while np.absolute(d_old - d) > conv_error:
            #convergence loop to reach fixpoint
            count = count + 1
            d_old = d
            s1 = s2
            s2 = update_async(s1, w)
            d = hamming(s1, s2)
        
        errors[pic, 1] = d
        iters[pic] = count
    
    errors
    iters