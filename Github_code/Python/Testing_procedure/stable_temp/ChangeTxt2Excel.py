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

# 提供所需要数据内容的位置信息
# address_all = ['E:/stand_rdf/ib/ib_lost2/stable', 'E:/stand_rdf/ic/ic_lost2/stable_temp',
#                'E:/stand_rdf/interstitals_426/analog_ib/data_b/stabel_temp',
#                'E:/stand_rdf/interstitals_426/analog_ic/data_c/stable_temp',
#                'E:/stand_rdf/interstitals_426/special/special/stable_temp']

# address_all = ['D:/桌面/stand_rdf/rdf_2023_4&6/ia_lost/stable_temp',
#                 'D:/桌面/stand_rdf/rdf_2023_4&6/id_lost/stable_temp',
#                 'D:/桌面/stand_rdf/rdf_2023_4&6/ie_lost/stable_temp',
address_all = ['D:/桌面/stand_rdf/rdf_2023_4&6/ORI/stable_temp']
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
        # if address_loop <= 0:# ib & ic 1279个粒子 anaib & anaic & special 1281个粒子
        #     particle_loop = particles_ib_ic
        # elif address_loop <= 2:
        #     particle_loop = particles_interstitial
        # else:
        particle_loop = particles_interstitial-1
        while number < loop - 1:
            number += 1
            print(number)
            # 加载该路径下的txt文件，并只取后面的N原子数据
            if number == 1:
                # 更新循环信息
                number_4_id = 0
                # 跳过前9条信息
                data = np.loadtxt(address[number - 1], skiprows=9)
                print(address[number - 1])
                data1 = np.loadtxt(address[number], skiprows=9)
                print(address[number])
                # 为相应数据增加对应的标题，提供pandas可处理的文件类型
                df = pd.DataFrame(data, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
                df1 = pd.DataFrame(data1, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
            else:
                # print(address)
                # 更新循环信息
                number_4_id = 0
                data1 = np.loadtxt(address[number], skiprows=9)
                print(address[number])
                df1 = pd.DataFrame(data1, columns=['id', 'type', 'addr_x', 'addr_y', 'addr_z'])
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
                df.loc[df.id == number_4_id, 'addr_x'] = df.loc[df.id == number_4_id, 'addr_x'] + df1.loc[
                    df.id == number_4_id, 'addr_x']
                df.loc[df.id == number_4_id, 'addr_y'] = df.loc[df.id == number_4_id, 'addr_y'] + df1.loc[
                    df.id == number_4_id, 'addr_y']
                df.loc[df.id == number_4_id, 'addr_z'] = df.loc[df.id == number_4_id, 'addr_z'] + df1.loc[
                    df.id == number_4_id, 'addr_z']

        # 将最后的文件内容进行平均化
        number_4_id = 0
        while number_4_id <= particle_loop:
            number_4_id += 1
            df.loc[df.id == number_4_id, 'addr_x'] = df.loc[df.id == number_4_id, 'addr_x'] / loop
            df.loc[df.id == number_4_id, 'addr_y'] = df.loc[df.id == number_4_id, 'addr_y'] / loop
            df.loc[df.id == number_4_id, 'addr_z'] = df.loc[df.id == number_4_id, 'addr_z'] / loop

        # 该部分由于一开始设置路径没有设置好，以至于没有办法进行代码的简化，如果使用数字进行xlsx的定义则可以实现循环操作，后续可以更改（已经改好了）

        df.to_excel(f'D:/桌面/stand_rdf/rdf_2023_4&6/average_location/{file_data[address_loop]}.xlsx', index=False)


if __name__ == "__main__":
    # file_name = f'D:/桌面/stand_rdf/rdf_2023_4&6/average_location/name.txt'
    # 选择低温条件下未发生位移的原子进行标准rdf统计
    file_name = f'D:/桌面/识别氧化镓中的缺陷结构/Step2_detect_defects/23.8.28_mul_tests/1/average_location/name.txt'
    Changetxt2Excel(address_all, file_name)
