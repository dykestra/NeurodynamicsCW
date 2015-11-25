import matplotlib.pyplot as plt
import numpy as np

# Generate plots for section a
def genA(conMatrix, p):
  xs = []
  ys = []
  N = len(conMatrix) - 200

  for i in range(N):
    for j in range(N):
      if conMatrix[i][j] != 0:
        xs.append(i)
        ys.append(j)


  plt.plot(xs, ys, "b.")
  plt.axis([0, N, 0, N])
  fig = plt.gcf()
  fig.set_size_inches(8, 8)
  fig.savefig("a/Connectivity plot for p={}.png".format(p))
  plt.clf()
  print("Connectivity plot for p={} completed".format(p))


# Generate plots for section b
def genB(runtime, firings, firingRates, p):
  xs = []
  ys = []
  N = len(firings) - 200
  
  for t in range(runtime):
    for idx in firings[t]:
      xs.append(t)
      ys.append(idx)
      module = int(np.floor(idx / 100.0))
      if module < 8:
        firingRates[t][module] += 1
  
  plt.plot(xs, ys, "b.")
  plt.axis([0, 1000, 0, N])
  fig = plt.gcf()
  fig.set_size_inches(8, 3)
  fig.savefig("b/Firing plot for p={}.png".format(p))
  plt.clf()
  
  print("Firing graph for p = {} completed".format(p))
  
  return firingRates


# Generate plots for section c
def genC(runtime, firingRates, p):
  lines = [[[],[]] for count in range(8)]
  colours = ['b-','r-','g-','c-','y-','k-','m-','b-']
  maxY = 0
  
  for tblock in range(50, runtime, 20):
    means = np.zeros(8)
    for t in range(50):
      means += firingRates[tblock - t]
    means /= 50
    for module in range(8):
      lines[module][0].append(tblock)
      lines[module][1].append(means[module])
      if (means[module] > maxY):
        maxY = means[module]

  for i in range(8):  
    plt.plot(lines[i][0], lines[i][1], colours[i])
  
  plt.axis([0,1000,0,int(maxY) + 1])
  fig = plt.gcf()
  fig.set_size_inches(8, 3)
  fig.savefig("c/Average module firing plot for p={}.png".format(p))
  plt.clf()
  
  print("Means firing graph for p = {} completed".format(p))
 
  
  
