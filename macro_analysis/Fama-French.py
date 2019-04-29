import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


FamaFrench = pd.read_csv("data/FamaFrenchData.csv")

df = FamaFrench.iloc[:, 1:]
sns.pairplot(df)
plt.show()

df2 = FamaFrench.values
plt.scatter(df2[:, 1], df2[:, 3], s=np.abs(df2[:, 2]), c=df2[:, 0],
            cmap=plt.cm.RdGy)  # 동그라미 크기를 기업의 size로, 검은색일수록 최근 빨간색일수록 옛날
plt.colorbar()
plt.xlabel(FamaFrench.columns[1])
plt.ylabel(FamaFrench.columns[3])
plt.show()

# 결론
# 과거 데이터에는 저pbr과 수익률은 양의 관계를 가질 수 있지만 현재에 올수록 저pbr과 수익률은 음의 관계를 가진다.
# 최근 산업구조의 변화로 과거처럼 많은 사람, 공장, 기계가 필요로 하지않다. -> 앞으로 pbr과 small firm은 설명력이 높지 않다.
# 미래에는 특허나 저작권을 가치평가로 사용할 확률이 높다. ex)PTR
