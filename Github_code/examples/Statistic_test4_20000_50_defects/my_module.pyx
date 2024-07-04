import numpy as np

def dis_r(x_4, y_4, z_4, x_s4, y_s4, z_s4):
    dis_r = np.sqrt((x_4 - x_s4) ** 2 + (y_4 - y_s4) ** 2 + (z_4 - z_s4) ** 2)
    return dis_r

def all_RDF(n_0620_t1, n_0620_t1_add, particle_rdf_test0620_1, radias_vol, n):
    # 另一个方法
    distances = np.zeros((n_0620_t1.shape[0], n_0620_t1_add.shape[0]))  # 创建一个全零矩阵用于存储距离
    data_all = n_0620_t1_add[:, 2:5]
    data_all = np.array(data_all)
    # print(data_all)
    for i in range(n_0620_t1.shape[0]): # 首先统计出每一个粒子的
        for j in range(n_0620_t1_add.shape[0]):
            distances[i][j] = np.linalg.norm(data_all[i] - data_all[j])
    # print(distances)
    for i in range(n_0620_t1.shape[0]): # 再用i表示待统计的粒子
        for c in range(n):
            count = 0
            id_all = []

            for j in range(n_0620_t1_add.shape[0]): # 对应另一个粒子之间的距离
                if distances[i][j] <= radias_vol[c, 0] and n_0620_t1_add[j, 0] not in id_all:
                    count += 1
                    id_all.append(n_0620_t1_add[j, 0])

            particle_rdf_test0620_1[c, 2 * i] = (count - 1) / radias_vol[c, 1]
            particle_rdf_test0620_1[c, 2 * i + 1] = count - 1

    return particle_rdf_test0620_1
