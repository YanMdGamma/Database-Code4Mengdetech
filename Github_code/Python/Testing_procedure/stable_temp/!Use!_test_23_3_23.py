import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# # 首先获得粒子总数
# particles_ib_ic = 1279
# particles_interstitial = 1281

# 该部分将对应的氧原子提前进行了去除
particles_ib_ic = 511
particles_interstitial = 513

# 测试ia_ib_510个原子
particles_ia_ib = 510

# 提供所需要数据内容的位置信息
# address_all = ['E:/stand_rdf/ib/ib_lost2/stable', 'E:/stand_rdf/ic/ic_lost2/stable_temp',
#                'E:/stand_rdf/interstitals_426/analog_ib/data_b/stabel_temp',
#                'E:/stand_rdf/interstitals_426/analog_ic/data_c/stable_temp',
#                'E:/stand_rdf/interstitals_426/special/special/stable_temp']

# address_all = ['D:/桌面/stand_rdf/rdf_2023_4&6/ia_lost/stable_temp',
#                 'D:/桌面/stand_rdf/rdf_2023_4&6/id_lost/stable_temp',
#                 'D:/桌面/stand_rdf/rdf_2023_4&6/ie_lost/stable_temp',
#                 'D:/桌面/stand_rdf/rdf_2023_4&6/ORI/stable_temp']
# address_all = ['D:/桌面/stand_rdf/rdf_2023_4&6/ORI/stable_temp']

# 选择低温的内容进行平均化操作

# address_all = ['D:/桌面/stand_rdf/new/specific_potential_soap/ia/stable_temp',
#                'D:/桌面/stand_rdf/new/specific_potential_soap/ib/stable_temp',
#                'D:/桌面/stand_rdf/new/specific_potential_soap/ic/stable_temp',
#                'D:/桌面/stand_rdf/new/specific_potential_soap/Ori/stable_temp']


# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ia&ib/average_location/stable_temp']
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ib&ic/average_location/stable_temp']

# 10000个数据点，5个缺陷结构 particle_number = 4091
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ia&ib/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ia&ic/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ib&ic/average_location/stable_temp']
# 100800个数据点，150个缺陷结构 39360粒子数

# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/50~100_points/test_2/vague/average_location/stable_temp']
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/50~100_points/test_3/ia+ib_48_2gap/ia+ib_48_2gap/average_location/stable_temp']

# address_all = ['D:/桌面/stand_rdf/new/specific_potential_soap/id/average_location/stable_temp',
#                'D:/桌面/stand_rdf/new/specific_potential_soap/ie/average_location/stable_temp']

# test1 3类不同的缺陷结构
# particle_number_larger = 10230
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test2/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test3/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test4/average_location/stable_temp',]
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test6/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test7/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test8/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test9/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test10/average_location/stable_temp']
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test5/average_location/stable_temp']

# test1 3类不同的缺陷结构 20个缺陷
# particle_number_larger = 10220
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test13/average_location/stable_temp']

# test1 3类不同的缺陷结构
# particle_number_larger = 10238
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test4/average_location/stable_temp']
# # address_all = ['D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test1/average_location/stable_temp']

# 尝试采用每一个实验组的数据进行自行的识别阈值获取
particle_number_larger = 6001
address_all = ['D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/500/average_location/stable_temp',]
# address_all = ['D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/1/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/2/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/3/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/4/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/5/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/6/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/7/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/8/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/9/average_location/stable_temp',
#                'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.9.5/Only_v/4000_2.5.5/15O/10/average_location/stable_temp']
# 统计循环数量

# 循环写入txt中的数据内容
def Changetxt2Excel(address_all, file_name):
    # 读取数据文件中分组的数目
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            # 将数据按照空格分开
            file_data = line.split(' ')
            print(file_data)
    # 对路径中所有的类别都进行该操作
    address_loop = -1
    for add in address_all:
        address_loop += 1
        # 定义路径的存储
        address = []
        ori_dir = f'{address_all[address_loop]}'
        name_list = os.listdir(ori_dir)
        print(name_list)
        for name in name_list:
            address.append(f'{address_all[address_loop]}/{name}')
        print(address)
        # 循环次数设置
        loop = len(name_list)
        print(loop)
        number = 0

        # 设置粒子数目的多少
        if address_loop <= 100:# ib & ic 1279个粒子 anaib & anaic & special 1281个粒子
            particle_loop = particle_number_larger
            # particle_loop = particles_ib_ic
        # elif address_loop <= 2:
        #     particle_loop = particles_interstitial
        # else:
        #     particle_loop = particles_interstitial-1
        else:
            particle_loop = particles_interstitial
        while number < loop - 1:
            number += 1
            print(number)
            # 加载该路径下的txt文件，并只取后面的N原子数据
            if number == 1:
                # 更新循环信息
                number_4_id = 0
                # 跳过前9条信息
                data = np.loadtxt(address[number - 1], skiprows=9)
                # print(address[number - 1])
                data1 = np.loadtxt(address[number], skiprows=9)
                # print(address[number])
                # 为相应数据增加对应的标题，提供pandas可处理的文件类型
                df = pd.DataFrame(data, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
                df1 = pd.DataFrame(data1, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
            else:
                # print(address)
                # 更新循环信息
                number_4_id = 0
                data2 = np.loadtxt(address[number], skiprows=9)
                # print(address[number])
                df1 = pd.DataFrame(data2, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
                # print(df1)
                # 将id值相同的数据进行相加
                # 用于测试
                # number_4_id = 1
            #             print(df.loc[df.id == 1, 'addr_x'])
            #             df.loc[df.id == 1, 'addr_x'] = df.loc[df.id == 1, 'addr_x'] + df1.loc[df.id == 1, 'addr_x']
            #             print(df.loc[df.id == 1, 'addr_x'])
            #             print(df1.loc[df.id == 1, 'addr_x'])
            #             print(df)
            #             print(df1)
            # 计算所有文件中粒子位置的平均值
            while number_4_id < particle_loop:
                number_4_id += 1
                # 这个部分是取值再进行赋值的操作，如果
                df.loc[df.id == number_4_id, 'addr_x'] = df1.addr_x.values[df1.id == number_4_id] + df.addr_x.values[
                    df.id == number_4_id]
                # if number_4_id == 963:
                #     print(df.loc[df.id == number_4_id, 'addr_x'])
                #     print(df1.loc[df1.id == number_4_id, 'addr_x'])
                #     print(df1.addr_x.values[df1.id == number_4_id])
                df.loc[df.id == number_4_id, 'addr_y'] = df1.addr_y.values[df1.id == number_4_id] + df.addr_y.values[
                    df.id == number_4_id]
                df.loc[df.id == number_4_id, 'addr_z'] = df1.addr_z.values[df1.id == number_4_id] + df.addr_z.values[
                    df.id == number_4_id]

        # 将最后的文件内容进行平均化
        number_4_id = 0
        while number_4_id <= particle_loop:
            number_4_id += 1
            df.loc[df.id == number_4_id, 'addr_x'] = df.loc[df.id == number_4_id, 'addr_x'] / loop
            df.loc[df.id == number_4_id, 'addr_y'] = df.loc[df.id == number_4_id, 'addr_y'] / loop
            df.loc[df.id == number_4_id, 'addr_z'] = df.loc[df.id == number_4_id, 'addr_z'] / loop

        # 该部分由于一开始设置路径没有设置好，以至于没有办法进行代码的简化，如果使用数字进行xlsx的定义则可以实现循环操作，后续可以更改（已经改好了）

        # df.to_excel(f'D:/桌面/stand_rdf/rdf_2023_4&6/average_location/{file_data[address_loop]}.xlsx', index=False)
        # df.to_excel(f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test1/average_location/{file_data[address_loop]}.xlsx', index=False)
        # df.to_excel(f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test1/average_location/.xlsx',
        #             index=False)
        df.to_excel(f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/100/average_location/{file_data[address_loop]}.xlsx',
                    index=False)

if __name__ == "__main__":
    # file_name = f'D:/桌面/stand_rdf/rdf_2023_4&6/average_location/name.txt'
    # file_name = f'D:/桌面/stand_rdf/new/specific_potential_soap/average_location/name.txt'
    # test_ia_ib
    file_name = f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/100/average_location/name_500.txt/'
    Changetxt2Excel(address_all, file_name)
