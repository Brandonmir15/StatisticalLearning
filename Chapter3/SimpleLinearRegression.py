
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


def main() -> None:

    x = [1, 3, 5, 7, 9, 11]
    y = [10, 15, 22, 26, 30, 36]

    model1 = SimpleLinearRegression(x,y)

    newValues = [2,14,19]
    predictions = model1.predict(newValues)
    print(predictions)

if __name__ == '__main__':
    main()