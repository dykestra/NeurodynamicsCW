from Connectivity import Connectivity as Conn
import numpy as np
import numpy.random as rn


class IzNetwork:

  def __init__(self):
    self.p = 0
    self.cm = Conn(p)
    
    self.runtime = 1000
    
    self.neurons = [IzNeuron(True, count) for count in xrange(800)]
    self.neurons = neurons + [IzNeuron(False, count + 800) for count in xrange(200)]
    
    self.firings = [[] for count in xrange(runtime)]

  def run(self):
    for t in xrange(1, runtime):
      for neuron in self.neurons:
        neuron.I = 15 if np.poisson(0.01, 1)[0] > 0 else 0
      updateNeurons(t)
        
    return
    
  def updateNeurons(t):
    dt = 0.2
    
    # Update current
    for neuron in self.neurons:
      ;#TODO: Get update from firings
      
    # Update v and u using the Izhikevich model and Euler method
    for k in xrange(int(1/dt)):
      for neuron in self.neurons:
        v = neuron.v
        u = neuron.u

        neuron.v += dt*(0.04*v*v + 5*v + 140 - u + n.I)
        neuron.u += dt*(n.a*(n.b*v - u))

      # Find index of neurons that have fired this millisecond
      fired = []
      for neuron in neurons:
        if neuron.v > 30:
          fired.append(neuron)

      if len(fired) > 0:
        for f in fired:
          self.firings[t].append(f)
          
          #TODO: Add firing to neuron somehow

          # Reset the membrane potential after spikes
          f.v  = f.c
          f.u += f.d

    return
      
  
class IzNeuron:

  def __init__(self, isExcitatory, index):

    self.a = 0.02
    self.b = 0.2 if isExcitatory else 0.25
    self.c = -65 + 10 * rn.rand() - 5
    self.d = (8 if isExcitatory else 2) + rn.rand()

    self.u = 0
    self.v = 0
    
    self.index = index

    self.incomingFirings = []

IN = IzNetwork()

IN.run()
