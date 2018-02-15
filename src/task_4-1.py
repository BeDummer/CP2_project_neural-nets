#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.1

import numpy as np
import hopfield_func as hf

N = 100 #number of neurons
P = np.array([10, 20, 30]) #number of pictures
CONV_ERROR = 0.1 #definition, when a fixpoint is reached
MAX_ITER = 1000; #maximum number of iterations (synchronous update)
np.random.seed()

for i_p in range(len(P)):
    #loop over different numbers of pictures
    picts = hf.rand_picts(N, P[i_p])
    #print(picts)
    w = hf.set_synapse(picts, P[i_p], N)
    errors = np.zeros((P[i_p],2))
    iters = np.zeros((P[i_p],1))
    #print(w)
    
    for pic in range(P[i_p]):
        #loop over pictures
        s1 = picts[:, pic]
        s1 = hf.rand_signal(N)
        #print(s1)
        s2 = hf.update_async(s1, w)
        #print(s2)
        d_old = N+1
        d = hf.hamming(s1, s2)
        errors[pic, 0] = d
        count = 0
        
        while np.absolute(d_old - d) > CONV_ERROR:
            #convergence loop to reach fixpoint
            count += 1
            d_old = d
            s1 = s2
            s2 = hf.update_async(s1, w)
            d = hf.hamming(s1, s2)
        
        errors[pic, 1] = d
        iters[pic] = count
    
    print(errors)
    print(iters)