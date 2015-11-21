"""
Setting up connectivity of network
"""

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

def Connectivity(p):

    C = np.zeros((1000,1000))
    
    # make 1000 random connections in each E-module
    for i in range(0, 800, 100):
        r = rn.randint(0, 100, size=(1000,2)) # 1000 random pairs
        for pair in r:
            while (pair[0] == pair[1]) or C[i + pair[0]][i + pair[1]]:
                if pair[0] == pair[1]:
                    pair[1] = rn.randint(0, 100)
                else:
                    pair[0] = rn.randint(0, 100)
                    pair[1] = rn.randint(0, 100)
            C[i + pair[0]][i + pair[1]] = 17
            
    # random rewiring of E-E connections
    for i in range(0, 800):
        for j in range(0, 800):
            if C[i][j] and rn.random() < p:
                C[i][j] = 0
                module = int(np.floor(i / 100.0))
                newModule = np.mod(module + rn.randint(1, 8), 8) # stole this from Ex_3
                h = rn.randint(0, 100) + (newModule * 100)
                
                while C[i][h] != 0:
                    newModule = np.mod(module + rn.randint(1, 8), 8) # stole this from Ex_3
                    h = rn.randint(0, 100) + (newModule * 100)
                
                C[i][h] = 17
                
    # connecting I-module
    for i in range(800, 1000):
        # diffuse connections from each I-neurons
        for j in range(0, 1000):
            if (i != j):
                sf = 2 if (j < 800) else 1   # different scaling factors for I-E and I-I
                C[i][j] = (rn.rand() - 1) * sf
                
        # E-I connections
        mod = rn.randint(0, 8) # pick random E-module
        neurons = rn.randint(0, 100, size=4) # pick 4 random neurons
        for n in neurons:
            C[mod*100 + n][i] = rn.rand() * 50
            
    return C

