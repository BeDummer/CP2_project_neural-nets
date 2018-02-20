#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.2

import numpy as np
import hopfield_func as hf

N = 100 #number of neurons
P = np.array([10, 20, 30]) #number of pictures
CONV_ERROR = 5 #definition, when a picture is reached
MAX_ITER = 100 #maximum number of iterations (synchronous update)
CONFIGS = 10 #number of random configurations
UPDATE_MODE = True #True = asynchronous update, False = synchronous update
BETA = False #False = no finite temperature implemented, else finite temp. with BETA
BETA_ITER = 5 #number of iterations with finite temperature
np.random.seed()

for i_p in range(len(P)):
    #loop over different numbers of pictures
    picts = hf.rand_picts(N, P[i_p])
    w = hf.set_synapse(picts, P[i_p], N)
    errors = np.zeros((CONFIGS,1))
    iters = np.zeros((CONFIGS,1))
    ispic = np.zeros((CONFIGS,1))
    
    for pic in range(CONFIGS):
        #loop over pictures
        beta = BETA
        s1 = hf.rand_signal(N)
        s2 = hf.update(s1, w, UPDATE_MODE, beta)
        count = 1
#        while beta:
#            s1 = s2.copy()
#            s2 = hf.update(s1, w, UPDATE_MODE, beta)
#            count += 1
#            if (count == BETA_ITER):
#                beta=False

        while (count < MAX_ITER) and not (np.array_equal(s1, s2)):
            #convergence loop to reach fixpoint
            count += 1
            s1 = s2.copy()
            s2 = hf.update(s1, w, UPDATE_MODE, beta)
        
        iters[pic] = count
        ispic[pic] = hf.is_pic(s2, picts, CONV_ERROR, True)
        if (ispic[pic] != -1):
            errors[pic] = hf.hamming_sym(picts[:, int(ispic[pic])], s2) / N
        else:
            errors[pic] = -1
    
    print(errors)
    print(iters)
    print(ispic)
    print("---")
