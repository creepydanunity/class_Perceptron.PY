from math import exp
from random import random


class Perceptron:
    def __init__(self, inputs=1):
        self.weights = [random() / 2 for i in range(inputs)]
        self.bias = random() / 2

    def __activation(self, x, dev=False):
        if not dev:
            return 1 / (1 + exp(-x))
        else:
            return self.__activation(x) * (1 - self.__activation(x))

    def __summator(self, x):
        s = self.bias
        for i in range(len(x)):
            s += self.weights[i] * x[i]
        return s

    def predict(self, x):
        return self.__activation(self.__summator(x))

    def train(self, x, y, lr=0.3):
        y_predicted = self.predict(x)
        error = y - y_predicted
        delta_w = error * self.__activation(self.__summator(x), dev=True)
        for i in range(len(x)):
            self.weights[i] += delta_w * lr * x[i]
        self.bias += delta_w * lr

