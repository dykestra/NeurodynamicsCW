import numpy as np
import matplotlib.pyplot as plt


def Scatter(CIJ, P):
  """
  Inputs:
  CIJ  --  Graph connectivity matrix.
  """
  xs = []
  ys = []
  N = len(CIJ) - 200

  for i in range(N):
    for j in range(N):
      if CIJ[i][j] != 0:
        xs.append(i)
        ys.append(j)


  plt.plot(xs, ys, "b.")
  plt.axis([0, N, 0, N])
  plt.savefig("a/plot for p=%.2f.pdf" % P)


def Lattice(CIJ):
  """
  Inputs:
  CIJ  --  Graph connectivity matrix.
  """

  N = len(CIJ)

  # Calculate the position of every node, assuming they are
  # evenly spaced in the unit circle
  angle = (2*np.pi)/N
  X_pos = np.zeros(N)
  Y_pos = np.zeros(N)
  list_of_lines = []
  for i in range(N):
    X_pos[i] = np.cos(angle*(N-(i)) + np.pi/2)
    Y_pos[i] = np.sin(angle*(N-(i)) + np.pi/2)

  # Create a list with the edges
  to_edge, from_edge = np.where(CIJ)
  nb_edges = len(to_edge)

  for i in range(nb_edges):
    xf = X_pos[from_edge[i]]
    yf = Y_pos[from_edge[i]]
    xt = X_pos[to_edge[i]]
    yt = Y_pos[to_edge[i]]
    list_of_lines.append((xf, xt))
    list_of_lines.append((yf, yt))
    list_of_lines.append('b')

  # Plot nodes and edges
  print "{0}".format(len(list_of_lines))
  plt.plot(*list_of_lines)
  plt.scatter(X_pos, Y_pos, s=80, c='r', marker='o', alpha=1)
  plt.axis('off')
  plt.show()
