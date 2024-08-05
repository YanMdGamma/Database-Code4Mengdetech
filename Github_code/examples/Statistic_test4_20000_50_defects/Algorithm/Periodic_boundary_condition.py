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
                # 
                for num in second_line.split(' '):
                    if num.isdigit():
                        numbers_int.append(int(num))
                        # print(numbers_int) # 
                    else:
                        try:
                            float(num)
                            numbers_float.append(float(num))
                            # print(numbers_float) # 
                        except ValueError:
                            continue
                # 
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

def replicative_solution(n_0620_t1, sphere_radium, x_max, x_min, y_max, y_min, z_max, z_min):
    create_spare_atoms = np.zeros((1, 6))  
    num_last = n_0620_t1.shape[0] 
    # print('particle number：', num_last)
    atoms_id = num_last
    count_atom = 0
    type_ = 1
    # 
    # 1、6 faces
    for spare_num in range(n_0620_t1.shape[0]):
        # print(abs(n_0620_t1[spare_num][2] - x_max))

        if abs(n_0620_t1[spare_num][2] - x_max) < sphere_radium:
            count_atom += 1
            num_last = num_last + 1
            print(count_atom)
            x_change = n_0620_t1[spare_num][2] - (x_max-x_min)
            create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                (num_last, type_, x_change, n_0620_t1[spare_num][3], n_0620_t1[spare_num][4], n_0620_t1[spare_num][5]), axis=None)))

            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

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

            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

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

            elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] - (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))

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

            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)
                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

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


            elif abs(n_0620_t1[spare_num][4] - z_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                z_change = n_0620_t1[spare_num][4] - (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, n_0620_t1[spare_num][3], z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

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

            elif abs(n_0620_t1[spare_num][3] - y_max) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                x_change = n_0620_t1[spare_num][2] + (x_max - x_min)
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, x_change, y_change, n_0620_t1[spare_num][4],
                     n_0620_t1[spare_num][5]), axis=None)))

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

            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] + (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))


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

            if abs(n_0620_t1[spare_num][4] - z_min) < sphere_radium:
                count_atom += 1
                num_last = num_last + 1
                y_change = n_0620_t1[spare_num][3] - (y_max - y_min)
                z_change = n_0620_t1[spare_num][4] + (z_max - z_min)

                create_spare_atoms = np.vstack((create_spare_atoms, np.concatenate(
                    (num_last, type_, n_0620_t1[spare_num][2], y_change, z_change,
                     n_0620_t1[spare_num][5]), axis=None)))

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

    sio.savemat('Replicative.mat', {'mydata': create_spare_atoms})
    return create_spare_atoms

# 
