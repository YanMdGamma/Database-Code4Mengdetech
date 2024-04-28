from shutil import copy
import os
import numpy as np
import pandas as pd
# import xlsxwriter as xw
from openpyxl import Workbook

# # 能量存储
# energylist = []
# energylist = np.loadtxt('D:/Useful_Statas/30_e.txt', dtype="int")
# print(energylist)

# 更改.txt文件中指定位置的内容（改变随机数，改变速度，改变文件后缀）
def alter(file_name, old_str, new_str):
    file_data = ""
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(file_data)


# 创建文件夹
def folder_MakerandStatas_Change(energylist, numberlist, Vx_30, Vz_30, X_length1, X_length2, angel ,type):
    i = -1
    for energy in energylist:
        energy = str(energy) + "ev_20"
        count = 0
        i += 1
        for number in numberlist:
            count += 1
            if count <= 20:
                number = numberlist[i*20 + count-1]
                os.makedirs(f'C:/Users/14237/Experiment/{angel}/{energy}/{number}', exist_ok=True)
                # 设置固定文件存储
                original_path = f'D:/original_files/{type}'
                save_path = f'C:/Users/14237/Experiment/{angel}/{energy}/{number}'
                profiles = os.listdir(original_path)
                for profile in profiles:
                    #print(profile)
                    from_path = original_path + '\\' + profile
                    copy(from_path, save_path)
                alter(f"C:/Users/YanMZ/Experiments/{angel}/{energy}/{number}/in.lammps", "123456", str(number))# 改变随机数
                alter(f"C:/Users/YanMZ/Experiments/{angel}/{energy}/{number}/in.lammps", "32.1", str(Vx_30[i]))# 改变x方向上的速度
                alter(f"C:/Users/YanMZ/Experiments/{angel}/{energy}/{number}/in.lammps", "-234.82", str(Vz_30[i]))# 改变Z方向上的速度
                # 为避免原有的注入离子射出反应区
                alter(f"C:/Users/YanMZ/Experiments/{angel}/{energy}/{number}/in.lammps", "14.652", str(X_length1))# 改变注入X方向的距离
                alter(f"C:/Users/YanMZ/Experiments/{angel}/{energy}/{number}/in.lammps", "34.652", str(X_length2))# 同上
            else:
                break


# 将后10000步数据改为.txt结尾
# 以注入角度为30度时为例
# 随机数存储
numberlist_0 = []
def Change_numberlist_0(energylist):
    for energy in energylist:
        energy = str(energy) + "ev_20"
        ori_dir_0 = f'D:/Useful_Statas/20/{energy}/'
        number_list = os.listdir(ori_dir_0)
        for number0 in number_list:
            numberlist_0.append(number0)
        # numberlist_0.remove("lmp_serial.txt")
    print(numberlist_0)

    # # 用来判断随机数数组中的重复元素是否已经被删去
    # i = 0
    # for n in numberlist_0:
    #     i += 1
    # print(i)

def Statas_Processing():
    # 将文件ib中稳定的粒子位置通过txt文件格式进行存储  这个部分并没有被解决，目的是将路径存放在一个txt文件中，后采用一种方式对文件中的字符串信息进行调用
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/ib/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/ic/stable_temp/'
    # ori_dir = f'E:/stand_rdf/interstitals_426/analog_ib/data_b/stabel_temp/'
    # ori_dir = f'E:/stand_rdf/interstitals_426/analog_ic/data_c/stable_temp/'
    # ori_dir = f'E:/stand_rdf/interstitals_426/special/special/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/ia/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/rdf_2023_4&6/id_lost/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/rdf_2023_4&6/ie_lost/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/Ori/stable_temp/'
    # add = pd.read_table(r"E:/stand_rdf/add.txt",sep = ",",header=None)
    # print(add.head())
    # ori_dir = f'{add(2)}'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ia&ib/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ia&ic/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ib&ic/average_location/stable_temp/'
    # 测试 5个点10000左右的粒子数量
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ia&ib/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ia&ic/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/5_points/5_points/10000/3+ib&ic/average_location/stable_temp/'
    # 测试 150个缺陷100800的粒子数量
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/50~100_points/test_2/vague/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/50~100_points/test_3/ia+ib_48_2gap/ia+ib_48_2gap/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/ie/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new/specific_potential_soap/id/average_location/stable_temp/'
    # 大体系3类缺陷结构
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test1/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test2/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test3/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test4/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test6/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test7/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test8/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test9/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test10/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test13/average_location/stable_temp/'

    # 标准结构
    # ia——ic
    # ori_dir = f'D:/桌面/stand_rdf/split_interstitial/ia_ic/test_ie_mod/average_location/stable_temp/'
    # ia——id
    # ori_dir = f'D:/桌面/stand_rdf/split_interstitial/ia_id/average_location/stable_temp/'
    # ia——ib
    # ori_dir = f'D:/桌面/stand_rdf/split_interstitial/ia_ib/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/stand_rdf/new(!别忘了ie)/specific_potential_soap（别忘了ie）/ie_contain_others（ie！）/ie_con_others/'
    # ie——other_structure
    # ori_dir = f'D:/桌面/stand_rdf/new(!别忘了ie)/specific_potential_soap（别忘了ie）/ie/未改变位置的ie/改变位置的ie（被挤回来的原子）/average_location/stable_temp/'
    ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/500/average_location/stable_temp/'

    # 大体系
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test1/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test4/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_6_types/test1/average_location/stable_temp/'

    # 尝试根据自己的训练组设置不同的识别阈值
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_new_23.6.19/23.6.19_test1/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_new_23.6.19/23.6.19_test2/average_location/stable_temp/'
    # ori_dir = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_new_23.6.19/23.6.20_test3/average_location/stable_temp/'

    name_list = os.listdir(ori_dir)
    for name in name_list:
        # print(name)
        ori_name = name
        name = name.split('.')
        # 如果文件名存在后缀
        if name[-1] == 'dat': # and int(name[-2]) > 30000:
            name[-1] = 'txt'
            # 进行字符串的拼接
            name = str.join('.', name)
        # 文件名不存在后缀
        else:
            name.append('txt')
            name = str.join('.', name)
        # 如果源文件中已经有更改过的文件，则跳过后续步骤
        if name not in name_list:
            ori_name = ori_dir + ori_name
            name = ori_dir + name
            os.rename(ori_name, name)


# 创建数据处理文件夹
def Excel_Generator(file_name):
    # 读取数据文件中分组的数目
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            # 将数据按照空格分开
            file_data = line.split(' ')
            print(file_data)
    # 需要形成的文件数目 ib+ic+anaib+anaic+special
    number = len(file_data)
    print(number)
    # 循环次数
    loop = 0
    while loop < number:
        loop += 1
        # 获得存放excel文件的路径
        os.makedirs(f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/100/average_location', exist_ok=True)
        wb = Workbook()
        save_excelname = 'sheet1'
        wb.create_sheet(title=str(save_excelname), index=0)
        wb.save(
            filename=f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/100/average_location/{file_data[loop - 1]}.xlsx')  # 对类如len(periodic_data(next_index))进行操作报的错，原因是列表索引是使用中括号，而不是使用小括号


if __name__ == "__main__":
    # file_name = f'D:/桌面/stand_rdf/new/specific_potential_soap/average_location/name.txt'
    # file_name = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ia&ib/average_location/name.txt'
    # file_name = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/2_points/ia&ic/average_location/name.txt'
    # file_name = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_5_types/test1/average_location/name.txt'
    # file_name = f'D:/桌面/识别氧化镓中的缺陷结构/人为制造有限个点缺陷/10_points_3types/new_test1/average_location/name1.txt'
    file_name = f'D:/桌面/识别氧化镓中的缺陷结构/Step3_dynamic_identification/anneal_12.14/100/average_location/name2.txt'

    # 在指定文件夹下创建excel文件
    # Excel_Generator(file_name)
    # 将.dat文件转换为.txt文件
    Statas_Processing()


