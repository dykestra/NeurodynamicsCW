from jpype import *
import os


def MICalc(data):
    path = os.getcwd() + "/infodynamics.jar"

    startJVM(getDefaultJVMPath(), "-Djava.class.path=" + path)
    classKraskov2 = JPackage("infodynamics.measures.continuous.kraskov").MultiInfoCalculatorKraskov2
    kraskov = classKraskov2()
    # Not sure if we need to set any properties (normalisation etc)
    # Not sure if we only have 2 joint variables
    kraskov.initialise(2)
    kraskov.setObservations(JArray(JDouble, 2)(data))
    information = kraskov.computeAverageLocalOfObservations()
    shutdownJVM()

    return information

    # http://lizier.me/joseph/software/jidt/javadocs/v1.3/infodynamics/measures/continuous/MultiInfoCalculator.html#computeAverageLocalOfObservations()
    # http://lizier.me/joseph/software/jidt/javadocs/v1.3/infodynamics/measures/continuous/kraskov/MultiInfoCalculatorKraskov2.html
