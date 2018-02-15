# Hopfield module

import numpy as np

def hamming(s1, s2):
    """Calculates Hamming distance."""
    comp = s1 != s2
    d = np.sum(comp)
    return d

def hamming_sym(s1, s2):
    """Calculates 'symmetric' Hamming distance (min(d, n-d))."""
    d = hamming(s1, s2)
    n = len(s1)
    d = np.minimum(d, n-d)
    return d

def set_synapse(picts, p, n):
    """Sets synapses for given pictures after Hebbs rule."""
    w = np.zeros((n, n))
    for i in range(p):
        w = w + np.outer(picts[:, i], picts[:, i])
    for i in range(n):
        w[i, i] = 0
    w = w / n
    return w

def rand_picts(n, p):
    """Generates p random pictures of length n."""
    picts = np.sign(np.random.rand(n, p) - 0.5)
    return picts

def update_sync(s1, w):
    """Updates a signal s synchronously with synapses w."""
    s2 = np.sign(w.dot(s))
    return s2

def update_async(s1, w):
    """Updates a signal s asynchronously with synapses w."""
    s2 = s1
    n = len(s1)
    for i in range(n):
        s2[i] = np.sign(np.inner(w[i, :], s2))
    return s2

def rand_signal(n):
    """Generates a random signal of length n."""
    s = np.sign(np.random.rand(n) - 0.5)
    return s
