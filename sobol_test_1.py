from SALib.sample import saltelli
from SALib.analyze import sobol
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


# Define the model inputs
problem = {
'num_vars':4,
'names': ['x1', 'x2', 'x3', 'x4'],
'bounds':[[0.06, 0.09],
          [0.2, 0.8],
          [200.00, 600.00],
          [50.00, 200.00]]
}
# Generate samples
param_values = saltelli.sample(problem, 20000)
# Run model (function)
Y = evaluate(param_values)
# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True )
# Print the first-order sensitivity indices
# print(Si['S1'])

