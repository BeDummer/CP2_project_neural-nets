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
length = int(len(sp_state) / 14)
beta = np.arange(length)
count = 0
#P10 = np.zeros(length)
#P20 = np.zeros(length)
#P30 = np.zeros(length)
P10a = np.zeros(length-1)
P10b = np.zeros(length-1)
P10c = np.zeros(length-1)
P10d = np.zeros(length-1)
#P10e = np.zeros(length-1)
#P10f = np.zeros(length-1)
#for i in range(7, len(sp_state), 9):
#    P10[count] = sp_state[i-1]
#    P20[count] = sp_state[i]
#    P30[count] = sp_state[i+1]
#    count += 1
for i in range(4, len(sp_state), 14):
    if (i == 4):
        P10inf = (sp_state[i-3] + sp_state[i] + sp_state[i+3] + sp_state[i+6]) / 4
    else:
        P10a[count] = sp_state[i-3]
        P10b[count] = sp_state[i]
        P10c[count] = sp_state[i+3]
        P10d[count] = sp_state[i+6]
#        P10e[count] = sp_state[i+9]
#        P10f[count] = sp_state[i+10]
        count += 1
    
#plt.plot(beta, P10, 'r-*', beta, P20, 'g-*', beta, P30, 'b-*')
plt.plot([1. , length-1], [P10inf, P10inf], 'k--', label = r'without noise ($\beta \rightarrow \inf$)')
plt.plot(beta[1:], P10a, 'r-*', label = '5 runs with noise')
plt.plot(beta[1:], P10b, 'g-*', label = '10 runs with noise')
plt.plot(beta[1:], P10c, 'b-*', label = '15 runs with noise')
plt.plot(beta[1:], P10d, 'm-*', label = '30 runs with noise')
#plt.plot(beta[1:], P10e, 'c-*', label = '50 runs with noise')
#plt.plot(beta[1:], P10f, 'y-*', label = '100 runs with noise')
plt.xticks(beta[1:])
plt.legend()
plt.xlabel(r'$\beta$')
plt.ylabel('ratio of spurious states')
plt.title(r'P = 20')
plt.savefig('../pics/fig_P20_w-noise.png')
plt.savefig('../pics/fig_P20_w-noise.pdf')
plt.show()
