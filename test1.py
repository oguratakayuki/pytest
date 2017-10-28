import numpy as np
from scipy import stats

o = np.array([12, 10, 9, 9, 13, 7])
e = np.array([10, 10, 10, 10, 10, 10])

print stats.chisquare(o, f_exp = e)
