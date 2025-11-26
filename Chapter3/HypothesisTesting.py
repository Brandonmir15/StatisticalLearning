from Chapter3Algos import avg
import math


def variance(trueValues:list, predictedValues:list) -> float:
    
    vals = []
    for i in range(len(predictedValues)):
        
       error = trueValues[i] - predictedValues[i]
       squaredError = error ** 2
       vals.append(squaredError)
    
    var = sum(vals) / (len(predictedValues) - 2)

    return var

def sumOfSquares(x:list):
    mean = avg(x)
    squaredErrors = []
    for eachNum in x:
        error = eachNum - mean
        squaredError = error ** 2
        squaredErrors.append(squaredError)

    return sum(squaredErrors)


def standardErrorWeights(x:list, trueValues:list, predictedValues:list) -> float:

    sigmaSquared = variance(trueValues, predictedValues)
    sumOfSquaresValue = sumOfSquares(x)

    se = math.sqrt(sigmaSquared / sumOfSquaresValue)
    return se


def standardErrorIntercepts(x:list, trueValues:list, predictedValues:list): #impliment later
    pass