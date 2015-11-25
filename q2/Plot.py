import numpy as np
import matplotlib.pyplot as plt
from MICalc import MICalc

def genPlot(xs, ys):
  plt.plot(xs, ys, "b.")
  plt.axis([0, 1, 0, 5])
  plt.savefig("Multi-Information plot.png")
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
  
  firings2 = []
  
  # Calculate mean firing rates
  for tblock in range(50, runtime, 20):
    means = np.zeros(8)
    for t in range(50):
      means += firingRates[tblock - t]
    means /= 50.0
    if tblock > 1000:
        firings2.append(means)

  return MICalc(firings2)
