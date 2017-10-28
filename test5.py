# -*- coding:utf-8 -*-
# t 検定
#https://qiita.com/ynakayama/items/e41f592ad7fe02f23c1c
import numpy as np
import scipy as sp
from scipy import stats

X = [68, 75, 80, 71, 73, 79, 69, 65]
Y = [86, 83, 76, 81, 75, 82, 87, 75]

print(X)
print(Y)

t, p = stats.ttest_rel(X, Y)

print( "t 値は %(t)s" %locals() )
print( "確率は %(p)s" %locals() )

if p < 0.05:
    print("有意な差があります")
else:
    print("有意な差がありません")

# [68 75 80 71 73 79 69 65]
# [86 83 76 81 75 82 87 75]
# t 値は -2.9923203754253302
# 確率は 0.0201600161737
# 有意な差があります
