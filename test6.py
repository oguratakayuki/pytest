# -*- coding:utf-8 -*-
#適合性の検定
# http://www.geisya.or.jp/~mwm48961/statistics/kai2.htm
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.stats.chi2.html
import numpy as np
import scipy.stats
from scipy.stats import chi2


s = [47,18,27,8]
e = [40,20,30,10]

observed = np.array(s)
expected = np.array(e)

# カイ二乗検定をおこなう
x2, p = scipy.stats.chisquare(observed, expected)

print("カイ二乗値は %(x2)s" %locals() )
print("確率は %(p)s" %locals() )


#自由度3のχ2分布において，有意水準5%の限界値
yuui = chi2.ppf(0.95, 3)
print(yuui)
if p > yuui:
    print("有意です")
else:
    print("有意ではありません")
