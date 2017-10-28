# coding:utf-8
import scipy as sp
import scipy.stats
import pandas as pd

# タブ区切りのテキストデータを読み込む
data = pd.read_csv("data.txt", sep="\t")

# クロス集計をする
crossed = pd.crosstab(data.A, data.B)



x2, p, dof, expected = sp.stats.chi2_contingency(crossed)

print("カイ二乗値は %(x2)s" %locals() )
print("確率は %(p)s" %locals() )
print("自由度は %(dof)s" %locals() )
print( expected )

if p < 0.05:
  print("有意な差があります")
else:
  print("有意な差がありません")
