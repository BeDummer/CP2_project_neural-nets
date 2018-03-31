#!/usr/bin/env python3
# main programm for simulation of Hopfield model: task 4.1

import numpy as np
import hopfield_func as hf

N = 100 #number of neurons
P = np.array([10, 20, 30]) #number of pictures
MAX_ITER = 100; #maximum number of iterations (synchronous update)
UPDATE_MODE = False #True = asynchronous update, False = synchronous update
RUNS = 100 #number of runs for better statistics with respect to the randomness of the saved pictures
if (UPDATE_MODE):
    FILENAME = "../results/task_4-1_run_N-{0}_RUNS-{1}_ASYNC.txt".format(N, RUNS)
else:
    FILENAME = "../results/task_4-1_run_N-{0}_RUNS-{1}_SYNC.txt".format(N, RUNS)
np.random.seed()

with open(FILENAME,"w") as f:
    f.write("P error_1 error_conv iters\n")
    
for i_p in range(len(P)):
    #loop over different numbers of pictures
    errors_1 = 0. #error after one iteration
    errors_conv = 0. #error after convergence
    iters = 0. #number of iterations to convergence

    for run in range(RUNS):
        picts = hf.rand_picts(N, P[i_p])
        w = hf.set_synapse(picts, P[i_p], N)
        
        for pic in range(P[i_p]):
            #loop over pictures
            s1 = picts[:, pic].copy()
            s2 = hf.update(s1, w, UPDATE_MODE)
            errors_1 += hf.hamming(s1, s2) / N
            count = 1 #count for number of iterations

            while (count < MAX_ITER) and not (np.array_equal(s1, s2)):
                #convergence loop to reach fixpoint
                count += 1
                s1 = s2.copy()
                s2 = hf.update(s1, w, UPDATE_MODE)
            
            errors_conv += hf.hamming(picts[:, pic], s2) / N #error after convergence
            iters += count
            
    with open(FILENAME,"a") as f:
            f.write("{0} {1} {2} {3}\n".format(P[i_p], errors_1 / P[i_p] / RUNS, errors_conv / P[i_p] / RUNS, iters / P[i_p] / RUNS))
               
    print("P = {0}\n".format(P[i_p]))
    print(errors_1 / P[i_p] / RUNS)
    print(errors_conv / P[i_p] / RUNS)
    print(iters / P[i_p] / RUNS)
    print("---")

if (UPDATE_MODE):
    print("Update-Mode: Asynchronous")
else:
    print("Update-Mode: Synchronous")
