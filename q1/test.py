from PlotConnectivity import Scatter
from Connectivity import Connectivity as Conn


def countConn(p):
  print "P = "+ str(p)
  con = Conn(p)
  count = 0

  for i in xrange(0, 800, 100):
    count = 0
    
    for j in xrange(i, i + 100):
      for k in xrange(800):
        if con[j][k] != 0:
          count += 1

    print "Count for module beginning neuron {} is: ".format(i) + str(count)


for i in xrange(6):
  countConn(i/10.0)

