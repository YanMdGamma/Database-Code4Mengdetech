import numpy as np
import scipy.io as sio
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

def replicative_solution(n_0620_t1, sphere_radium, x_max, x_min, y_max, y_min, z_max, z_min):
    create_spare_atoms = np.zeros((1, 6))  # 创建一个虚拟粒子的外层面包糠
    num_last = n_0620_t1.shape[0] # 一共有多少个粒子
    # print('粒子数量为：', num_last)
    atoms_id = num_last
    count_atom = 0
    type_ = 1
    # 如果对应的粒子距离边界的长度要小于球壳半径，就在外侧覆盖一层类周期性粒子
    # 1、扩充6个面
    for spare_num in range(n_0620_t1.shape[0]):
        # print(abs(n_0620_t1[spare_num][2] - x_max))

        if abs(n_0620_t1[spare_num][2] - x_max) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            print(count_atom)
            x_change = n_0620_t1[spare_num][2] - (x_max-x_min)
            # print('修改后的x大小：', x_change)
            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, x_change, n_0620_t1[spare_num][3], n_0620_t1[spare_num][4], n_0620_t1[spare_num][5]), axis=None)))

            # print(create_spare_atoms)
            # 如果对应的构型在所需的棱上，我们就在扩胞一次
            # 如果对应点位在接近于xmax的平面，并且和zmin的距离小于4.2埃米
            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

            #     如果对应的棱上满足相应的点坐标位置，就在扩大一次点的坐标信息
                if abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] + (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

                elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应点位在接近于xmax的平面，并且和zmax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

            #     如果对应的棱上满足相应的点坐标位置，就在扩大一次点的坐标信息
                if abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] + (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

                elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应点位在接近于xmax的平面，并且和ymin的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应点位在接近于xmax的平面，并且和ymax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] + (y_max - y_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))

        if abs(n_0620_t1[spare_num][2] - x_min) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            x_change = n_0620_t1[spare_num][2] + (x_max-x_min)
            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, x_change, n_0620_t1[spare_num][3], n_0620_t1[spare_num][4],
                 n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应的构型在所需的棱上，我们就在扩胞一次
            # 如果对应点位在接近于xmin的平面，并且和zmin的距离小于4.2埃米
            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

                #     如果对应的棱上满足相应的点坐标位置，就在扩大一次点的坐标信息
                if abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] + (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

                elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] - (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))


            # 如果对应点位在接近于xmin的平面，并且和zmax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

                #     如果对应的棱上满足相应的点坐标位置，就在扩大一次点的坐标信息
                if abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] + (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

                elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                    count_atom += 1
                    num_last = num_last + 1
                    x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                    z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                    y_change = n_0620_t1[spare_num][3] - (y_max - y_min)

                    create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                        (num_last, type_, x_change, y_change, z_change,
                         n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应点位在接近于xmin的平面，并且和ymax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应点位在接近于xmin的平面，并且和ymin的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] + (y_max - y_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))


        if abs(n_0620_t1[spare_num][3] - y_min) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            y_change = n_0620_t1[spare_num][3] + (y_max-y_min)

            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, n_0620_t1[spare_num][2], y_change, n_0620_t1[spare_num][4],
                 n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应的构型在所需的棱上，我们就在扩胞一次
            # 如果对应点位在接近于ymin的平面，并且和zmin的距离小于4.2埃米
            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] + (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))


            # 如果对应点位在接近于ymin的平面，并且和zmax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] + (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

        if abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            y_change = n_0620_t1[spare_num][3] - (y_max-y_min)

            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, n_0620_t1[spare_num][2], y_change, n_0620_t1[spare_num][4],
                 n_0620_t1[spare_num][5]), axis=None)))

            # 如果对应的构型在所需的棱上，我们就在扩胞一次
            # 如果对应点位在接近于ymax的平面，并且和zmin的距离小于4.2埃米
            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))


            # 如果对应点位在接近于ymax的平面，并且和zmax的距离小于4.2埃米
            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

        if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            z_change = n_0620_t1[spare_num][4] + (z_max-z_min)

            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, n_0620_t1[spare_num][2], n_0620_t1[spare_num][3], z_change,
                 n_0620_t1[spare_num][5]), axis=None)))

        if abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            z_change = n_0620_t1[spare_num][4] - (z_max-z_min)

            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, n_0620_t1[spare_num][2], n_0620_t1[spare_num][3], z_change,
                 n_0620_t1[spare_num][5]), axis=None)))

    np.save('Replicative.npy', create_spare_atoms)
    return create_spare_atoms