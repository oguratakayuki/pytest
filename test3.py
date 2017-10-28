# -*- coding:utf-8 -*-
# https://qiita.com/ynakayama/items/6b89cb451a73ae7a8990
import numpy as np
import scipy.stats

s = 204 # 表が出る回数
f = 196 # 裏が出る回数
e = 200 # 期待される回数

# 帰無仮説 (204:196)
observed = np.array([s,f])
# 対立仮説 (200:200)
expected = np.array([e,e])

# カイ二乗検定をおこなう
x2, p = scipy.stats.chisquare(observed, expected)

print("カイ二乗値は %(x2)s" %locals() )
print("確率は %(p)s" %locals() )

# 統計学的有意水準 0.05 より高いかどうか調べる
if p > 0.05:
    print("有意です")
else:
    print("有意ではありません")
