from PlotConnectivity import Scatter as Lattice
from Connectivity import Connectivity as Conn

for i in xrange(6):
  p = i / 10.0
  Lattice(Conn(p), p)

