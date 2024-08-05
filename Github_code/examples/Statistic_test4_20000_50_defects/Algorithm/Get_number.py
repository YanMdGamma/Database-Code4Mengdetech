import os
import random
import numpy as np
import time
import shutil


def get_number_from_line(file_path, lin_num, number_po):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[lin_num]
                numbers_int = []
                numbers_float = []
                for num in second_line.split(' '):
                    if num.isdigit():
                        numbers_int.append(int(num))
                    else:
                        try:
                            float(num)
                            numbers_float.append(float(num))
                        except ValueError:
                            continue

                if len(numbers_int) > 0 and len(numbers_float) == 0:  
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
                    return print("No more float and int value!")
    except IOError:
        print("Cannot open the file!!")
    return None

