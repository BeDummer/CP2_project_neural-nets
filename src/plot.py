#!/usr/bin/env python3
# main programm for plotting results from task_4-2_big-run.py

import matplotlib.pyplot as plt
import numpy as np

FILENAME="../results/task_4-2_run_N-100_CONF-1000_ERR-5_RUNS-1000_ASYNC_complete.txt"

with open(FILENAME) as f:
    f.readline()
    data = f.readlines()

array = np.array([0, 0, 0, 0])
for line in data:
    array_tmp = [float(i) for i in line.split()]
    array = np.vstack((array, array_tmp))

array = array[1:, :]
sp_state = array[:, 3]
length = int(len(sp_state) / 12)
beta = np.arange(length)
count = 0
#P10 = np.zeros(length)
#P20 = np.zeros(length)
#P30 = np.zeros(length)
P10a = np.zeros(length)
P10b = np.zeros(length)
P10c = np.zeros(length)
P10d = np.zeros(length)
#for i in range(7, len(sp_state), 9):
#    P10[count] = sp_state[i-1]
#    P20[count] = sp_state[i]
#    P30[count] = sp_state[i+1]
#    count += 1
for i in range(5, len(sp_state), 12):
    P10a[count] = sp_state[i-3]
    P10b[count] = sp_state[i]
    P10c[count] = sp_state[i+3]
    P10d[count] = sp_state[i+6]
    count += 1
    
#plt.plot(beta, P10, 'r-*', beta, P20, 'g-*', beta, P30, 'b-*')
plt.plot(beta, P10a, 'r-*', beta, P10b, 'g-*', beta, P10c, 'b-*', beta, P10d, 'k-*')
plt.show()
