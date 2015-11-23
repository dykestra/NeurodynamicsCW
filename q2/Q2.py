import numpy.random as rn
import sys
sys.path.append('../q1')
from IzNetwork import IzNetwork
from Plot import *


N  = 20
xs = []
ys = []

for i in range(N):
  print "Creating network {}".format(i)

  p =  rn.random()
  runtime = 60000
  
  IN = IzNetwork(p, runtime)
  IN.run()

  xs.append(p)
  ys.append(analyseFirings(IN.firings))

genPlot(xs, ys)