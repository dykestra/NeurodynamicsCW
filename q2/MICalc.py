from jpype import *
import os

# Data list of 8 lists for each module. Each module is a list of points [[time, rate], ..... [t, r]]
def MICalc(data):
    path = os.getcwd() + "/infodynamics.jar"

    startJVM(getDefaultJVMPath(), "-Djava.class.path=" + path)
    classKraskov2 = JPackage("infodynamics.measures.continuous.kraskov").MultiInfoCalculatorKraskov2
    kraskov = classKraskov2()

    kraskov.initialise(2)
    
    # Add each module of observations
    kraskov.startAddObservations()
    for module in data:
        # module[i] = [time, firingRate] 
        javaArray = JArray(JDouble, 2)(module)
        kraskov.addObservations(javaArray)
    kraskov.finaliseAddObservations()
    
    # Calculate the multi-infrmation for the 8 sets
    information = kraskov.computeAverageLocalOfObservations()
    shutdownJVM()

    # Conversion to bits
    return (information * np.log2(np.e))
