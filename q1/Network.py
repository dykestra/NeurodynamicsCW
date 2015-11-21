from Connectivity import Connectivity as Conn
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

class IzNetwork:

  def __init__(self, _p, _runtime):
    self.p = _p
    self.cm = Conn(self.p)
    
    self.runtime = _runtime
    
    self.neurons = [IzNeuron(True, count) for count in xrange(800)]
    self.neurons = self.neurons + [IzNeuron(False, count) for count in xrange(800, 1000)]
    
    self.firings = [[] for count in xrange(self.runtime)]

  def run(self):
    for t in xrange(1, self.runtime):
      for neuron in self.neurons:
        neuron.I = 15 if rn.poisson(0.01, 1)[0] > 0 else 0
      self.updateNeurons(t)
        
    return
    
  def updateNeurons(self, t):
    dt = 0.2
    
    # Update current
    for neuron in self.neurons:
      i = len(neuron.incomingFirings)
      while i > 0:
        i -= 1
        
        firing = neuron.incomingFirings[i]
        
        if firing[0] == 1:
          neuron.I += firing[1]
          del neuron.incomingFirings[i]
        else:
          firing[0] -= 1
      
    # Update v and u using the Izhikevich model and Euler method
    for k in xrange(int(1/dt)):
      for neuron in self.neurons:
        v = neuron.v
        u = neuron.u

        neuron.v += dt*(0.04*v*v + 5*v + 140 - u + neuron.I)
        neuron.u += dt*(neuron.a*(neuron.b*v - u))

      # Find index of neurons that have fired this millisecond
      fired = []
      for neuron in self.neurons:
        if neuron.v >= 30:
          fired.append(neuron)

      if len(fired) > 0:
        for f in fired:
          self.firings[t].append(f.index)
          
          for i in xrange(1000):
            if self.cm[f.index][i] != 0:
              delay = rn.randint(1, 21) if ((f.index < 800) and (i < 800)) else 1
              self.neurons[i].incomingFirings.append([delay, self.cm[f.index][i]])

          # Reset the membrane potential after spikes
          f.v  = f.c
          f.u += f.d

    return

class IzNeuron:

  def __init__(self, isExcitatory, _index):

    self.a = 0.02
    self.b = 0.2 if isExcitatory else 0.25
    self.c = -65
    self.d = 8 if isExcitatory else 2

    self.v = -65
    self.u = self.b * self.v
    
    self.index = _index

    self.incomingFirings = []

for i in xrange(6):
  # Rewiring probability
  p = i / 10.0
  
  # Time in ms to simulate
  runtime = 1000
  
  IN = IzNetwork(p, runtime)
  
  IN.run()
  
  firings = IN.firings
  firingRates = [np.zeros(8) for count in xrange(runtime)]
  
  xs = []
  ys = []
  N = len(firings) - 200
  
  for t in xrange(runtime):
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
  
  lines = [[[],[]] for count in xrange(8)]
  colours = ['b-','r-','g-','c-','y-','k-','m-','b-']
  
  for tblock in xrange(50, runtime, 20):
    means = np.zeros(8)
    for t in xrange(50):
      means += firingRates[tblock - t]
    means /= 50
    for module in xrange(8):
      lines[module][0].append(tblock)
      lines[module][1].append(means[module])
      
  for i in xrange(8):  
    plt.plot(lines[i][0], lines[i][1], colours[i])

  plt.axis([0,1000,0,10])
  fig = plt.gcf()
  fig.set_size_inches(8, 3)
  fig.savefig("c/Average module firing plot for p={}.png".format(p))
  plt.clf()
  
