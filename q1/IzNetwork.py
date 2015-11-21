from Connectivity import Connectivity as Conn
import numpy as np
import numpy.random as rn
import threading

class IzNetwork:

  def __init__(self, _p, _runtime):
    self.p = _p
    self.cm = Conn(self.p)
    
    self.runtime = _runtime
    
    self.neurons = [IzNeuron(True, count) for count in range(800)]
    self.neurons = self.neurons + [IzNeuron(False, count) for count in range(800, 1000)]
    
    self.firings = [[] for count in range(self.runtime)]

  def run(self):
    for t in range(1, self.runtime):
      for neuron in self.neurons:
        neuron.I = 15 if rn.poisson(0.01, 1)[0] > 0 else 0
      self.updateNeurons(t)
        
    return
    
  def updateNeurons(self, t):
    dt = 1
    
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
    for k in range(int(1/dt)):
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
          
          for i in range(1000):
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
