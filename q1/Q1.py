from IzNetwork import IzNetwork
from Plot import *
import numpy as np
import threading
import time

class Q1Thread (threading.Thread):
  def __init__(self, threadID, p):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.p = p
    
  def run(self):
    print("Starting thread {}".format(self.threadID))
    runtime = 1000
    
    IN = IzNetwork(self.p, runtime)
    
    t = time.time()
    IN.run()
    workTime = int(np.round(time.time() - t))
    
    print("Thread {} simulation completed in {} seconds".format(self.threadID, workTime))
    
    firings = IN.firings
    firingRates = [np.zeros(8) for count in range(runtime)]

    threadLock.acquire()
    genA(IN.cm, self.p)
    firingRates = genB(runtime, firings, firingRates, self.p)
    genC(runtime, firingRates, self.p)
    threadLock.release()
    
    print("Thread {} completed".format(self.threadID))

threads = []
threadLock = threading.Lock()

for i in range(6):
  # Rewiring probability
  p = i / 10.0
  thread = Q1Thread(i, p)
  thread.start()
  threads.append(thread)
  
for t in threads:
  t.join()

print("Complete")
