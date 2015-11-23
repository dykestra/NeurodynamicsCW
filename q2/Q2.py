import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import sys
sys.path.append('../q1')
from IzNetwork import IzNetwork
from MICalc import MICalc

N  = 20
xs = []
ys = []

for i in range(N):
  print "Creating network number {}".format(i)

  p =  rn.random()
  runtime = 60000
  
  IN = IzNetwork(p, runtime)
  IN.run()

  xs.append(p)
  ys.append(analyseFirings(N.firings))

plt.plot(xs, ys, "b.")
plt.axis([0, (int)(max(xs) + 1), 0, (int)(max(ys) + 1)])
plt.savefig("Multi-Information plot png".format(p))
plt.clf()
print("Multi-Information plot generated")


def analyseFirings(firings):
  runtime = len(firings)
  firingRates = [np.zeros(8) for count in range(runtime)]
  modules = [[] for count in range(8)]

  # Get Num firings per milisecond
  for t in range(runtime):
    for idx in firings[t]:
      module = int(np.floor(idx / 100.0))
      if module < 8:
        firingRates[t][module] += 1
  
  # Calculate mean firing rates
  for tblock in range(50, runtime, 20):
    means = np.zeros(8)
    for t in range(50):
      means += firingRates[tblock - t]
    means /= 50
    for module in range(8):
      # Discard first seconds worth of data
      if tblock > 1000:
        modules[module].append([tblock, means[module]])  

  return MICalc(modules)