from jpype import *
import numpy as np

# Data list of 8 lists for each module. Each module is a list of points [[time, rate], ..... [t, r]]
def MICalc(data):
    classKraskov2 = JPackage("infodynamics.measures.continuous.kraskov").MultiInfoCalculatorKraskov2
    kraskov = classKraskov2()

    kraskov.initialise(8)
    
    # Add each module of observations
    kraskov.startAddObservations()
    
    javaArray = JArray(JDouble, 2)(data)
    kraskov.addObservations(javaArray)
        
    kraskov.finaliseAddObservations()
    
    # Calculate the multi-infrmation for the 8 sets
    information = kraskov.computeAverageLocalOfObservations()

    # Conversion to bits
    return (information * np.log2(np.e))
