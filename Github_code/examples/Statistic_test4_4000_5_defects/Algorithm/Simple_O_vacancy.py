import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
import scipy.io as sio

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
    elbowIndex = -1  # Default value
    if diff_errors.size > 0:
        elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex + 1, k_values, errors

def Simple_O_vacancy(test_1_use):
    O1_all = []
    O1_pre = []
    O1_all_id = []
    O1_all_differ = [] # 
    count_O1 = 0

    for i in range(test_1_use.shape[0]):
        col_judge = test_1_use.shape[1]
        if (int(test_1_use[i, 5]) == 1 or int(test_1_use[i, 5]) == 2) and int(test_1_use[i, 7]) == 3:  # 
            O1_all.append(test_1_use[i, 6])
            O1_pre.append(test_1_use[i, 8])
            O1_all_id.append(test_1_use[i, 0])
            if col_judge < 11:
                O1_all_differ.append(test_1_use[i, 6])
            else:
                O1_all_differ.append(test_1_use[i, 10])

            if int(test_1_use[i, 6]) == 1:
                count_O1 += 1

    data_ia = {'Similarity': O1_all,
               'differ': O1_pre,
               'id_ic': O1_all_id,
               'differ_max': O1_all_differ
    }

    input_data = pd.DataFrame(data_ia)  # 
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 
    O1_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  
    print('O1_all_without_du = ', O1_all_without_du)
    print('deleted_rows = ', deleted_rows)

    O1_all_without = O1_all_without_du.to_numpy()
    O1_all_without = O1_all_without.T
    print('O1_all_without = ', O1_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    O1_all = O1_all_without[0, :]

    if O1_all.shape[0] == 0:
        O1_infimum_all = []
    elif np.max(O1_all) < 0.5 : # 0.5
        O1_infimum_all = []
    elif O1_all.shape[0] == 1:
        O1_infimum_all = O1_all_id
    elif O1_all.shape[0] == 2 and np.max(O1_all) > 0.5 and np.min(O1_all) < np.max(
        O1_all) * 0.7:  # 
        O1_pre = O1_all_without[1, :]
        O1_all_id = O1_all_without[2, :]

        # ia_final = np.vstack((ia_all, ia_pre, ia_all_id, ia_all_differ))
        O1_final = np.vstack((O1_all, O1_pre, O1_all_id))
        O1_infimum_all = []

        O1_final1 = O1_final[0, :]
        O1_final1 = O1_final1.tolist()
        index_O1 = O1_final1.index(np.max(O1_all))
        O1_infimum_all.append(O1_final[2, index_O1])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(O1_all):
                    O1_infimum_all.append(deleted_rows[2, i])

    else:
        O1_pre = O1_all_without[1, :]
        O1_all_id = O1_all_without[2, :]
        O1_all_differ = O1_all_without[3, :]
        # 
        # 
        O1_all = np.vstack((O1_all, O1_pre, O1_all_differ))
        O1_final = np.vstack((O1_all, O1_all_id))
        print('O1_all = ', O1_all)

        # ia_all = np.sort(ia_all)

        O1_min_1 = np.min(O1_all[0, :])
        O1_min_2 = np.min(O1_all[1, :])
        # print('ia_min = ', ia_min)
        O1_max_1 = np.max(O1_all[0, :])
        O1_max_2 = np.max(O1_all[1, :])

        O1_min = np.vstack((O1_min_1, O1_min_2))
        O1_max = np.vstack((O1_max_1, O1_max_2))
        print('O1_min = ', O1_min)
        print('O1_max = ', O1_max)

        # 
        contains_positive = np.any(O1_all[1, :] > 0)
        contains_negative = np.any(O1_all[1, :] < 0)

        O1_all = np.array(O1_all)
        print(O1_all)

        if contains_positive or contains_negative:
            elbowIndex_O1, elbowO1_k, elbowO1_e = elbow(O1_all)

            sio.savemat('elbowO1_k.mat', {'elbowO1_k': elbowO1_k})
            sio.savemat('elbowO1_e.mat', {'elbowO1_e': elbowO1_e})

            # elbowIndex_ia = 8
            print("elbowIndex_O1", elbowIndex_O1)
            if elbowIndex_O1 == 0: # 
                elbowIndex_O1 = 1
            #
            kmeans = KMeans(n_clusters=elbowIndex_O1)
            #     print(ia_all)
            O1_all = O1_all.T
            idx_O1 = kmeans.fit_predict(O1_all) + 1  # ia_all 23.9.2 
            #
            O1_all = np.column_stack((O1_all, idx_O1))
            # #
            C_O1 = kmeans.cluster_centers_
            C_O1 = np.column_stack((C_O1, np.arange(1, C_O1.shape[0] + 1)))
            C_O1 = C_O1[C_O1[:, 0].argsort()]
            print("C_O1", C_O1)
            count = 0
            # for i in range(C_a.shape[0]):
            #     print(C_a.shape[1])
            #     if C_a.shape[1] > 2:
            #         if abs(C_a[i, 2]) > 0.045: # 0.0045
            #             C_a = np.delete(C_a, i, axis=0)
            #     else:
            #         C_a = C_a

            O1_all_cate = []
            O1_all_cate = np.concatenate((O1_all_cate, O1_all[O1_all[:, -1] == C_O1[-1, -1], 0]))

            # 
            print('24.1.5: O1_all_cate:', O1_all_cate)

            for i in range(C_O1.shape[0] - 1):
                if C_O1[C_O1.shape[0] - i - 2, 0] > 0.91 * C_O1[-1, 0]:
                    O1_all_cate = np.concatenate((O1_all_cate, O1_all[O1_all[:, -1] == C_O1[C_O1.shape[0] - i - 2, -1], 0]))

            print('C_O1 = ', C_O1)  # 
            print('---------------------------------------------')

            print('C_O1[-1, 1] = ', C_O1[0, -1])
            print('---------------------------------------------')
              # 

            id_O1_final = []
            c_O1 = 0
            O1_final1 = O1_final[0, :]
            O1_final1 = O1_final1.tolist()
            print(O1_final1)

            for i in O1_all_cate:
                c_O1 += 1
                if i in O1_final[0, :]:
                    index_O1 = O1_final1.index(i)
                    id_O1_final.append(O1_final[3, index_O1])
                    print('24.1.5:id_O1_final:', O1_final[3, index_O1])

            # 
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in O1_all_cate:
                        id_O1_final.append(deleted_rows[2, i])
                        print('24.1.5:deleted_rows[2, i]:', deleted_rows[2, i])
            # print(ia_all)
            # print(ia_all[:, 1])
            print('O1_all_cate = ', O1_all_cate)
            print('-----------------------------------------------')
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------')
            O1_infimum_all = id_O1_final  # 
            print('O1 last recognition threshold: ', O1_infimum_all)
            print('All the contents of the O1 configuration-----------------------------------------------')
        else:
            O1_infimum_all = O1_all_id
            print(O1_infimum_all)
    #
    O2_all = []
    O2_pre = []
    O2_all_id = []
    count_O2 = 0

    for i in range(test_1_use.shape[0]):
        if (int(test_1_use[i, 5]) == 3 or int(test_1_use[i, 5]) == 4) and int(test_1_use[i, 7]) == 3:  # 
            O2_all.append(test_1_use[i, 6])
            O2_pre.append(test_1_use[i, 8])
            O2_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_O2 += 1

    data_ib = {'Similarity': O2_all,
               'differ': O2_pre,
               'id_O2': O2_all_id
    }

    input_data = pd.DataFrame(data_ib)  # 
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 
    O2_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  
    print('O2_all_without_du = ', O2_all_without_du)
    print('deleted_rows = ', deleted_rows)

    O2_all_without = O2_all_without_du.to_numpy()
    O2_all_without = O2_all_without.T
    print('O2_all_without = ', O2_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    O2_all = O2_all_without[0, :]

    if O2_all.shape[0] == 0:
        O2_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(O2_all) < 0.5:
        O2_infimum_all = []
    elif O2_all.shape[0] == 1:
        O2_infimum_all = O2_all_id
    elif O2_all.shape[0] == 2 and np.max(O2_all) > 0.5 and np.min(O2_all) < np.max(O2_all)*0.8: # 
        O2_pre = O2_all_without[1, :]
        O2_all_id = O2_all_without[2, :]

        O2_final = np.vstack((O2_all, O2_pre, O2_all_id))
        O2_infimum_all = []

        O2_final1 = O2_final[0, :]
        O2_final1 = O2_final1.tolist()
        index_O2 = O2_final1.index(np.max(O2_all))
        O2_infimum_all.append(O2_final[2, index_O2])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(O2_all):
                    O2_infimum_all.append(deleted_rows[2, i])
    else:
        #  
        O2_pre = O2_all_without[1, :]
        O2_all_id = O2_all_without[2, :]

        O2_all = np.vstack((O2_all, O2_pre))
        O2_final = np.vstack((O2_all, O2_all_id))
        print('O2_final = ', O2_all)

        # ia_all = np.sort(ia_all)

        O2_min_1 = np.min(O2_all[0, :])
        O2_min_2 = np.min(O2_all[1, :])
        # print('ia_min = ', ia_min)
        O2_max_1 = np.max(O2_all[0, :])
        O2_max_2 = np.max(O2_all[1, :])

        O2_min = np.vstack((O2_min_1, O2_min_2))
        O2_max = np.vstack((O2_max_1, O2_max_2))
        print('O2_min = ', O2_min)
        print('O2_max = ', O2_max)
        # 
        contains_positive = np.any(O2_all[1, :] > 0)
        contains_negative = np.any(O2_all[1, :] < 0)

        O2_all = np.array(O2_all)

        if contains_positive or contains_negative:
            elbowIndex_O2, elbowO2_k, elbowO2_e = elbow(O2_all)

            sio.savemat('elbowO2_k.mat', {'elbowO2_k': elbowO2_k})
            sio.savemat('elbowO2_e.mat', {'elbowO2_e': elbowO2_e})
            # elbowIndex_ia = 8
            print(elbowIndex_O2)
            #
            kmeans = KMeans(n_clusters=elbowIndex_O2)
            #     print(ia_all)
            O2_all = O2_all.T
            idx_O2 = kmeans.fit_predict(O2_all) + 1 # ia_all 23.9.2 
            #
            O2_all = np.column_stack((O2_all, idx_O2))
            # #
            C_O2 = kmeans.cluster_centers_
            C_O2 = np.column_stack((C_O2, np.arange(1, C_O2.shape[0] + 1)))
            C_O2 = C_O2[C_O2[:, 0].argsort()]

            print('C_O2 = ', C_O2)  # 
            print('---------------------------------------------')

            print('C_O2[-1, 1] = ', C_O2[-1, -1])
            print('---------------------------------------------')
            O2_all_cate = O2_all[O2_all[:, -1] == C_O2[-1, -1], 0]  # 
            for i in range(C_O2.shape[0] - 1):
                if C_O2[C_O2.shape[0] - i - 2, 0] > 0.5:
                    O2_all_cate = np.concatenate((O2_all_cate, O2_all[O2_all[:, -1] == C_O2[C_O2.shape[0] - i - 2, -1], 0]))
            id_O2_final = []
            c_O2 = 0
            O2_final1 = O2_final[0, :]
            O2_final1 = O2_final1.tolist()
            print(O2_final1)

            for i in O2_all_cate:
                c_O2 += 1
                if i in O2_final[0, :]:
                    index_O2 = O2_final1.index(i)
                    id_O2_final.append(O2_final[2, index_O2])

            # 
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in O2_all_cate:
                        id_O2_final.append(deleted_rows[2, i])
            print('O2_all_cate = ', O2_all_cate)
            print('-----------------------------------------------')
            # print('np.min(b_all_cate)', np.min(b_all_cate))
            print('-----------------------------------------')
            O2_infimum_all = id_O2_final  # 
            print('O2 last recognition threshold: ', O2_infimum_all)
            print('All the contents of the O2 configuration-----------------------------------------------')
        else:
            O2_infimum_all = O2_all_id
            print(O2_infimum_all)

    O3_all = []
    O3_pre = []
    O3_all_id = []
    count_O3 = 0

    for i in range(test_1_use.shape[0]):
        if (int(test_1_use[i, 5]) == 5 or int(test_1_use[i, 5]) == 6) and int(test_1_use[i, 7]) == 4:
            O3_all.append(test_1_use[i, 6])
            O3_pre.append(test_1_use[i, 8])
            O3_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_O3 += 1

    data_ic = {'Similarity': O3_all,
               'differ': O3_pre,
               'id_ic': O3_all_id
    }

    input_data = pd.DataFrame(data_ic)  # 
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 
    O3_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  
    print('O3_all_without_du = ', O3_all_without_du)
    print('deleted_rows = ', deleted_rows)

    O3_all_without = O3_all_without_du.to_numpy()
    O3_all_without = O3_all_without.T
    print('O3_all_without = ', O3_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    O3_all = O3_all_without[0, :]

    if O3_all.shape[0] == 0: #  
        O3_infimum_all = []
    elif np.max(O3_all) < 0.5:
        O3_infimum_all = []
    elif O3_all.shape[0] == 1:
        O3_infimum_all = O3_all_id
    elif O3_all.shape[0] == 2 and np.max(O3_all) > 0.5 and np.min(O3_all) < np.max(
        O3_all) * 0.7:  # 
        O3_pre = O3_all_without[1, :]
        O3_all_id = O3_all_without[2, :]

        O3_final = np.vstack((O3_all, O3_pre, O3_all_id))
        O3_infimum_all = []

        O3_final1 = O3_final[0, :]
        O3_final1 = O3_final1.tolist()
        index_O3 = O3_final1.index(np.max(O3_all))
        O3_infimum_all.append(O3_final[2, index_O3])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(O3_all):
                    O3_infimum_all.append(deleted_rows[2, i])

    else:
        #  
        O3_pre = O3_all_without[1, :]
        O3_all_id = O3_all_without[2, :]

        O3_all = np.vstack((O3_all, O3_pre))
        O3_final = np.vstack((O3_all, O3_all_id))
        print('O3_final = ', O3_final)
        print('O3_all = ', O3_all)
        # ia_all = np.sort(ia_all)

        O3_min_1 = np.min(O3_all[0, :])
        O3_min_2 = np.min(O3_all[1, :])
        # print('ia_min = ', ia_min)
        O3_max_1 = np.max(O3_all[0, :])
        O3_max_2 = np.max(O3_all[1, :])

        O3_min = np.vstack((O3_min_1, O3_min_2))
        O3_max = np.vstack((O3_max_1, O3_max_2))
        print('O3_min = ', O3_min)
        print('O3_max = ', O3_max)

        # 
        contains_positive = np.any(O3_all[1, :] > 0)
        contains_negative = np.any(O3_all[1, :] < 0)

        O3_all = np.array(O3_all)
        print(O3_all)

        if contains_positive or contains_negative:
            elbowIndex_O3, elbowO3_k, elbowO3_e = elbow(O3_all)

            sio.savemat('elbowO3_k.mat', {'elbowO3_k': elbowO3_k})
            sio.savemat('elbowO3_e.mat', {'elbowO3_e': elbowO3_e})
            # elbowIndex_ia = 8
            print(elbowIndex_O3)

            kmeans = KMeans(n_clusters=elbowIndex_O3)
            #     print(ia_all)
            O3_all = O3_all.T
            idx_O3 = kmeans.fit_predict(O3_all) + 1  # ia_all 23.9.2 
            #
            O3_all = np.column_stack((O3_all, idx_O3))
            # #
            C_O3 = kmeans.cluster_centers_
            C_O3 = np.column_stack((C_O3, np.arange(1, C_O3.shape[0] + 1)))
            C_O3 = C_O3[C_O3[:, 0].argsort()]
            print('C_O3 = ', C_O3)  # 
            print('---------------------------------------------')

            print('C_O3[-1, 1] = ', C_O3[-1, -1])
            print('---------------------------------------------')
            O3_all_cate = O3_all[O3_all[:, -1] == C_O3[-1, -1], 0]  # 

            for i in range(C_O3.shape[0] - 1):
                if C_O3[C_O3.shape[0] - i - 2, 0] > 0.5:
                    O3_all_cate = np.concatenate((O3_all_cate, O3_all[O3_all[:, -1] == C_O3[C_O3.shape[0] - i - 2, -1], 0]))

            id_O3_final = []
            c_O3 = 0
            O3_final1 = O3_final[0, :]
            O3_final1 = O3_final1.tolist()
            print(O3_final1)

            for i in O3_all_cate: #  
                c_O3 += 1
                if i in O3_final[0, :]:
                    index_O3 = O3_final1.index(i)
                    id_O3_final.append(O3_final[2, index_O3])

            # 
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in O3_all_cate:
                        id_O3_final.append(deleted_rows[2, i])

            print('O3_all_cate = ', O3_all_cate)
            print('-----------------------------------------------')
            print('np.min(O3_all_cate)', np.min(O3_all_cate))
            print('-----------------------------------------')
            O3_infimum_all = id_O3_final  # 
            print('O3 last recognition threshold: ', O3_infimum_all)
            print('All the contents of the O3 configuration-----------------------------------------------')
        else:
            O3_infimum_all = O3_all_id
            print(O3_infimum_all)
    #
    return O1_infimum_all, O2_infimum_all, O3_infimum_all

