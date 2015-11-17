from PlotConnectivity import Scatter as Lattice
from Connectivity import Connectivity as Conn
from numpy import arange

for i in arange(0, 0.6, 0.1):
  Lattice(Conn(i), i)