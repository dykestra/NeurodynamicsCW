from PlotConnectivity import Scatter
from Connectivity import Connectivity as Conn

for i in xrange(6):
  p = i / 10.0
  Scatter(Conn(p), p)

