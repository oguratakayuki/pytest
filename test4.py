# -*- coding:utf-8 -*-
#適合性の検定
# http://www.geisya.or.jp/~mwm48961/statistics/kai2.htm
# https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.stats.chi2.html
import numpy as np
import scipy.stats
from scipy.stats import chi2

s = [37,25,12,26]
e = [40,20,10,30]

# 帰無仮説 (204:196)
observed = np.array(s)
# 対立仮説 (200:200)
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
