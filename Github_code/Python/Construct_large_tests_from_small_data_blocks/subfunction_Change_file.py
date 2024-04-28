import numpy as np
import random
import re

def replace_number(match, new_num):
    number_str = match.group()
    if number_str == '0.0':
        return new_num  # 在这里设置你想要替换的值
    else:
        return number_str

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
                # if int(numbers[number_po]) == 0: # 如果对应的数字是0.0，需要根据正则表达式进行计算
                #     pattern = r'\b\d+(?:\.\d+)?\b'
                #     result = re.sub(pattern, lambda match: replace_number(match, str(new_number)), second_line)
                #     line = result
                # else:
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

if __name__ == "__main__":
    np.set_printoptions(threshold=np.inf)
    # 生成随机点的坐标

    min_coord_x = 1  # x坐标的最小值
    max_coord_x = 6  # x坐标的最大值

    min_coord_y = 1  # y坐标的最小值
    max_coord_y = 8  # y坐标的最大值

    min_coord_z = 1  # z坐标的最小值
    max_coord_z = 9  # z坐标的最大值

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

    # 缺陷比例
    ratio_ia = 0.2
    ratio_ib = 0.1
    ratio_ic = 0.3
    ratio_id = 0.1
    ratio_ie = 0.1

    #
    ia_num = int(ratio_ia * num_points)
    ib_num = int(ratio_ib * num_points)
    ic_num = int(ratio_ic * num_points)
    id_num = int(ratio_id * num_points)
    ie_num = int(ratio_ie * num_points)
    ori_num = num_points - (ie_num + id_num + ic_num + ib_num + ia_num)

    print(ia_num)
    print(ib_num)
    print(ic_num)
    print(id_num)
    print(ie_num)
    print(ori_num)

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
    file_path = "/home/ps/YMZ/py_tests_mul/temp/temporary.txt"
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
    for i in range(1, ia_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ia_ori.txt'
        multi = ia_position_alti[i-1, :]
        type_i = 'ia'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ib_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ib_ori.txt'
        multi = ib_position_alti[i-1, :]
        type_i = 'ib'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)
    for i in range(1, ic_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ic_ori.txt'
        multi = ic_position_alti[i-1, :]
        type_i = 'ic'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)
    for i in range(1, id_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/id_ori.txt'
        multi = id_position_alti[i-1, :]
        type_i = 'id'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ie_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/ie_ori.txt'
        multi = ie_position_alti[i-1, :]
        type_i = 'ie'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    for i in range(1, ori_num+1):
        # i = 0
        file_name = f'/home/ps/YMZ/py_tests_mul/data_base/Origin_221.txt'
        multi = ori_position_alti[i-1, :]
        type_i = 'ori'
        file_data += Change_func(type_i, multi, x_lenths, y_lenths, z_lenths)

    add_lines_to_txt_file(file_path, file_data, -1)  # 将更换后的数据增加到原有的数据文件中
