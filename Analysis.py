__author__ = 'stevenydc'
import numpy as np

# truth and pred are of type np.array
def eval(truth, pred):
    # Generating weight
    w = [[(i-j)**2 for j in range(1,9)] for i in range(1,9)]
    w = np.divide(w, float((8-1)**2))

    # Generating Histogram Matrix, O (letter)
    O = [np.array([sum((truth==i) & (pred==j)) for j in range(1,9)]) for i in range(1,9)]

    # Generating histogram matrix of expected ratings
    E = np.outer([sum(truth==i) for i in range(1,9)], [sum(pred==j) for j in range(1,9)])
    E = np.multiply(float(sum(sum(O)))/sum(sum(E)), E)
    # print E

    return 1-float(sum(sum(np.multiply(w,O))))/sum(sum(np.multiply(w,E)))
