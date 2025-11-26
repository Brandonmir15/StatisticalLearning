
import numpy as np

class SimpleLinearRegression:

    def __init__(self, inputs, outputs):

        self.inputs = inputs
        self.outputs = outputs
        self.slope = self.simpleLinearReggresion()[0]
        self.intercept = self.simpleLinearReggresion()[1]


    def simpleLinearReggresion(self) -> tuple:

        def avg(nums:list) -> float:
            return sum(nums)/len(nums)
    
        x_mean = avg(self.inputs)
        y_mean = avg(self.outputs)
        numerator = []
        denom = []

        for i in range(len(self.inputs)):

            diffX = self.inputs[i] - x_mean
            diffY = self.outputs[i] - y_mean
            prod = diffX * diffY
            numerator.append(prod)
            denom.append(diffX ** 2)
        
        numeratorSum = sum(numerator)
        denomSum = sum(denom) 
        slope = numeratorSum / denomSum
        intercept = y_mean - (slope * x_mean)

        return (slope,intercept)
    

    def predict(self, newInputs:list[float]) -> list[float]:
        
        result = []
        for eachInput in newInputs:
            prediction = (self.slope * eachInput) + self.intercept
            result.append(prediction)

        return result
    

class MultipleLinearRegression:

    def __init__(self, inputs, outputs, steps):

        self.inputs = inputs
        self.outputs = outputs
        self.weights = self.gradient_descent()

        



    def gradient_descent(self,step=0.01, itterations=1000):
        n = self.inputs.shape[0]
        p = self.inputs.shape[1]
        
    
        weights = np.zeros(p) # start off with a guess of the coeffients and work from there
        
        for i in range(itterations):
            prediction = self.inputs @ weights              #we are going to get our predicito
            error = prediction - self.outputs      
                
            gradient = (2/n) * (self.inputs.T @ error)  # gradient equation
            weights = weights - step * gradient       # update step
            

        return weights
    
   
    def predictions(self, newInputs:list[float]):
        X = np.array(X) # here we change our array to an np array
        if X.ndim == 1:
            X = X.reshape(1, -1)

        ones = np.ones((X.shape[0], 1)) 
        X = np.hstack((ones, X))

        return X @ self.weights




def avg(nums:list) -> float:
    return sum(nums)/len(nums)