import numpy as np
from scipy.optimize import leastsq

def f(x, p):
    a_, b_, c_, d_ = p

    return np.exp(a_ + b_/x + c_*np.log(x) + d_*np.power(x, 2.0))  # pv

    # return a_/np.power(b_, 1.0 + np.power(1.0 - x/c_, d_))  # rho

    #Tc = 649.13
    #Tr = x / Tc
    #return a_*np.power(1.0 - Tr, ((0.0*Tr + 0.0)*Tr + 0.0)*Tr + b_)  # hl

def err(p, y, x):
    a_, b_, c_, d_ = p
    return y - f(x, p)

p0 = (7.25177292e+01, -7.62519716e+03, -7.28935794e+00,  3.28917e-06)

X = np.array([250,280,300,330,350,400,450,500])
Y = np.array([7.534700e+00, 8.855539e+01, 3.387853e+02, 1.804621e+03,
              4.598329e+03, 2.994409e+04, 1.213473e+05, 3.583001e+05])

P = leastsq(err, p0, args=(Y, X))
print(P)


########################### Cached Data #############################
'''
#TMB - vapor pressure
p0 = (7.25177292e+01, -7.62519716e+03, -7.28935794e+00,  3.28917e-06)
Y = np.array([7.534700e+00, 8.855539e+01, 3.387853e+02, 1.804621e+03,
              4.598329e+03, 2.994409e+04, 1.213473e+05, 3.583001e+05])

#TMB - density
p0 = (7.25690829e+01, 2.59485174e-01, 6.49128824e+02, 2.77244022e-01)
Y = np.array([9.091213e+02, 8.864409e+02, 8.709069e+02, 8.469055e+02,
              8.303815e+02, 7.868793e+02, 7.393565e+02, 6.860078e+02])

#TMB - heat of vaporization
p0 = (4.81080524e+05, 3.41999853e-01)
Y = np.array([4.073629e+05, 3.966210e+05, 3.891365e+05, 3.773613e+05,
              3.691004e+05, 3.467194e+05, 3.211479e+05, 2.909107e+05])
'''
########################## End Cached Data ##########################

