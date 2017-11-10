# -*- coding:utf-8 -*-
#カイ二乗検定（独立性の検定)
import scipy.stats
import numpy as np
#https://logics-of-blue.com/chi-squared-test/ 

house = [ [ 70,180 ], [ 30,120 ] ]
chi2, p, ddof, expected = scipy.stats.chi2_contingency( house )
msg = "Test Statistic: {}\np-value: {}\nDegrees of Freedom: {}\n"
print( msg.format( chi2, p, ddof ) )
print( ddof )

#https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
#数値の配列同士に対して、計算式を適用した配列を作成
ret = [ ((x - y) ** 2) / y for x, y in zip(house, expected)]
ret = np.sum(ret)
print(ret)

#https://stackoverflow.com/questions/11725115/p-value-from-chi-sq-test-statistic-in-python
print(1 - scipy.stats.chi2.cdf(ret, ddof))
