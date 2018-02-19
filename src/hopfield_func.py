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
        w = np.add(w, np.outer(picts[:, i], picts[:, i]))
    for i in range(n):
        w[i, i] = 0.
    w = np.divide(w,n)
    return w

def rand_picts(n, p):
    """Generates p random pictures of length n."""
    picts = np.sign(np.random.rand(n, p) - 0.5)
    return picts

def update(s1, w, async=True):
    """Updates a signal s asynchronously or synchronously with synapses w."""
    if async:
        s2 = s1.copy()
        n = len(s1)
        for i in range(n):
            cache = np.sign(np.inner(w[i, :], s2))
            if (cache == 0):
                cache = -1
            s2[i] = cache
        return s2
    else:
        s2 = np.sign(w.dot(s1))
        return s2

def rand_signal(n):
    """Generates a random signal of length n."""
    s = np.sign(np.random.rand(n) - 0.5)
    return s
    
def is_pic(s, picts, error=1, fancy_hamming=False):
    """Checks, if signal s is (almost) equal to a given picture
    ... and returns the number of the picture (or -1 if false)"""
    p = picts.shape[(picts.ndim - 1)]
    for pic in range(p):
        if fancy_hamming:
            if (hamming_sym(s, picts[:, pic]) < error):
                return pic
        else:
            if (hamming(s, picts[:, pic]) < error):
                return pic
    return (-1)
