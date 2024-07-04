import numpy
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
import scipy.io as sio

# 肘部图的绘制和选择
def elbow(inputArg1):
    # 设置聚类数量的范围
    inputArg1 = inputArg1.T
    print(inputArg1.shape)
    input_data = pd.DataFrame(inputArg1)
    inputArg1 = input_data.drop_duplicates()  # 对原始数据中的重复数据进行清洗
    k_values = np.arange(1, inputArg1.shape[0] + 1)
    print(k_values)
    # 初始化聚类误差存储向量
    errors = np.zeros(len(k_values))
    print(errors)

    # 计算每个聚类数量下的聚类误差
    # warnings.filterwarnings("ignore", category= ConvergenceWarning)
    for i, k in enumerate(k_values):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(inputArg1)
        errors[i] = np.sum(np.min(kmeans.transform(inputArg1), axis=1))

    # 绘制肘部图
    plt.figure()
    # plt.rcParams['font.family'] = 'SimHei'
    mpl.rcParams["font.sans-serif"] = ["SimHei"]
    # 设置正常显示符号
    mpl.rcParams["axes.unicode_minus"] = False
    plt.plot(k_values, errors, 'o-')
    plt.title('Elbow Method')
    plt.xlabel('Cluster number')
    plt.ylabel('error')

    # 寻找肘部位置
    diff_errors = np.diff(errors)
    elbowIndex = -1  # Default value
    if diff_errors.size > 0:
        elbowIndex = np.where(np.abs(diff_errors) <= np.abs(np.mean(diff_errors)))[0][0]
    plt.plot(k_values[elbowIndex], errors[elbowIndex], 'ro', markersize=10, linewidth=2)
    plt.show()

    return elbowIndex + 1, k_values, errors

def threshold_point_defects(test_1_use):
    ia_all = []
    ia_pre = []
    ia_all_id = []
    ia_all_differ = [] # 在静态的实验里面没有引入这个变量
    count_ia = 0

    for i in range(test_1_use.shape[0]):
        col_judge = test_1_use.shape[1]
        if int(test_1_use[i, 5]) == 1 and test_1_use[i, 6] > 0.5 and int(test_1_use[i, 7]) == 4 and test_1_use[i, 9] == 0:  # 增加了配位数的判断
            ia_all.append(test_1_use[i, 6])
            ia_pre.append(test_1_use[i, 8])
            ia_all_id.append(test_1_use[i, 0])
            if col_judge < 11:
                ia_all_differ.append(test_1_use[i, 6])
            else:
                ia_all_differ.append(test_1_use[i, 10])

            if int(test_1_use[i, 6]) == 1:
                count_ia += 1

    data_ia = {'Similarity': ia_all,
               'differ': ia_pre,
               'id_ic': ia_all_id,
               'differ_max': ia_all_differ
    }

    input_data = pd.DataFrame(data_ia)  # 对重复数据进行的操作
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 得到重复数据的行
    ia_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  得到删除重复数据的内容
    print('ia_all_without_du = ', ia_all_without_du)
    print('deleted_rows = ', deleted_rows)

    ia_all_without = ia_all_without_du.to_numpy()
    ia_all_without = ia_all_without.T
    print('ia_all_without = ', ia_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    ia_all = ia_all_without[0, :]

    if ia_all.shape[0] == 0:
        a_infimum_all = []
    # elif np.max(ia_all) < 0.5 : # 0.5
    #     a_infimum_all = []
    elif ia_all.shape[0] == 1:
        a_infimum_all = ia_all_id
    elif ia_all.shape[0] == 2:
        ia_pre = ia_all_without[1, :]
        ia_all_id = ia_all_without[2, :]

        # ia_final = np.vstack((ia_all, ia_pre, ia_all_id, ia_all_differ))
        ia_final = np.vstack((ia_all, ia_pre, ia_all_id))
        a_infimum_all = []

        ia_final1 = ia_final[0, :]
        ia_final1 = ia_final1.tolist()
        index_a = ia_final1.index(np.max(ia_all))
        a_infimum_all.append(ia_final[2, index_a])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(ia_all):
                    a_infimum_all.append(deleted_rows[2, i])

    else:
        ia_pre = ia_all_without[1, :]
        ia_all_id = ia_all_without[2, :]
        ia_all_differ = ia_all_without[3, :]
        # 这个differ后面动态测试的时候有用
        # 24.1.4 求解均值
        # 这个differ后面动态测试的时候有用
        ia_all = np.vstack((ia_all, ia_pre, ia_all_differ))
        ia_final = np.vstack((ia_all, ia_all_id))
        print('ia_all = ', ia_all)

        # ia_all = np.sort(ia_all)

        ia_min_1 = np.min(ia_all[0, :])
        ia_min_2 = np.min(ia_all[1, :])
        # print('ia_min = ', ia_min)
        ia_max_1 = np.max(ia_all[0, :])
        ia_max_2 = np.max(ia_all[1, :])

        ia_min = np.vstack((ia_min_1, ia_min_2))
        ia_max = np.vstack((ia_max_1, ia_max_2))
        print('ia_min = ', ia_min)
        print('ia_max = ', ia_max)

        # 判断是否既有大于零的数也有小于零的数
        contains_positive = np.any(ia_all[1, :] > 0)
        contains_negative = np.any(ia_all[1, :] < 0)

        ia_all = np.array(ia_all)
        print(ia_all)

        if contains_positive or contains_negative:
            elbowIndex_ia, elbowia_k, elbowia_e = elbow(ia_all)

            sio.savemat('elbowia_k.mat', {'elbowia_k': elbowia_k})
            sio.savemat('elbowia_e.mat', {'elbowia_e': elbowia_e})

            # elbowIndex_ia = 8
            print("elbowIndex_ia", elbowIndex_ia)
            if elbowIndex_ia == 0: # 仅仅识别出一个ia构型
                elbowIndex_ia = 1
            #
            kmeans = KMeans(n_clusters=elbowIndex_ia)
            #     print(ia_all)
            ia_all = ia_all.T
            idx_ia = kmeans.fit_predict(ia_all) + 1  # ia_all 23.9.2 这个组别自己定义会从0组开始
            #
            ia_all = np.column_stack((ia_all, idx_ia))
            # #
            C_a = kmeans.cluster_centers_
            C_a = np.column_stack((C_a, np.arange(1, C_a.shape[0] + 1)))
            C_a = C_a[C_a[:, 0].argsort()]
            print("C_a", C_a)
            count = 0
            # # 如果最值之间的平均值要大于0.45，那么便舍去该组，更新C_a
            # for i in range(C_a.shape[0]):
            #     print(C_a.shape[1])
            #     if C_a.shape[1] > 2:
            #         if abs(C_a[i, 2]) > 0.045: # 0.0045
            #             C_a = np.delete(C_a, i, axis=0)
            #     else:
            #         C_a = C_a

            a_all_cate = []
            a_all_cate = np.concatenate((a_all_cate, ia_all[ia_all[:, -1] == C_a[-1, -1], 0]))

            # 将对应的differ平均值进行计算
            print('24.1.5: a_all_cate:', a_all_cate)

            for i in range(C_a.shape[0] - 1):
                if C_a[C_a.shape[0] - i - 2, 0] > 0.91 * C_a[-1, 0]:
                    a_all_cate = np.concatenate((a_all_cate, ia_all[ia_all[:, -1] == C_a[C_a.shape[0] - i - 2, -1], 0]))

            print('C_a = ', C_a)  # 这个最后一类好像就行
            print('---------------------------------------------')

            print('C_a[-1, 1] = ', C_a[0, -1])
            print('---------------------------------------------')
              # 最后一行的类别

            id_a_final = []
            c_a = 0
            ia_final1 = ia_final[0, :]
            ia_final1 = ia_final1.tolist()
            print(ia_final1)

            for i in a_all_cate:
                c_a += 1
                if i in ia_final[0, :]:
                    index_a = ia_final1.index(i)
                    id_a_final.append(ia_final[3, index_a])
                    print('24.1.5:id_a_final:', ia_final[3, index_a])

            # 判断是否会在重复值当中存在和a_all_cate相同的内容
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows.shape[1]):
                    if deleted_rows[0, i] in a_all_cate:
                        id_a_final.append(deleted_rows[2, i])
                        print('24.1.5:deleted_rows[2, i]:', deleted_rows[2, i])
            # print(ia_all)
            # print(ia_all[:, 1])
            print('a_all_cate = ', a_all_cate)
            print('-----------------------------------------------')
            # print('np.min(a_all_cate)', np.min(a_all_cate))
            print('-----------------------------------------')
            a_infimum_all = id_a_final  # 根据识别阈值来进行判断
            print('ia last recognition threshold: ', a_infimum_all)
            print('All the contents of the ia configuration-----------------------------------------------')
        else:
            a_infimum_all = ia_all_id
            print(a_infimum_all)
    #
    ib_all = []
    ib_pre = []
    ib_all_id = []
    count_ib = 0

    for i in range(test_1_use.shape[0]):
        if int(test_1_use[i, 5]) == 2 and int(test_1_use[i, 7]) == 6 and test_1_use[i, 9] == 0:  # 增加了配位数的判断
            ib_all.append(test_1_use[i, 6])
            ib_pre.append(test_1_use[i, 8])
            ib_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_ib += 1

    data_ib = {'Similarity': ib_all,
               'differ': ib_pre,
               'id_ic': ib_all_id
    }

    input_data = pd.DataFrame(data_ib)  # 对重复数据进行的操作
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 得到重复数据的行
    ib_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  得到删除重复数据的内容
    print('ib_all_without_du = ', ib_all_without_du)
    print('deleted_rows = ', deleted_rows)

    ib_all_without = ib_all_without_du.to_numpy()
    ib_all_without = ib_all_without.T
    print('ib_all_without = ', ib_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    ib_all = ib_all_without[0, :]

    # 还要增加的内容是，对于识别结果仅有两个粒子的情况，要去除识别效果差的，两个粒子的情况无法采用聚类区分，会有很大误差
    if ib_all.shape[0] == 0:
        b_infimum_all = []
        # print(ib_all.shape[0])
    elif np.max(ib_all) < 0.5:
        b_infimum_all = []
    elif ib_all.shape[0] == 1:
        b_infimum_all = ib_all_id
    elif ib_all.shape[0] == 2 and np.max(ib_all) > 0.5 and np.min(ib_all) < np.max(ib_all)*0.8: #  如果最小值比最大值的0.5还小就认为不是所需要的构型
        ib_pre = ib_all_without[1, :]
        ib_all_id = ib_all_without[2, :]

        ib_final = np.vstack((ib_all, ib_pre, ib_all_id))
        b_infimum_all = []

        ib_final1 = ib_final[0, :]
        ib_final1 = ib_final1.tolist()
        index_b = ib_final1.index(np.max(ib_all))
        b_infimum_all.append(ib_final[2, index_b])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(ib_all):
                    b_infimum_all.append(deleted_rows[2, i])
    else:
        #  如果存在相同的内容就需要将后面的值先进行存储
        ib_pre = ib_all_without[1, :]
        ib_all_id = ib_all_without[2, :]

        ib_all = np.vstack((ib_all, ib_pre))
        ib_final = np.vstack((ib_all, ib_all_id))
        print('ib_final = ', ib_all)

        # ia_all = np.sort(ia_all)

        ib_min_1 = np.min(ib_all[0, :])
        ib_min_2 = np.min(ib_all[1, :])
        # print('ia_min = ', ia_min)
        ib_max_1 = np.max(ib_all[0, :])
        ib_max_2 = np.max(ib_all[1, :])

        ib_min = np.vstack((ib_min_1, ib_min_2))
        ib_max = np.vstack((ib_max_1, ib_max_2))
        print('ib_min = ', ib_min)
        print('ib_max = ', ib_max)
        # 判断是否既有大于零的数也有小于零的数
        contains_positive = np.any(ib_all[1, :] > 0)
        contains_negative = np.any(ib_all[1, :] < 0)

        ib_all = np.array(ib_all)

        if contains_positive or contains_negative:
            elbowIndex_ib, elbowib_k, elbowib_e = elbow(ib_all)

            sio.savemat('elbowib_k.mat', {'elbowib_k': elbowib_k})
            sio.savemat('elbowib_e.mat', {'elbowib_e': elbowib_e})
            # elbowIndex_ia = 8
            print(elbowIndex_ib)
            #
            kmeans = KMeans(n_clusters=elbowIndex_ib)
            #     print(ia_all)
            ib_all = ib_all.T
            idx_ib = kmeans.fit_predict(ib_all) + 1 # ia_all 23.9.2 这个组别自己定义会从0组开始
            #
            ib_all = np.column_stack((ib_all, idx_ib))
            # #
            C_b = kmeans.cluster_centers_
            C_b = np.column_stack((C_b, np.arange(1, C_b.shape[0] + 1)))
            C_b = C_b[C_b[:, 0].argsort()]

            print('C_b = ', C_b)  # 这个最后一类好像就行
            print('---------------------------------------------')

            print('C_b[-1, 1] = ', C_b[-1, -1])
            print('---------------------------------------------')
            b_all_cate = ib_all[ib_all[:, -1] == C_b[-1, -1], 0]  # 最后一行的类别
            for i in range(C_b.shape[0] - 1):
                if C_b[C_b.shape[0] - i - 2, 0] > 0.5:
                    b_all_cate = np.concatenate((b_all_cate, ib_all[ib_all[:, -1] == C_b[C_b.shape[0] - i - 2, -1], 0]))
            id_b_final = []
            c_b = 0
            ib_final1 = ib_final[0, :]
            ib_final1 = ib_final1.tolist()
            print(ib_final1)

            for i in b_all_cate:
                c_b += 1
                if i in ib_final[0, :]:
                    index_b = ib_final1.index(i)
                    id_b_final.append(ib_final[2, index_b])

            # 判断是否会在重复值当中存在和b_all_cate相同的内容
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows):
                    if deleted_rows[0, i] in b_all_cate:
                        id_b_final.append(deleted_rows[2, i])
            print('b_all_cate = ', b_all_cate)
            print('-----------------------------------------------')
            # print('np.min(b_all_cate)', np.min(b_all_cate))
            print('-----------------------------------------')
            b_infimum_all = id_b_final  # 根据识别阈值来进行判断
            print('ib last recognition threshold: ', b_infimum_all)
            print('All the contents of the ib configuration-----------------------------------------------')
        else:
            b_infimum_all = ib_all_id
            print(b_infimum_all)

    ic_all = []
    ic_pre = []
    ic_all_id = []
    count_ic = 0

    for i in range(test_1_use.shape[0]):
        if int(test_1_use[i, 5]) == 3 and int(test_1_use[i, 7]) == 6: #  and test_1_use[i, 9] == 0增加了配位数的判断
            ic_all.append(test_1_use[i, 6])
            ic_pre.append(test_1_use[i, 8])
            ic_all_id.append(test_1_use[i, 0])

            if int(test_1_use[i, 6]) == 1:
                count_ic += 1

    data_ic = {'Similarity': ic_all,
               'differ': ic_pre,
               'id_ic': ic_all_id
    }

    input_data = pd.DataFrame(data_ic)  # 对重复数据进行的操作
    print('input_data = ')
    print(input_data)
    deleted_rows = input_data[input_data.duplicated(subset=['Similarity', 'differ'], keep='first')]  # 得到重复数据的行
    ic_all_without_du = input_data.drop_duplicates(subset=['Similarity', 'differ'], keep='first')  #  得到删除重复数据的内容
    print('ic_all_without_du = ', ic_all_without_du)
    print('deleted_rows = ', deleted_rows)

    ic_all_without = ic_all_without_du.to_numpy()
    ic_all_without = ic_all_without.T
    print('ic_all_without = ', ic_all_without)
    deleted_rows = deleted_rows.to_numpy()
    deleted_rows = deleted_rows.T
    print('deleted_rows_numpy = ', deleted_rows)

    ic_all = ic_all_without[0, :]

    if ic_all.shape[0] == 0: #  如果测试集中没有对应的缺陷构型
        c_infimum_all = []
    elif np.max(ic_all) < 0.5:
        c_infimum_all = []
    elif ic_all.shape[0] == 1:
        c_infimum_all = ic_all_id
    elif ic_all.shape[0] == 2 and np.max(ic_all) > 0.5 and np.min(ic_all) < np.max(
        ic_all) * 0.7:  # 如果最小值比最大值的0.5还小就认为不是所需要的构型
        ic_pre = ic_all_without[1, :]
        ic_all_id = ic_all_without[2, :]

        ic_final = np.vstack((ic_all, ic_pre, ic_all_id))
        c_infimum_all = []

        ic_final1 = ic_final[0, :]
        ic_final1 = ic_final1.tolist()
        index_c = ic_final1.index(np.max(ic_all))
        c_infimum_all.append(ic_final[2, index_c])
        print('deleted_rows = ', deleted_rows.shape[1])
        if deleted_rows.shape[1] != 0:
            for i in range(deleted_rows.shape[1]):
                if deleted_rows[0, i] == np.max(ic_all):
                    c_infimum_all.append(deleted_rows[2, i])

    else:
        #  如果存在相同的内容就需要将后面的值先进行存储
        ic_pre = ic_all_without[1, :]
        ic_all_id = ic_all_without[2, :]

        ic_all = np.vstack((ic_all, ic_pre))
        ic_final = np.vstack((ic_all, ic_all_id))
        print('ic_final = ', ic_final)
        print('ic_all = ', ic_all)
        # ia_all = np.sort(ia_all)

        ic_min_1 = np.min(ic_all[0, :])
        ic_min_2 = np.min(ic_all[1, :])
        # print('ia_min = ', ia_min)
        ic_max_1 = np.max(ic_all[0, :])
        ic_max_2 = np.max(ic_all[1, :])

        ic_min = np.vstack((ic_min_1, ic_min_2))
        ic_max = np.vstack((ic_max_1, ic_max_2))
        print('ic_min = ', ic_min)
        print('ic_max = ', ic_max)

        # 判断是否既有大于零的数也有小于零的数
        contains_positive = np.any(ic_all[1, :] > 0)
        contains_negative = np.any(ic_all[1, :] < 0)

        ic_all = np.array(ic_all)
        print(ic_all)

        if contains_positive or contains_negative:
            elbowIndex_ic, elbowic_k, elbowic_e = elbow(ic_all)

            sio.savemat('elbowic_k.mat', {'elbowic_k': elbowic_k})
            sio.savemat('elbowic_e.mat', {'elbowic_e': elbowic_e})
            # elbowIndex_ia = 8
            print(elbowIndex_ic)

            kmeans = KMeans(n_clusters=elbowIndex_ic)
            #     print(ia_all)
            ic_all = ic_all.T
            idx_ic = kmeans.fit_predict(ic_all) + 1  # ia_all 23.9.2 这个组别自己定义会从0组开始
            #
            ic_all = np.column_stack((ic_all, idx_ic))
            # #
            C_c = kmeans.cluster_centers_
            C_c = np.column_stack((C_c, np.arange(1, C_c.shape[0] + 1)))
            C_c = C_c[C_c[:, 0].argsort()]
            print('C_c = ', C_c)  # 这个最后一类好像就行
            print('---------------------------------------------')

            print('C_c[-1, 1] = ', C_c[-1, -1])
            print('---------------------------------------------')
            c_all_cate = ic_all[ic_all[:, -1] == C_c[-1, -1], 0]  # 最后一行的类别

            for i in range(C_c.shape[0] - 1):
                if C_c[C_c.shape[0] - i - 2, 0] > 0.5:
                    c_all_cate = np.concatenate((c_all_cate, ic_all[ic_all[:, -1] == C_c[C_c.shape[0] - i - 2, -1], 0]))

            id_c_final = []
            c_c = 0
            ic_final1 = ic_final[0, :]
            ic_final1 = ic_final1.tolist()
            print(ic_final1)

            for i in c_all_cate: #  有可能存在两个值一模一样的问题
                c_c += 1
                if i in ic_final[0, :]:
                    index_c = ic_final1.index(i)
                    id_c_final.append(ic_final[2, index_c])

            # 判断是否会在重复值当中存在和c_all_cate相同的内容
            if deleted_rows.shape[1] != 0:
                for i in range(deleted_rows):
                    if deleted_rows[0, i] in c_all_cate:
                        id_c_final.append(deleted_rows[2, i])

            print('c_all_cate = ', c_all_cate)
            print('-----------------------------------------------')
            print('np.min(c_all_cate)', np.min(c_all_cate))
            print('-----------------------------------------')
            c_infimum_all = id_c_final  # 根据识别阈值来进行判断
            print('ic last recognition threshold: ', c_infimum_all)
            print('All the contents of the ic configuration-----------------------------------------------')
        else:
            c_infimum_all = ic_all_id
            print(c_infimum_all)
    #
    return a_infimum_all, b_infimum_all, c_infimum_all

