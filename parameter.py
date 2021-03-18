import math
import numpy as np

def evaluate(values):
    Y = np.zeros([values.shape[0]])
    Gr = 1000.00
    A = 0.6
    for i, x in enumerate(values):
       Y[i] = (16*1.38e-23/(3*x[0])) + ((A * 0.33 * x[1] + (0.025 * (0.18 * math.pow(Gr, 0.25)/math.pow(x[2]/x[3], 0.1)) * (1 - x[1]))) + (1 - A) * (((4.5e-3 * math.pow(Gr, 0.25) / math.pow((x[2]/x[3]), 0.1)) * 0.33) /
                                         (x[1] * 4.5e-3 * (math.pow(Gr, 0.25) / math.pow((x[2]/[x[3]]), 0.1)) + 0.33 * (1 - x[1]))))

    return Y