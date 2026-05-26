import numpy as np

'''
f is n entry function, 
x is a point to evaluate f where len(x)=n
f outputs list where len = m
'''

def gradient(f, x, i, h=1e-5):
    x_plus  = x.copy(); x_plus[i]  += h
    x_minus = x.copy(); x_minus[i] -= h
    return (np.array(f(x_plus)) - np.array(f(x_minus))) / (2*h)

def jacobian_matrix(f, x: list[float]) -> list[list[float]]:
    J = []
    for i in range(len(x)):
        J.append(gradient(f,x,i))
    return np.transpose(J)