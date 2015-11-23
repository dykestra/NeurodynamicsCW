from jpype import *
import os
import numpy.random as rn
import sys
sys.path.append('../q1')
from IzNetwork import IzNetwork
from Plot import *

path = os.getcwd() + "/infodynamics.jar"
startJVM(getDefaultJVMPath(), "-Djava.class.path=" + path)

N  = 2
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

shutdownJVM()
genPlot(xs, ys)