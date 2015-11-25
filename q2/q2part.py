from jpype import *
import os
import numpy.random as rn
import sys
sys.path.append('../q1')
from IzNetwork import IzNetwork
from Plot import *

path = os.getcwd() + "/infodynamics.jar"
startJVM(getDefaultJVMPath(), "-Djava.class.path=" + path)

p =  rn.random()
runtime = 60000

IN = IzNetwork(p, runtime)
IN.run()

print("{},{}".format(p, analyseFirings(IN.firings)))

shutdownJVM()
