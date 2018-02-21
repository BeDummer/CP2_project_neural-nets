#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.2

import numpy as np
import hopfield_func as hf

N = 10000 #number of neurons
P = np.array([1000, 2000, 3000]) #number of pictures
CONV_ERROR = 5 #definition, when a picture is reached
MAX_ITER = 100 #maximum number of iterations (synchronous update)
CONFIGS = 1000 #number of random configurations
UPDATE_MODE = True #True = asynchronous update, False = synchronous update
BETA = 4 #False = no finite temperature implemented, else finite temp. with BETA
BETA_ITER = 5 #number of iterations with finite temperature
FILENAME = "../results/task_4-2_run_N-{0}_CONF-{1}_ERR-{2}_ASYNC.txt".format(N, CONFIGS, CONV_ERROR)
np.random.seed()

with open(FILENAME,"w") as f:
    f.write("beta beta_iter P sp_state\n")
for BETA in range(11):
    for BETA_ITER in range(3, 10, 3):
        for i_p in range(len(P)):
            #loop over different numbers of pictures
            picts = hf.rand_picts(N, P[i_p])
            w = hf.set_synapse(picts, P[i_p], N)
            sp_state = 0
            
            for pic in range(CONFIGS):
                #loop over pictures
                beta = BETA
                s1 = hf.rand_signal(N)
                s2 = hf.update(s1, w, UPDATE_MODE, beta)
                count = 1
                while beta:
                    s1 = s2.copy()
                    s2 = hf.update(s1, w, UPDATE_MODE, beta)
                    count += 1
                    if (count == BETA_ITER):
                        beta=False

                while (count < MAX_ITER) and not (np.array_equal(s1, s2)):
                    #convergence loop to reach fixpoint
                    count += 1
                    s1 = s2.copy()
                    s2 = hf.update(s1, w, UPDATE_MODE, beta)
                
                if (hf.is_pic(s2, picts, CONV_ERROR, True) == -1):
                    sp_state += 1
            with open(FILENAME,"a") as f:
                f.write("{0} {1} {2} {3}\n".format(BETA, BETA_ITER, P[i_p], sp_state/N))
