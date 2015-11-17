from PlotConnectivity import Scatter
from Connectivity import Connectivity as Conn
from numpy import arange

for i in arange(0, 0.6, 0.1):
  Scatter(Conn(i), i)