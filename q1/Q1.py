from IzNetwork import IzNetwork
from Plot import *
import numpy as np

for i in range(6):
  # Rewiring probability
  p = i / 10.0
  # Time in ms to simulate
  runtime = 1000
  
  IN = IzNetwork(p, runtime)
  
  IN.run()
  
  firings = IN.firings
  firingRates = [np.zeros(8) for count in range(runtime)]

  genA(IN.cm, p)
  firingRates = genB(runtime, firings, firingRates, p)
  genC(runtime, firingRates, p)
