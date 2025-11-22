"""
This file will just contain some of the algorithms we implimented throught this chatper

"""


# this function takes in an array of tuples, the tuples being the points
def simpleReggresion(points:list) -> list:

    predictions = []
    
    pointsDict = {}
    # Here we can store our points in a dict
    for eachPoint in points:
        if(eachPoint[0]) not in pointsDict:
            pointsDict[eachPoint[0]] = []
        pointsDict[eachPoint[0]].append(eachPoint[1])

    for x0 in pointsDict:

        predSum = sum(pointsDict[x0])
        avg = round(predSum/len(pointsDict[x0]),2)
        predictions.append((x0, avg))


    return predictions


def neighborhoodRegression(points:dict, neighborhood=0.4) -> list:

    # so for this function we will make the neighboor hood size 0.4 in both directions
    pointsDict = {}
    #Here we are using a for loop to store each x with its y values in a dict
    for eachPoint in points:
        if eachPoint[0] not in pointsDict:
            pointsDict[eachPoint[0]] = []                   # this will store the x as a key with [] as a value
        pointsDict[eachPoint[0]].append(eachPoint[1])

    results = []

    for x0 in range(10):
        
        # for each number we are gonna want to check if it has its nweigbors in its neigborhood
        neighbors = []

        # if there is an x in out neighbor we will add its Y value to our neighboors
        for x in pointsDict:
            if abs(x - x0) <= neighborhood:
                for y in pointsDict[x]:
                    neighbors.append(y) 

      
       
        if len(neighbors) > 0:
            prediction = round(sum(neighbors) / len(neighbors),2 )# this gets the average
        else:
            prediction = None
        

        results.append((x0, prediction)) # then we will append that average to our results

    return results


# i need to fix ther parameters here to make it more compatible with the above functions
def meanSquaredError(trueValues:list, predictedValues:list) -> float:
    
    vals = []
    for i in range(len(predictedValues)):
        
       error = trueValues[i] - predictedValues[i]

       squaredError = error ** 2

       vals.append(squaredError)
    

    mse = round(sum(vals) / len(predictedValues), 2)

    return mse