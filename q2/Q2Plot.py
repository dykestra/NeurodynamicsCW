from Plot import *

xs = []
ys = []

with open("output.txt") as f:
  for line in f:
    cords = line.split(",")
    xs.append(float(cords[0]))
    ys.append(float(cords[1]))
    
genPlot(xs, ys)
