"""
Setting up connectivity of network
"""

import numpy as np
import numpy.random as rn

def Connectivity(p):

    C = np.zeros((100,100))
    
    # make 1000 random connections in each E-module
    for i in xrange(0, 800, 100):
        r = rn.randint(0, 100, size=(1000,2)) # 1000 random pairs
        for pair in r:
            C[i + pair[0]][i + pair[1]] = 1
            
    # random rewiring of E-E connections
    for i in xrange(0, 800):
        for j in xrange(0, 800):
            if C[i][j] and rn.random() < p:
                C[i][j] = 0
                h = int(np.mod(i + np.ceil(rn.random()*(800-1))-1, 800)) # stole this from Ex_3
                C[i][h] = 1
                
    # connecting I-module
    for i in xrange(800, 1000):
        # diffuse connections from each I-neurons
        for j in xrange(0, 1000):
            if (i != j):
                C[i][j] = 1
                
        # E-I connections
        mod = rn.randint(0, 8, size=None) # pick random E-module
        neurons = rn.randint(0, 100, size=4) # pick 4 random neurons
        for n in neurons:
            C[mod*100 + n][i] = 1
            
    return C