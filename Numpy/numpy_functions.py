import numpy as np

def det(matrix):
    if matrix.size==1:
        return matrix[0,0]
    if matrix.ndim!=2:
        raise Exception("matrix not two-dimensional")
    if matrix.shape[0]!=matrix.shape[1]:
        raise Exception("matrix not quadratic")
    determinant = 0
    for i in range(0,matrix.shape[0],2):
        determinant += matrix[0,i]*det(np.concatenate((matrix[1:,0:i],matrix[1:,i+1:]),axis=1))
    for i in range(1,matrix.shape[0],2):
        determinant -= matrix[0,i]*det(np.concatenate((matrix[1:,0:i],matrix[1:,i+1:]),axis=1))
    return determinant

def tr(matrix):
    if matrix.size==1:
        return matrix[0,0]
    if matrix.ndim!=2:
        raise Exception("matrix not two-dimensional")
    if matrix.shape[0]!=matrix.shape[1]:
        raise Exception("matrix not quadratic")
    trace = 0
    for i in range(matrix.shape[0]):
        trace += matrix[i,i]
    return trace
