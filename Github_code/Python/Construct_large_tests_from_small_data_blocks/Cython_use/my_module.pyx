import numpy as np

def dis_r(x_4, y_4, z_4, x_s4, y_s4, z_s4):
    dis_r = np.sqrt((x_4 - x_s4) ** 2 + (y_4 - y_s4) ** 2 + (z_4 - z_s4) ** 2)
    return dis_r

def all_RDF(n_0620_t1, particle_rdf_test0620_1, radias_vol, n):
    for num_test1 in range(n_0620_t1.shape[0]):
        test0620_coordination1 = n_0620_t1[num_test1, 2:5]
        for c in range(n):
            count = 0
            for i in range(n_0620_t1.shape[0]):
                if dis_r(test0620_coordination1[0], test0620_coordination1[1], test0620_coordination1[2], n_0620_t1[i, 2], n_0620_t1[i, 3], n_0620_t1[i, 4]) <= radias_vol[c, 0]:
                    count += 1
            particle_rdf_test0620_1[c, 2 * num_test1] = (count - 1) / radias_vol[c, 1]
            particle_rdf_test0620_1[c, 2 * num_test1 + 1] = count - 1
    return particle_rdf_test0620_1