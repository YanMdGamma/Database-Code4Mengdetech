import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 肘部图的绘制和选择
def elbow(inputArg1):
    # 设置聚类数量的范围
    k_values = np.arange(1, inputArg1.shape[0] + 1)
    # 初始化聚类误差存储向量
    errors = np.zeros(len(k_values))

    # 计算每个聚类数量下的聚类误差
    for i, k in enumerate(k_values):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(inputArg1)
        errors[i] = np.sum(np.min(kmeans.transform(inputArg1), axis=1))

    # 绘制肘部图
    plt.figure()
    plt.plot(k_values, errors, 'o-')
    plt.title('肘部图')
    plt.xlabel('聚类数量')
    plt.ylabel('聚类误差')

    # 寻找肘部位置
    diff_errors = np.diff(errors)
    elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex

