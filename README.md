# NeurodynamicsCW

## Question 1
All files in the directory q1 are associated with this question. 

* Connectivity.py: Depends on Numpy. This file contains one function that given a rewiring probablity p will generate a connection matrix as per the specification.

* IzNetwork.py: Depends on Numpy, Threading and Connectivity. This file declares two classes one which holds the parameters for the individual neuron it represents along with the incoming firings and another class to simulate the network of neurons as described in the specification.

* Plot.py: Depends on Matplotlib and Numpy. This file contains 3 methods to analyse and plot data for sections a, b and c as described in the specification.

* Q1.py: Depends on Numpy, IzNetwork and Plot. This file is just a script to create and run the network and then analyse and plot the results of the experiment outlined in the specification.

The plots for section a, b and c can be found in the respective folders. Note by running the following code the plots in these folders will be replaced: 

```
python Q1.py
``` 

## Question 2
All files in the directory q2 are associated with this question. 

* MICalc.py: Depends on Jpype and OS. This file contains one function that calculates the multi-information of the set of mean firing rates for the set of modules. Note this section spins up a JVM and uses the infodynamics JAR to run the analysis.

* Plot.py: Depends on Numpy, Matplotlib.pyplot and MICalc. This file contains a function for analysing the firings data of 1 run of a network resulting in the output of the multi-information of the 8 modules' firing data and another function to plot the results of many such runs.

* Q2.py: Depends on Numpy, q1/IzNetwork (and thus sys) and Plot. This file is a script that performs analysis of 20 randomly rewired networks and generates the plot of p vs information in bits.

* infodynamics.jar: Java Information Dynamics Toolkit.
