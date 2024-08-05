import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def elbow(inputArg1):
    # 
    k_values = np.arange(1, inputArg1.shape[0] + 1)
    # 
    errors = np.zeros(len(k_values))

    # 
    for i, k in enumerate(k_values):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(inputArg1)
        errors[i] = np.sum(np.min(kmeans.transform(inputArg1), axis=1))

    # 
    plt.figure()
    plt.plot(k_values, errors, 'o-')
    plt.title('elbow map')
    plt.xlabel('cluster number')
    plt.ylabel('cluster difference')


    diff_errors = np.diff(errors)
    elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex

