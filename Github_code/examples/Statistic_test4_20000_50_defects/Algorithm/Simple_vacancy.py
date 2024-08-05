import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
import scipy.io as sio

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

    plt.figure()
    # plt.rcParams['font.family'] = 'SimHei'  
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
 
    mpl.rcParams["axes.unicode_minus"] = False
    plt.plot(k_values, errors, 'o-')
    plt.title('Elbow Method')
    plt.xlabel('Cluster number')
    plt.ylabel('error')


    diff_errors = np.diff(errors)
    elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex + 1, k_values, errors

def Simple_vacancy(test_1_use):
    Ga1_all = []
    Ga1_pre = []
    Ga1_all_id = []
    count_Ga1 = 0
    # ide_all = []
    # ide_d_final = []
    # ied_e_final = []
    for i in range(test_1_use.shape[0]):
        if int(test_1_use[i, 5]) == 8 and test_1_use[i, 7] == 6: 
            Ga1_all.append(test_1_use[i, 6])
            Ga1_pre.append(test_1_use[i, 8]/10)
            Ga1_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_Ga1 += 1

    data_Ga1 = {'Similarity': Ga1_all,
               'differ': Ga1_pre,
               'id_ic': Ga1_all_id
    }

    input_data = pd.DataFrame(data_Ga1)  
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')] 
    Ga1_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first') 
    print('Ga1_all_without_du = ', Ga1_all_without_du)
    print('deleted_rows = ', deleted_rows)

    Ga1_all_without = Ga1_all_without_du.to_numpy()
    Ga1_all_without = Ga1_all_without.T
    print('Ga1_all_without = ', Ga1_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    Ga1_all = Ga1_all_without[0, :]
    if Ga1_all.shape[0] == 0:
        Ga1_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(Ga1_all) < 0.5:
        Ga1_infimum_all = []
    elif Ga1_all.shape[0] == 1:
        Ga1_infimum_all = Ga1_all_id
    elif Ga1_all.shape[0] == 2 and np.max(Ga1_all) > 0.5 and np.min(Ga1_all) < np.max(
            Ga1_all) * 0.8: 
        Ga1_pre = Ga1_all_without[1, :]
        Ga1_all_id = Ga1_all_without[2, :]

        Ga1_final = np.vstack((Ga1_all, Ga1_pre, Ga1_all_id))
        Ga1_infimum_all = []

        Ga1_final1 = Ga1_final[0, :]
        Ga1_final1 = Ga1_final1.tolist()
        index_Ga1 = Ga1_final1.index(np.max(Ga1_all))
        Ga1_infimum_all.append(Ga1_final[2, index_Ga1])
        print('deleted_rows = ', deleted_rows.shape[1])

        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(Ga1_all):
                    Ga1_infimum_all.append(deleted_rows[2, i])
    else:
        Ga1_pre = Ga1_all_without[1, :]
        Ga1_all_id = Ga1_all_without[2, :]

        Ga1_all = np.vstack((Ga1_all, Ga1_pre))
        Ga1_final = np.vstack((Ga1_all, Ga1_all_id))
        print('Ga1_all = ', Ga1_all)

        # ia_all = np.sort(ia_all)

        Ga1_min_1 = np.min(Ga1_all[0, :])
        Ga1_min_2 = np.min(Ga1_all[1, :])
        # print('ia_min = ', ia_min)
        Ga1_max_1 = np.max(Ga1_all[0, :])
        Ga1_max_2 = np.max(Ga1_all[1, :])

        Ga1_min = np.vstack((Ga1_min_1, Ga1_min_2))
        Ga1_max = np.vstack((Ga1_max_1, Ga1_max_2))
        print('Ga1_min = ', Ga1_min)
        print('Ga1_max = ', Ga1_max)

        contains_positive = np.any(Ga1_all[1, :] > 0)
        contains_negative = np.any(Ga1_all[1, :] < 0)

        Ga1_all = np.array(Ga1_all)
        print(Ga1_all)

        if contains_positive or contains_negative:
            elbowIndex_id, elbowid_k, elbowid_e = elbow(Ga1_all)

            sio.savemat('elbowid_k.mat', {'elbowid_k': elbowid_k})
            sio.savemat('elbowid_e.mat', {'elbowid_e': elbowid_e})
            # elbowIndex_id = 3
            print(elbowIndex_id)
            #
            kmeans = KMeans(n_clusters=elbowIndex_id)
            #     print(ia_all)
            Ga1_all = Ga1_all.T
            Ga1x_id = kmeans.fit_predict(Ga1_all) + 1
            #
            Ga1_all = np.column_stack((Ga1_all, Ga1x_id))
            # #
            C_d = kmeans.cluster_centers_
            C_d = np.column_stack((C_d, np.arange(1, C_d.shape[0] + 1)))
            C_d = C_d[C_d[:, 0].argsort()]
            print('C_d = ', C_d) 
            print('---------------------------------------------')

            print('C_d[-1, -1] = ', C_d[-1, -1])
            print('---------------------------------------------')
            if C_d[-1, 0] <= 0.5:
                Ga1_all_cate = []
            else:
                Ga1_all_cate = Ga1_all[Ga1_all[:, -1] == C_d[-1, -1], 0] 

            ide = []
            # for i in range(C_d.shape[0] - 1):
            #     if C_d[C_d.shape[0] - i - 2, 0] > 0.7 * C_d[-1, 0] and C_d[C_d.shape[0] - i - 2, 0] >= 0.5:
            #         Ga1_all_cate = np.concatenate((Ga1_all_cate, Ga1_all[Ga1_all[:, -1] == C_d[C_d.shape[0] - i - 2, -1], 0]))
            #     else:
            #          ide = np.concatenate((ide, Ga1_all[Ga1_all[:, -1] == C_d[C_d.shape[0] - i - 2, -1], 0]))

            Ga1_d_final = []
            c_d = 0
            Ga1_final1 = Ga1_final[0, :]
            Ga1_final1 = Ga1_final1.tolist()
            print(Ga1_final1)

            if  np.array(Ga1_all_cate).shape == 0:
                Ga1_d_final = []
            else:
                for i in Ga1_all_cate:
                    if i > 0.5:
                        print("The value of i is: ", i)
                        c_d += 1
                        if i in Ga1_final[0, :]:
                            index_Ga1 = Ga1_final1.index(i)
                            Ga1_d_final.append(Ga1_final[2, index_Ga1])

                if deleted_rows.shape[1] != 0:
                    for i in range(deleted_rows.shape[1]):
                        if deleted_rows[0, i] in Ga1_all_cate:
                            Ga1_d_final.append(deleted_rows[2, i])

            # print(ia_all)
            # print(ia_all[:, 1])
            print('ide configuration Atomic ids of all id types-------------------------------------------')
            # print(ide_d_final)
            print('Ga1_all_cate = ', Ga1_all_cate)
            print('-----------------------------------------------')
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------')
            Ga1_infimum_all = Ga1_d_final  
            print('Ga1 last recognition threshold', Ga1_infimum_all)
            print('All the contents of the Ga1 configuration-----------------------------------------------')
        else:
            Ga1_infimum_all = Ga1_all_id
        print(Ga1_infimum_all)

    #
    Ga2_all = []
    Ga2_pre = []
    Ga2_all_id = []
    count_Ga2 = 0

    for i in range(test_1_use.shape[0]):
        if int(test_1_use[i, 5]) == 9 and test_1_use[i, 7] == 4: 
            Ga2_all.append(test_1_use[i, 6] * 10)
            Ga2_pre.append(test_1_use[i, 8])
            Ga2_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_Ga2 += 1

    data_Ga2 = {'Similarity': Ga2_all,
               'differ': Ga2_pre,
               'id_ic': Ga2_all_id
    }

    input_data = pd.DataFrame(data_Ga2) 
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')] 
    Ga2_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')
    print('Ga2_all_without_du = ', Ga2_all_without_du)
    print('deleted_rows = ', deleted_rows)

    Ga2_all_without = Ga2_all_without_du.to_numpy()
    Ga2_all_without = Ga2_all_without.T
    print('Ga2_all_without = ', Ga2_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    Ga2_all = Ga2_all_without[0, :]
    if Ga2_all.shape[0] == 0:
        Ga2_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(Ga2_all) < 2:
        Ga2_infimum_all = []
    elif Ga2_all.shape[0] == 1:
        Ga2_infimum_all = Ga2_all_id
    elif Ga2_all.shape[0] == 2 and np.max(Ga2_all) > 2 and np.min(Ga2_all) < np.max(Ga2_all)*0.8:
        Ga2_pre = Ga2_all_without[1, :]
        Ga2_all_id = Ga2_all_without[2, :]

        Ga2_final = np.vstack((Ga2_all, Ga2_pre, Ga2_all_id))
        Ga2_infimum_all = []

        Ga2_final1 = Ga2_final[0, :]
        Ga2_final1 = Ga2_final1.tolist()
        index_Ga2 = Ga2_final1.index(np.max(Ga2_all))
        Ga2_infimum_all.append(Ga2_final[2, index_Ga2])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(Ga2_all):
                    Ga2_infimum_all.append(deleted_rows[2, i])
    else:
        Ga2_pre = Ga2_all_without[1, :]
        Ga2_all_id = Ga2_all_without[2, :]

        Ga2_all = np.vstack((Ga2_all, Ga2_pre))
        Ga2_final = np.vstack((Ga2_all, Ga2_all_id))
        print('Ga2_all = ', Ga2_all)

        # ia_all = np.sort(ia_all)

        Ga2_min_1 = np.min(Ga2_all[0, :])
        Ga2_min_2 = np.min(Ga2_all[1, :])
        # print('ia_min = ', ia_min)
        Ga2_max_1 = np.max(Ga2_all[0, :])
        Ga2_max_2 = np.max(Ga2_all[1, :])

        Ga2_min = np.vstack((Ga2_min_1, Ga2_min_2))
        Ga2_max = np.vstack((Ga2_max_1, Ga2_max_2))
        print('Ga2_min = ', Ga2_min)
        print('Ga2_max = ', Ga2_max)

        contains_positive = np.any(Ga2_all[1, :] > 0)
        contains_negative = np.any(Ga2_all[1, :] < 0)

        Ga2_all = np.array(Ga2_all)
        print(Ga2_all)

        if contains_positive or contains_negative:
            elbowIndex_Ga2, elbowGa2_k, elbowGa2_Ga2 = elbow(Ga2_all)

            sio.savemat('elbowie_k.mat', {'elbowie_k': elbowGa2_k})
            sio.savemat('elbowie_e.mat', {'elbowie_e': elbowGa2_Ga2})
            # elbowIndex_ia = 8
            print(elbowIndex_Ga2)
            #
            kmeans = KMeans(n_clusters=elbowIndex_Ga2)
            #     print(ia_all)
            Ga2_all = Ga2_all.T
            idx_Ga2 = kmeans.fit_predict(Ga2_all) + 1 
            #
            Ga2_all = np.column_stack((Ga2_all, idx_Ga2))
            # #
            C_Ga2 = kmeans.cluster_centers_
            C_Ga2 = np.column_stack((C_Ga2, np.arange(1, C_Ga2.shape[0] + 1)))
            C_Ga2 = C_Ga2[C_Ga2[:, 0].argsort()]
            print('C_Ga2 = ', C_Ga2) 
            print('---------------------------------------------')

            print('C_Ga2[-1, 1] = ', C_Ga2[-1, -1])
            print('---------------------------------------------')
            Ga2_all_cate = Ga2_all[Ga2_all[:, -1] == C_Ga2[-1, -1], 0]
            # ied = []
            # for i in range(C_Ga2.shape[0]):
            #     if C_Ga2[i, 0] > 5: 
            #         Ga2_all_cate = np.concatenate((Ga2_all_cate, Ga2_all[Ga2_all[:, -1] == C_Ga2[i, -1], 0]))  
            #     elif C_Ga2[i, 0] <= 5 and C_Ga2[i, 0] >= 1:
            #         ied = np.concatenate((Ga2_all_cate, Ga2_all[Ga2_all[:, -1] == C_Ga2[i, -1], 0]))

            id_Ga2_final = []
            ied_Ga2_final = []
            c_Ga2 = 0
            Ga2_final1 = Ga2_final[0, :]
            Ga2_final1 = Ga2_final1.tolist()
            print(Ga2_final1)

            for i in Ga2_all_cate:
                c_Ga2 += 1
                if i in Ga2_final[0, :]:
                    index_Ga2 = Ga2_final1.index(i)
                    id_Ga2_final.append(Ga2_final[2, index_Ga2])

            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in Ga2_all_cate:
                        id_Ga2_final.append(deleted_rows[2, i])

            # print(ia_all)
            # print(ia_all[:, 1])
            print('Ga2_all_cate = ', Ga2_all_cate)
            print('-----------------------------------------------')
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------')
            Ga2_infimum_all = id_Ga2_final
            print('Ga2 last recognition threshold: ', Ga2_infimum_all)
            print('All the contents of the Ga2 configuration-----------------------------------------------')
            # e_infimum_all = ie_all_id
            # print(e_infimum_all)
        else:
            Ga2_infimum_all = Ga2_all_id
            print(Ga2_infimum_all)

    # Ga2_all = np.concatenate((ied_Ga2_final, ide_Ga1_final))
    return Ga1_infimum_all, Ga2_infimum_all
    pass
