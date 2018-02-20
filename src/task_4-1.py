#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.1

import numpy as np
import hopfield_func as hf

N = 100 #number of neurons
P = np.array([10, 20, 30]) #number of pictures
MAX_ITER = 100; #maximum number of iterations (synchronous update)
UPDATE_MODE = True #True = asynchronous update, False = synchronous update
np.random.seed()

for i_p in range(len(P)):
    #loop over different numbers of pictures
    picts = hf.rand_picts(N, P[i_p])
    w = hf.set_synapse(picts, P[i_p], N)
    errors = np.zeros((P[i_p],2))
    iters = np.zeros((P[i_p],1))
    ispic = np.zeros((P[i_p],1))
    
    for pic in range(P[i_p]):
        #loop over pictures
        s1 = picts[:, pic].copy()
        s2 = hf.update(s1, w, UPDATE_MODE)
        errors[pic, 0] = hf.hamming(s1, s2) / N
        count = 1       

        while (count < MAX_ITER) and not (np.array_equal(s1, s2)):
            #convergence loop to reach fixpoint
            count += 1
            s1 = s2.copy()
            s2 = hf.update(s1, w, UPDATE_MODE)
        
        errors[pic, 1] = hf.hamming(picts[:, pic], s2) / N
        iters[pic] = count
        ispic[pic] = hf.is_pic(s2, picts)
    
    print(errors)
    print(iters)
    print(ispic)
