import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
import scipy.io as sio
import math

# 
def elbow(inputArg1):
    # 
    inputArg1 = inputArg1.T
    print(inputArg1.shape)
    input_data = pd.DataFrame(inputArg1)
    inputArg1 = input_data.drop_duplicates()  # 
    k_values = np.arange(1, inputArg1.shape[0] + 1)
    print(k_values)
    # 
    errors = np.zeros(len(k_values))
    print(errors)

    # 
    # warnings.filterwarnings("ignore", category= ConvergenceWarning)
    for i, k in enumerate(k_values):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(inputArg1)
        errors[i] = np.sum(np.min(kmeans.transform(inputArg1), axis=1))

    # 
    plt.figure()
    # plt.rcParams['font.family'] = 'SimHei' 
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    # 
    mpl.rcParams["axes.unicode_minus"] = False
    plt.plot(k_values, errors, 'o-')
    plt.title('Elbow Method')
    plt.xlabel('Cluster number')
    plt.ylabel('error')

    # 
    diff_errors = np.diff(errors)
    elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex + 1, k_values, errors

def threshold_interstitials(test_1_use, file):
    id_all = []
    id_pre = []
    id_all_id = []
    count_id = 0
    ide_all = []
    ide_d_final = []
    ied_e_final = []
    for i in range(test_1_use.shape[0]):
        if (int(test_1_use[i, 5]) == 1 or int(test_1_use[i, 5]) == 2) and test_1_use[i, 7] == 4:  # 增加了配位数的判断
            id_all.append(test_1_use[i, 6])
            id_pre.append(test_1_use[i, 8]/10)
            id_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_id += 1

    data_id = {'Similarity': id_all,
               'differ': id_pre,
               'id_id': id_all_id
    }

    input_data = pd.DataFrame(data_id)  # 
    print('input_data = ', file=file)
    print(input_data, file=file)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 
    id_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  
    print('id_all_without_du = ', id_all_without_du, file=file)
    print('deleted_rows = ', deleted_rows, file=file)

    id_all_without = id_all_without_du.to_numpy()
    id_all_without = id_all_without.T
    print('id_all_without = ', id_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    id_all = id_all_without[0, :]
    if id_all.shape[0] == 0:
        d_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(id_all) < 0.5:
        d_infimum_all = []
    elif id_all.shape[0] == 1:
        d_infimum_all = id_all_id
    elif id_all.shape[0] == 2 and np.max(id_all) > 0.5 and np.min(id_all) < np.max(
            id_all) * 0.8:  #
        id_pre = id_all_without[1, :]
        id_all_id = id_all_without[2, :]

        id_final = np.vstack((id_all, id_pre, id_all_id))
        d_infimum_all = []

        id_final1 = id_final[0, :]
        id_final1 = id_final1.tolist()
        index_d = id_final1.index(np.max(id_all))
        d_infimum_all.append(id_final[2, index_d])
        print('deleted_rows = ', deleted_rows.shape[1], file=file)

        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(id_all):
                    d_infimum_all.append(deleted_rows[2, i])
    else:
        id_pre = id_all_without[1, :]
        id_all_id = id_all_without[2, :]

        id_all = np.vstack((id_all, id_pre))
        id_final = np.vstack((id_all, id_all_id))
        print('id_all = ', id_all, file=file)

        # ia_all = np.sort(ia_all)

        id_min_1 = np.min(id_all[0, :])
        id_min_2 = np.min(id_all[1, :])
        # print('ia_min = ', ia_min)
        id_max_1 = np.max(id_all[0, :])
        id_max_2 = np.max(id_all[1, :])

        id_min = np.vstack((id_min_1, id_min_2))
        id_max = np.vstack((id_max_1, id_max_2))
        print('id_min = ', id_min, file=file)
        print('id_max = ', id_max, file=file)

        # 
        contains_positive = np.any(id_all[1, :] > 0)
        contains_negative = np.any(id_all[1, :] < 0)

        id_all = np.array(id_all)
        print(id_all)

        if contains_positive or contains_negative:
            elbowIndex_id, elbowid_k, elbowid_e = elbow(id_all)

            sio.savemat('elbowid_k.mat', {'elbowid_k': elbowid_k})
            sio.savemat('elbowid_e.mat', {'elbowid_e': elbowid_e})
            # elbowIndex_id = 3
            print(elbowIndex_id)
            #
            kmeans = KMeans(n_clusters=elbowIndex_id)
            #     print(ia_all)
            id_all = id_all.T
            idx_id = kmeans.fit_predict(id_all) + 1 # ia_all 23.9.2 
            #
            id_all = np.column_stack((id_all, idx_id))
            # #
            C_d = kmeans.cluster_centers_
            C_d = np.column_stack((C_d, np.arange(1, C_d.shape[0] + 1)))
            C_d = C_d[C_d[:, 0].argsort()]
            print('C_d = ', C_d, file=file)  # 
            print('---------------------------------------------', file=file)

            print('C_d[-1, -1] = ', C_d[-1, -1], file=file)
            print('---------------------------------------------', file=file)
            if C_d[-1, 0] <= 0.5:
                d_all_cate = []
            else:
                d_all_cate = id_all[id_all[:, -1] == C_d[-1, -1], 0]  # 

            # 
            ide = []
            for i in range(C_d.shape[0] - 1):
                if (C_d[C_d.shape[0] - i - 2, 0] > 0.7 * C_d[-1, 0] and C_d[C_d.shape[0] - i - 2, 0] >= 0.5) or math.ceil(C_d[C_d.shape[0] - i - 2, 0] * 10) >= 6:
                    d_all_cate = np.concatenate((d_all_cate, id_all[id_all[:, -1] == C_d[C_d.shape[0] - i - 2, -1], 0]))
                else:
                     ide = np.concatenate((ide, id_all[id_all[:, -1] == C_d[C_d.shape[0] - i - 2, -1], 0]))

            id_d_final = []
            c_d = 0
            id_final1 = id_final[0, :]
            id_final1 = id_final1.tolist()
            print(id_final1)


            if  np.array(d_all_cate).shape == 0:
                id_d_final = []
            else:
                for i in d_all_cate:
                    if i > 0.5:
                        print("The value of i is: ", i)
                        c_d += 1
                        if i in id_final[0, :]:
                            index_d = id_final1.index(i)
                            id_d_final.append(id_final[2, index_d])

                if deleted_rows.shape[1] != 0:
                    for i in range(deleted_rows.shape[1]):
                        if deleted_rows[0, i] in d_all_cate:
                            id_d_final.append(deleted_rows[2, i])

            #   
            ide_d_final = []
            if  np.array(ide).shape == 0:
                ide_d_final = []
            else:
                for i in ide:
                    c_d += 1
                    if i in id_final[0, :]:
                        index_d = id_final1.index(i)
                        # 
                        ide_d_final.append(id_final[2, index_d])

                if deleted_rows.shape[1] != 0:
                    for i in range(deleted_rows.shape[1]):
                        if deleted_rows[0, i] in d_all_cate:
                            ide_d_final.append(deleted_rows[2, i])
                # 
                for i in d_all_cate:
                    if i < 0.5:
                        print("i的值为：", i)
                        c_d += 1
                        if i in id_final[0, :]:
                            index_d = id_final1.index(i)
                            ide_d_final.append(id_final[2, index_d])

            # print(ia_all)
            # print(ia_all[:, 1])
            print('ide configuration Atomic ids of all id types-------------------------------------------', file=file)
            print(ide_d_final)
            print('d_all_cate = ', d_all_cate, file=file)
            print('-----------------------------------------------', file=file)
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------', file=file)
            d_infimum_all = id_d_final  # 
            print('id last recognition threshold', d_infimum_all, file=file)
            print('All the contents of the id configuration-----------------------------------------------', file=file)
        else:
            d_infimum_all = id_all_id
        print(d_infimum_all)

    #
    ie_all = []
    ie_pre = []
    ie_all_id = []
    count_ie = 0

    for i in range(test_1_use.shape[0]):
        if (int(test_1_use[i, 5]) == 3 or int(test_1_use[i, 5]) == 4) and test_1_use[i, 7] == 4:  # 
            ie_all.append(test_1_use[i, 6] * 10)
            ie_pre.append(test_1_use[i, 8])
            ie_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_ie += 1

    data_ie = {'Similarity': ie_all,
               'differ': ie_pre,
               'id_ie': ie_all_id
    }

    input_data = pd.DataFrame(data_ie)  # 
    print('input_data = ', file=file)
    print(input_data, file=file)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 
    ie_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  
    print('ie_all_without_du = ', ie_all_without_du, file=file)
    print('deleted_rows = ', deleted_rows, file=file)

    ie_all_without = ie_all_without_du.to_numpy()
    ie_all_without = ie_all_without.T
    print('ie_all_without = ', ie_all_without, file=file)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows, file=file)

    ie_all = ie_all_without[0, :]
    if ie_all.shape[0] == 0:
        e_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(ie_all) < 2:
        e_infimum_all = []
    elif ie_all.shape[0] == 1:
        e_infimum_all = ie_all_id
    elif ie_all.shape[0] == 2 and np.max(ie_all) > 2 and np.min(ie_all) < np.max(ie_all)*0.8: #  
        ie_pre = ie_all_without[1, :]
        ie_all_id = ie_all_without[2, :]

        ie_final = np.vstack((ie_all, ie_pre, ie_all_id))
        e_infimum_all = []

        ie_final1 = ie_final[0, :]
        ie_final1 = ie_final1.tolist()
        index_e = ie_final1.index(np.max(ie_all))
        e_infimum_all.append(ie_final[2, index_e])
        print('deleted_rows = ', deleted_rows.shape[1], file=file)
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(ie_all):
                    e_infimum_all.append(deleted_rows[2, i])
    else:
        ie_pre = ie_all_without[1, :]
        ie_all_id = ie_all_without[2, :]

        ie_all = np.vstack((ie_all, ie_pre))
        ie_final = np.vstack((ie_all, ie_all_id))
        print('ie_all = ', ie_all, file=file)

        # ia_all = np.sort(ia_all)

        ie_min_1 = np.min(ie_all[0, :])
        ie_min_2 = np.min(ie_all[1, :])
        # print('ia_min = ', ia_min)
        ie_max_1 = np.max(ie_all[0, :])
        ie_max_2 = np.max(ie_all[1, :])

        ie_min = np.vstack((ie_min_1, ie_min_2))
        ie_max = np.vstack((ie_max_1, ie_max_2))
        print('ie_min = ', ie_min, file=file)
        print('ie_max = ', ie_max, file=file)

        # 
        contains_positive = np.any(ie_all[1, :] > 0)
        contains_negative = np.any(ie_all[1, :] < 0)

        ie_all = np.array(ie_all)
        print(ie_all)

        if contains_positive or contains_negative:
            elbowIndex_ie, elbowie_k, elbowie_e = elbow(ie_all)

            sio.savemat('elbowie_k.mat', {'elbowie_k': elbowie_k})
            sio.savemat('elbowie_e.mat', {'elbowie_e': elbowie_e})
            # elbowIndex_ia = 8
            print(elbowIndex_ie)
            #
            kmeans = KMeans(n_clusters=elbowIndex_ie)
            #     print(ia_all)
            ie_all = ie_all.T
            idx_ie = kmeans.fit_predict(ie_all) + 1  
            #
            ie_all = np.column_stack((ie_all, idx_ie))
            # #
            C_e = kmeans.cluster_centers_
            C_e = np.column_stack((C_e, np.arange(1, C_e.shape[0] + 1)))
            C_e = C_e[C_e[:, 0].argsort()]
            print('C_e = ', C_e, file=file)  # 
            print('---------------------------------------------', file=file)

            print('C_e[-1, 1] = ', C_e[0, -1])
            print('---------------------------------------------', file=file)
            e_all_cate = []
            ied = []
            for i in range(C_e.shape[0]):
                if C_e[i, 0] > 5: # 
                    e_all_cate = np.concatenate((e_all_cate, ie_all[ie_all[:, -1] == C_e[i, -1], 0]))   # 
                elif C_e[i, 0] <= 5 and C_e[i, 0] >= 1:
                    ied = np.concatenate((e_all_cate, ie_all[ie_all[:, -1] == C_e[i, -1], 0]))

            id_e_final = []
            ied_e_final = []
            c_e = 0
            ie_final1 = ie_final[0, :]
            ie_final1 = ie_final1.tolist()
            print(ie_final1)

            for i in e_all_cate:
                c_e += 1
                if i in ie_final[0, :]:
                    index_e = ie_final1.index(i)
                    id_e_final.append(ie_final[2, index_e])

            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in e_all_cate:
                        id_e_final.append(deleted_rows[2, i])

#           
            for i in ied:
                c_e += 1
                if i in ie_final[0, :]:
                    index_e = ie_final1.index(i)
                    ied_e_final.append(ie_final[2, index_e])

            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in e_all_cate:
                        ied_e_final.append(deleted_rows[2, i])
            print('ide configuration Atomic ids of all ie types--------------------------------------', file=file)
            print(ied_e_final)
            # print(ia_all)
            # print(ia_all[:, 1])
            print('e_all_cate = ', e_all_cate)
            print('-----------------------------------------------', file=file)
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------', file=file)
            e_infimum_all = id_e_final  # 
            print('ie last recognition threshold: ', e_infimum_all, file=file)
            print('All the contents of the ie configuration-----------------------------------------------', file=file)
            # e_infimum_all = ie_all_id
            # print(e_infimum_all)
        else:
            e_infimum_all = ie_all_id
            print(e_infimum_all)

    ide_all = np.concatenate((ied_e_final, ide_d_final))
    return d_infimum_all, e_infimum_all, ide_all
    pass
