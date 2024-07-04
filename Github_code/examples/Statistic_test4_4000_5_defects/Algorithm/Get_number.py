import os
import random
import numpy as np
import time
import shutil


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

