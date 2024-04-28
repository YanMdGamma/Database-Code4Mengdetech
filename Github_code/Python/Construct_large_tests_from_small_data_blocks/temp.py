import os
import random
import numpy as np
import time
import shutil
import Change_txt2dat


# 这个函数用来返回dat文件中第一个要更改的 80 atoms 数据，中的数字大小
def get_number_from_line(file_path, lin_num, number_po):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[lin_num]
                numbers_int = []
                numbers_float = []
                # 将不同的数据类型存储到不同的数组中
                for num in second_line.split(' '):
                    if num.isdigit():
                        numbers_int.append(int(num))
                        # print(numbers_int) # 用来是否运行正常
                    else:
                        try:
                            float(num)
                            numbers_float.append(float(num))
                            # print(numbers_float) # 用来看是否运行正常
                        except ValueError:
                            continue
                # 返回我需要的内容，即盒子的长宽高
                if len(numbers_int) > 0 and len(numbers_float) == 0:  # python 中表示并且关系用and *& 不好用*
                    print(numbers_int)
                    return numbers_int[number_po]
                elif len(numbers_float) > 0 and len(numbers_int) == 0:
                    print(numbers_float)
                    return numbers_float[number_po]
                elif len(numbers_float) > 0 and len(numbers_int) > 0:
                    int_float = numbers_int + numbers_float
                    print(int_float)
                    return int_float[number_po]
                else:
                    return print("不存在整型与浮点型数据。")
    except IOError:
        print("无法打开文件或读取数据出错。")
    return None


# 更改.txt文件中指定位置的内容（改变随机数，改变速度，改变文件后缀）
def replace_number_in_line(file_path, new_number, lin_num, number_po):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[lin_num]
                numbers_int = []
                numbers_float = []
                # 将不同的数据类型存储到不同的数组中
                for num in second_line.split(' '):
                    if num.isdigit():
                        numbers_int.append(int(num))
                        # print(numbers_int) # 用来是否运行正常
                    else:
                        try:
                            float(num)
                            numbers_float.append(float(num))
                            # print(numbers_float) # 用来看是否运行正常
                        except ValueError:
                            continue

                if len(numbers_int) > 0 and len(numbers_float) == 0:  # python 中表示并且关系用and *& 不好用*
                    # print(numbers_int)
                    numbers = numbers_int
                elif len(numbers_float) > 0 and len(numbers_int) == 0:
                    # print(numbers_float)
                    numbers = numbers_float
                elif len(numbers_float) > 0 and len(numbers_int) > 0:
                    int_float = numbers_int + numbers_float
                    # print(int_float)
                    numbers = int_float
                else:
                    print("不存在整型与浮点型数据。")

                if len(numbers) > 0:
                    updated_line = second_line.replace(str(numbers[number_po]), str(new_number), 1)
                    lines[lin_num] = updated_line
                    with open(file_path, 'w') as updated_file:
                        updated_file.writelines(lines)
                    print("原始数据集中，数字已成功替换。")
                    return
    except IOError:
        print("无法打开文件或读取数据出错。")
    print("无法替换第二行的第一个数字。")

# 更改.txt文件中指定位置的内容（改变随机数，改变速度，改变文件后缀）
def replace_number_in_line4lines(line, new_number, number_po):
    try:
        if len(line) >= 2:
            second_line = line
            numbers_int = []
            numbers_float = []
            # 将不同的数据类型存储到不同的数组中
            for num in second_line.split(' '):
                if num.isdigit():
                    numbers_int.append(int(num))
                    # print(numbers_int) # 用来是否运行正常
                else:
                    try:
                        float(num)
                        numbers_float.append(float(num))
                        # print(numbers_float) # 用来看是否运行正常
                    except ValueError:
                        continue

            if len(numbers_int) > 0 and len(numbers_float) == 0:  # python 中表示并且关系用and *& 不好用*
                # print(numbers_int)
                numbers = numbers_int
            elif len(numbers_float) > 0 and len(numbers_int) == 0:
                # print(numbers_float)
                numbers = numbers_float
            elif len(numbers_float) > 0 and len(numbers_int) > 0:
                int_float = numbers_int + numbers_float
                # print(int_float)
                numbers = int_float
            else:
                print("不存在整型与浮点型数据。")

            if len(numbers) > 0:
                data_list = second_line.split()
                data_list[number_po] = str(new_number)
                # updated_line = second_line.replace(str(numbers[number_po]), str(new_number), 1)
                updated_line = ' '.join(data_list) + '\n'
                line = updated_line
            print("原始数据集中，数字已成功替换。")
            return line
    except IOError:
        print("无法打开文件或读取数据出错。")
    print("无法替换第二行的第一个数字。")

# 这是一个将所需数据增加到指定txt文件中的函数，file_path 代表了指定文件 data 代表自己需要增加的数据 position 代表了需要增加的位
# 置
def overwrite_and_insert_txt_file(file_path, n, file_to_insert):
    try:
        with open(file_path, 'r') as original_file:
            lines = original_file.readlines()

        with open(file_to_insert, 'r') as insert_file:
            data_to_insert = insert_file.read()

        # 在第n行之后覆写插入另一个txt文件的内容
        lines[n:] = [data_to_insert + '\n']

        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("文件覆写和插入成功！")

    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
    except Exception as e:
        print("发生了一个错误：", e)


# 这是一个将所需数据（该数据内容为行内容，而不是文件）增加到指定txt文件中的函数，file_path 代表了指定文件 data 代表自己需要增加的数据 position 代表了需要增加的位
# 置
def add_lines_to_txt_file(file_path, data, position):
    try:
        # with open(file_path, 'a') as file:
        #     file.write('\n')
        with open(file_path, 'r+') as file:
            lines = file.readlines()
            lines.insert(position, data)
            file.seek(0)
            file.writelines(lines)
        print("1、数据已成功添加到文件中。")
    except IOError:
        print("1、无法打开文件或写入数据出错。")

# 编写一个用于判断每一个line中数字的多少
def detect_num_in_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            count_line = 0
            for line in lines:
                count_num = 0
                count_line += 1
                for num in line.split(' '):
                    if num.isdigit():
                        count_num += 1
                    else:
                        try:
                            float(num)
                            count_num += 1
                        except ValueError:
                            continue
                # 返回我需要的内容，即盒子的长宽高
                if count_num == 5:
                    break
    except IOError:
        print("无法打开文件或读取数据出错。")
    return count_line


# 重写我们的数据文件
def alter(file_name, skip_num, num_atoms):
    file_data = ""
    with open(file_name, "r", encoding="utf-8") as f: # 跳过数据文件重写我们的内容，为扩胞做准备
        if num_atoms == -1:
            count_lin = 0
            for line in f:
                count_lin += 1
                if count_lin > skip_num:
                    file_data += line
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(file_data)
        else:
            lin_num = 0 # 更换原子id值的大小
            lines = f.readlines()
            num_lines = len(lines)
            # print(num_lines)
            for line in range(num_lines):
                # lin_num += 1
                print(line)
                replace_number_in_line(file_name, line + 1, line, 0)


# 将extra文件夹下的更改后的文件复制到extra_c文件夹中
def copy_files(source_folder, destination_folder):
    try:
        # 创建目标文件夹（如果不存在）
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # 获取源文件夹中的所有文件列表
        files = os.listdir(source_folder)

        for file in files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # 判断路径是否是文件
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)  # 使用 copy2 以保留文件的元数据

        print("文件复制完成！")
    except Exception as e:
        print("发生错误：", e)

# 获得指定路径下文件的名字
def get_file_names_in_directory(directory):
    try:
        file_names = os.listdir(directory)
        return file_names
    except Exception as e:
        print("发生错误：", e)
        return []

# 更改文件后缀
# 从原始文件夹中获取需要处理的基文件，以及放大的倍数

def Change_func(type, multi, x_lenths, y_lenths, z_lenths):
    # multi = [a, b, c]
    if type == 'ia':
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ia_ori.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num, number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num, number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num, number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容
            # print(file_data)

    elif type == 'ib':
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ib_ori.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容

    elif type == 'ic':
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ic_ori.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容

    elif type == 'id':
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/id_ori.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容

    elif type == 'ie':
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ie_ori.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容

    else:
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/Origin_221.txt'
        with open(file_name, "r", encoding="utf-8") as f:
            lin_num = -1
            file_data = ""
            for line in f:
                number_po_x = 2
                number_po_y = 3
                number_po_z = 4
                lin_num += 1
                new_number_x = (multi[0] - 1) * x_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_x)  # 获得x方向位置
                new_number_y = (multi[1] - 1) * y_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_y)  # 获得y方向位置
                new_number_z = (multi[2] - 1) * z_lenths + get_number_from_line(file_name, lin_num,
                                                                                number_po_z)  # 获得z方向位置
                line_x = replace_number_in_line4lines(line, new_number_x, number_po_x)  # 替换原始的数据内容
                line_y = replace_number_in_line4lines(line_x, new_number_y, number_po_y)  # 替换原始的数据内容
                line_z = replace_number_in_line4lines(line_y, new_number_z, number_po_z)  # 替换原始的数据内容
                file_data += line_z  # 增加原始数据中的内容

    return file_data


# 创造一个txt文件
def create_txt_file(file_path):
    try:
        with open(file_path, 'w') as txt_file:
            pass
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 获得拼接结束后的粒子文件
def mul_atoms(mul_x, mul_y, mul_z, r_a, r_b, r_c, r_d, r_e):
    # 生成随机点的坐标，

    min_coord_x = 1  # x坐标的最小值
    max_coord_x = mul_x  # x坐标的最大值

    min_coord_y = 1  # y坐标的最小值
    max_coord_y = mul_y  # y坐标的最大值

    min_coord_z = 1  # z坐标的最小值
    max_coord_z = mul_z  # z坐标的最大值

    print(f'首先确定放大倍数: \nx方向放大 {max_coord_x} 倍；\n'
          f'\ny方向放大 {max_coord_y} 倍；\n'
          f'\nz方向放大 {max_coord_z} 倍\n\n'
          f'共放大{max_coord_z*max_coord_y*max_coord_x}倍\n'
          f'粒子总数约为：{max_coord_z*max_coord_y*max_coord_x*80}个')

    num_points = max_coord_x * max_coord_y * max_coord_z  # 总共的点数
    print(num_points)

    # 使用集合来跟踪已生成的坐标
    generated_coords = set()

    # 生成不重复的随机点坐标
    points_r = []
    while len(points_r) < num_points:
        x = random.randint(min_coord_x, max_coord_x)
        y = random.randint(min_coord_y, max_coord_y)
        z = random.randint(min_coord_z, max_coord_z)

        coord = (x, y, z)
        if coord not in generated_coords:
            generated_coords.add(coord)
            points_r.append(coord)

    points = np.array(points_r)

    # 打乱点的顺序，以确保随机性
    np.random.shuffle(points)
    print(points)

    # 每一种缺陷在粒子总数中的比例，但不意味着缺陷数量占据粒子总数的比例，要进行换算
    # 缺陷比例
    ratio_ia = r_a
    ratio_ib = r_b
    ratio_ic = r_c
    ratio_id = r_d
    ratio_ie = r_e

    #
    ia_num = int(ratio_ia * num_points)
    ib_num = int(ratio_ib * num_points)
    ic_num = int(ratio_ic * num_points)
    id_num = int(ratio_id * num_points)
    ie_num = int(ratio_ie * num_points)
    ori_num = num_points - (ie_num + id_num + ic_num + ib_num + ia_num)


    # 将点坐标分成六份
    # 这个下面好像还有些问题，需要改一下，改完了
    ia_position_alti = np.zeros((ia_num, 3))
    ib_position_alti = np.zeros((ib_num, 3))
    ic_position_alti = np.zeros((ic_num, 3))
    id_position_alti = np.zeros((id_num, 3))
    ie_position_alti = np.zeros((ie_num, 3))
    ori_position_alti = np.zeros((ori_num, 3))

    for num in range(1, num_points + 1):
        if num in range(1, ia_num + 1):
            ia_position_alti[num - 1, :] = points[num - 1, :]
        elif num in range(ia_num + 1, ia_num + ib_num + 1):
            ib_position_alti[num - ia_num - 1, :] = points[num - 1, :]
        elif num in range(ia_num + ib_num + 1, ia_num + ib_num + ic_num + 1):
            ic_position_alti[num - ia_num - ib_num - 1, :] = points[num - 1, :]
        elif num in range(ia_num + ib_num + ic_num + 1, ia_num + ib_num + ic_num + id_num + 1):
            id_position_alti[num - ia_num - ib_num - ic_num - 1, :] = points[num - 1, :]
        elif num in range(ia_num + ib_num + ic_num + id_num + 1, ia_num + ib_num + ic_num + id_num + ie_num + 1):
            ie_position_alti[num - ia_num - ib_num - ic_num - id_num - 1, :] = points[num - 1, :]
        else:
            ori_position_alti[num - ia_num - ib_num - ic_num - id_num - ie_num - 1, :] = points[num - 1, :]

    print(ia_position_alti)

    # 指定你想创建的txt文件的路径
    file_path = "/home/ps/YMZ/py_tests_mul/temp/Origin_221.txt"
    create_txt_file(file_path)

    file_path_ori = '/home/ps/YMZ/py_tests_mul/ori/Origin_221.txt'

    x_lenths = get_number_from_line(f'{file_path_ori}', 3, 1) - get_number_from_line(f'{file_path_ori}', 3, 0)
    y_lenths = get_number_from_line(f'{file_path_ori}', 4, 1) - get_number_from_line(f'{file_path_ori}', 4, 0)
    z_lenths = get_number_from_line(f'{file_path_ori}', 5, 1) - get_number_from_line(f'{file_path_ori}', 5, 0)

    print(x_lenths)
    print(y_lenths)
    print(z_lenths)

    # 每一次都要增加相应的元素，并更新原文件
    # 先扩一下，ia构型
    file_data = ''
    for i in range(1, ia_num + 1):
        multi = ia_position_alti[i - 1, :]
        type_i = 'ia'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ib_num + 1):
        multi = ib_position_alti[i - 1, :]
        type_i = 'ib'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)
    for i in range(1, ic_num + 1):
        multi = ic_position_alti[i - 1, :]
        type_i = 'ic'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)
    for i in range(1, id_num + 1):
        multi = id_position_alti[i - 1, :]
        type_i = 'id'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ie_num + 1):
        multi = ie_position_alti[i - 1, :]
        type_i = 'ie'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ori_num + 1):
        multi = ori_position_alti[i - 1, :]
        type_i = 'ori'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    add_lines_to_txt_file(file_path, file_data, -1)  # 将更换后的数据增加到原有的数据文件中

    file_path = "/home/ps/YMZ/py_tests_mul/temp"
    return file_path

if __name__ == "__main__":
    # # # 1
    start_time = time.time()

    # Your code here
    file_path_ori = '/home/ps/YMZ/py_tests_mul/ori/Origin_221.txt'

    # 需要生成n组实验对象
    # 更新文件的名称
    examples_num = 11

    for i in range(1, examples_num):
        copy_files(f'/home/ps/YMZ/py_tests_mul/ori/test_ori', f'/home/ps/YMZ/py_tests_mul/ori/ori')
        time_use = time.time()
        # 转换为.txt文件
        folder_new_name = str(time_use) + ".txt"
        os.rename(f'/home/ps/YMZ/py_tests_mul/ori/ori/Origin_221.txt',
                  f'/home/ps/YMZ/py_tests_mul/ori/ori/{folder_new_name}')

    # 将得到的extra中的粒子数据与ori文件进行合并
    name_list = os.listdir(f'/home/ps/YMZ/py_tests_mul/ori/ori')

    # 循环更新对应的数据
    for i in range(1, examples_num):
        print(
            "------------------------------------------Part 1 Begin----------------------------------------------------")
        # # # 第一步首先获得要更改的第一个数据内容
        # # # 原始数据集中的原子大小

        np.set_printoptions(threshold=np.inf)
        # 先进行所需要实验组的原子拼接
        mul_x = 3
        mul_y = 5
        mul_z = 5

        r_a = 0.00
        r_b = 0.00
        r_c = 0.00
        r_d = 0.00
        r_e = 0.00

        # 在相同的比值下同时进行num实验
        file_path = mul_atoms(mul_x, mul_y, mul_z, r_a, r_b, r_c, r_d, r_e)
        print(file_path)

        number_ori = get_number_from_line(f'{file_path_ori}', 1, 0)

        if number_ori is not None:
            print("1、原始文件中，第二行的第一个数字是:", number_ori)
        else:
            print("1、原始文件中，无法获取第二行的第一个数字。")

        # 要增加的原子大小，这个地方设置对应的ia，ib，ic构型的晶格内容
        file_path_extra = '/home/ps/YMZ/py_tests_mul/extra/Origin_221.txt'

        copy_files(file_path, '/home/ps/YMZ/py_tests_mul/extra')  # 将原有的数据文件复制到extra路径下

        # # # 3.1 获得待增加晶格的长，宽和高
        print(
            "------------------------------------------Part 3 Begin----------------------------------------------------")
        x_line = get_number_from_line(f'{file_path_ori}', 3, 1) - get_number_from_line(f'{file_path_ori}', 3, 0)
        print("x方向的长度为：", x_line)
        y_line = get_number_from_line(f'{file_path_ori}', 4, 1) - get_number_from_line(f'{file_path_ori}', 4, 0)
        print("y方向的长度为：", y_line)
        z_line = get_number_from_line(f'{file_path_ori}', 5, 1) - get_number_from_line(f'{file_path_ori}', 5, 0)
        print("z方向的长度为：", z_line)

        alter(f'{file_path_extra}', 0, 0)  # 更换原子的id值

        overwrite_and_insert_txt_file(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', 14,
                                      f'{file_path_extra}')  # 23.8.6 10：332
        #
        # 4 要更改对应的箱长和粒子总数
        # 4.1 先对粒子总数进行更改
        number_change = get_number_from_line(f'{file_path_extra}', -1, 0)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', number_change, 1, 0)
        # 4.2 改变盒子的大小
        data = np.loadtxt(f'{file_path_extra}')
        # data = np.array(data)
        data = np.sort(data, axis=0)
        print(data)

        x_max = data[-1, 2]
        x_min = data[0, 2]
        y_max = data[-1, 3]
        y_min = data[0, 3]
        z_max = data[-1, 4]
        z_min = data[0, 4]

        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', x_max, 3, 1)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', x_min, 3, 0)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', y_max, 4, 1)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', y_min, 4, 0)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', z_max, 5, 1)
        replace_number_in_line(f'/home/ps/YMZ/py_tests_mul/ori/ori/{name_list[i-1]}', z_min, 5, 0)

    Change_txt2dat.Statas_Processing('/home/ps/YMZ/py_tests_mul/ori/ori/')

    end_time = time.time()
    # 该程序总共运行时间
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
