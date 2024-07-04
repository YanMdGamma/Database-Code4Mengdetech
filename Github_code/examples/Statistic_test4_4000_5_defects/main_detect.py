from Algorithm import threshold_defects, threshold_interstitials, Periodic_boundary_condition, Change_xyz2use
import numpy as np
import scipy.io as sio
from math import pi
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
import my_module


#
# Load the data set and database type
def main(xyz_file_output_path, amplification_coefficient4abc, amplification_coefficient4de, Atom_type, massage_comment):
    data = sio.loadmat('n_0620_t1.mat')
    n_0620_t1 = data['test1']
    f_c_data = sio.loadmat('../f_c.mat')
    f_c = f_c_data['mydata']
    s_c_data = sio.loadmat('../s_c.mat')
    s_c = s_c_data['mydata']
    ia_data = sio.loadmat('../ia.mat')
    ia = ia_data['mydata']
    ib_data = sio.loadmat('../ib.mat')
    ib = ib_data['mydata']
    ic_data = sio.loadmat('../ic.mat')
    ic = ic_data['mydata']
    id1_data = sio.loadmat('../ida.mat')
    id1 = id1_data['mydata']
    id2_data = sio.loadmat('../idd.mat')
    id2 = id2_data['mydata']
    ie1_data = sio.loadmat('../iea.mat')
    ie1 = ie1_data['mydata']
    ie2_data = sio.loadmat('../iee.mat')
    ie2 = ie2_data['mydata']

    f_c_bc_data = sio.loadmat('../f_c_bc.mat')
    f_c_bc = f_c_bc_data['mydata']

    f_c_asv_data = sio.loadmat('../asv.mat')
    f_c_asv = f_c_asv_data['mydata']


    cr = 4.2  # This length should be the theoretical value that can distinguish between 'ib' and 'ic' configurations
    n = 400
    dr = cr / n
    radias_vol = np.zeros((n, 2))
    radias_vol[:, 0] = np.arange(dr, cr + dr, dr)
    radias_vol[:, 1] = 4 / 3 * pi * radias_vol[:, 0]**3

    particle_rdf_test0620_1 = np.zeros((n, 2 * n_0620_t1.shape[0]))

    # Add periodic boundary conditions # extend
    sphere_radium = 4.2
    x_max = 48.4282885418
    x_min = 0.0
    y_max = 30.857209332500002
    y_min = 0.0
    z_max = 29.396923244
    z_min = 0.0

    data = sio.loadmat('n_0620_t1.mat')
    Periodic_boundary_condition.replicative_solution(n_0620_t1, sphere_radium, x_max, x_min, y_max, y_min, z_max, z_min)

    data_add = sio.loadmat('Replicative.mat')
    n_0620_t1_add = data_add['mydata']
    n_0620_t1_add = n_0620_t1_add[1:, :] # Delete a row with all zeros
    n_0620_t1_add = np.concatenate((n_0620_t1, n_0620_t1_add), axis=0)


    particle_rdf_test0620_1 = my_module.all_RDF(n_0620_t1, n_0620_t1_add, particle_rdf_test0620_1, radias_vol, n)
    sio.savemat('start.mat', {'mydata': particle_rdf_test0620_1})

    index = np.arange(1, n + 1)
    percent_stand_test0620_1 = np.zeros((n_0620_t1.shape[0], n))

    for i in range(n_0620_t1.shape[0]):
        for j in range(n):
            percent_stand_test0620_1[i, j] = particle_rdf_test0620_1[j, 2 * i]

    test0620_1 = np.zeros(ia.shape[1])
    test_0620_1 = np.zeros((percent_stand_test0620_1.shape[0], ia.shape[1]))

    for i in range(percent_stand_test0620_1.shape[0]):
        percent_1 = percent_stand_test0620_1[i, :]
        tck = splrep(index, percent_1, k=3)
        test_0620_1[i, :] = splev(index, tck)  # Interpolation

    stand_all = np.vstack((ia[0, :], ib[0, :], ic[0, :], f_c[0, :], s_c[0, :], f_c_bc[0, :], f_c_asv[0, :]))
    fig = plt.figure()
    plt.plot(index, ia[0, :])

    similarity_score_0620_1 = np.zeros((percent_stand_test0620_1.shape[0], 7))
    best_sim = np.zeros((percent_stand_test0620_1.shape[0], 5))

    #
    for i in range(percent_stand_test0620_1.shape[0]):
        test_line = test_0620_1[i, :]
        for j in range(7):
            stand_line = stand_all[j, :]
            d = np.sqrt(np.sum((test_line - stand_line) ** 2))
            mul = amplification_coefficient4abc
            similarity_score_0620_1[i, j] = 1 / (1 + mul * np.mean(d))

        max_simi = np.max(similarity_score_0620_1[i, :])
        temp_list = similarity_score_0620_1[i, :].tolist() # Convert to a normal python array
        max_index = temp_list.index(max_simi) # Get the position of the maximum value
        diff = np.sum(test_line - stand_all[max_index, :]) # All the difference values of the curve are statistically obtained, either the whole is smaller or the whole is larger
        tail_value = test_line[-1] - stand_all[max_index, -1]  # The size of the end value must be the same

        count_m = np.argmax(similarity_score_0620_1[i, :]) + 1
        # Just calculate the curves and the contents of the maximum similarity standard database
        best_sim[i, 0] = count_m
        best_sim[i, 1] = max_simi
        best_sim[i, 2] = diff
        best_sim[i, 3] = tail_value
    #
    # Suppose 'n_0620_t1' and 'best_sim' are your data arrays
    array_coord = n_0620_t1[:, 5]
    array_coord = array_coord.reshape(-1, 1)

    # First we combined the data into 'test_0620_1_use'
    test_0620_1_use = np.concatenate((n_0620_t1[:, :5], best_sim[:, [0, 1]], array_coord, best_sim[:, [2, 3]]), axis=1)
    sio.savemat('stand_all.mat', {'mydata': test_0620_1_use})

    #
    with open('output.txt', 'w') as file:
        #
        ia_detective, ib_detective, ic_detective = threshold_defects.threshold_point_defects(test_0620_1_use, file)

        print('The ID of ia is: ', ia_detective, '\nThe ID of ib is: ', ib_detective, '\nThe ID of ic is: ', ic_detective, file=file)

    ic_test0620_1 = np.zeros((1, 4))
    ia_test0620_1 = np.zeros((1, 4))
    ib_test0620_1 = np.zeros((1, 4))

    best_sim_3 = best_sim[:, 3]
    best_sim_3 = best_sim_3.reshape(-1, 1)

    sio.savemat('stand_all.mat', {'mydata': test_0620_1_use})

    for i in range(best_sim.shape[0]):
        if test_0620_1_use[i, 0] in ia_detective:
            ia_test0620_1 = np.vstack((ia_test0620_1, np.concatenate(
                (test_0620_1_use[i, 0], test_0620_1_use[i, 2:5]), axis=None)))
        elif test_0620_1_use[i, 0] in ib_detective:
            ib_test0620_1 = np.vstack((ib_test0620_1, np.concatenate(
                (test_0620_1_use[i, 0], test_0620_1_use[i, 2:5]), axis=None)))
        elif test_0620_1_use[i, 0] in ic_detective:
            ic_test0620_1 = np.vstack((ic_test0620_1, np.concatenate(
                (test_0620_1_use[i, 0], test_0620_1_use[i, 2:5]), axis=None)))

    ia_test0620_1 = ia_test0620_1[1:, :]
    ib_test0620_1 = ib_test0620_1[1:, :]
    ic_test0620_1 = ic_test0620_1[1:, :]

    sio.savemat('ia.mat', {'mydata': ia_test0620_1})
    sio.savemat('ib.mat', {'mydata': ib_test0620_1})
    sio.savemat('ic.mat', {'mydata': ic_test0620_1})

    #
    point_id = np.concatenate((ia_test0620_1[:, 0], ib_test0620_1[:, 0], ic_test0620_1[:, 0]))
    #
    stand_all_1 = np.vstack([id1[0, :], id2[0, :], ie1[0, :], ie2[0, :], f_c[0, :], s_c[0, :]])
    #
    sio.savemat('stand_all_1.mat', {'mydata': stand_all_1})
    similarity_score_test52 = np.zeros((6, n_0620_t1.shape[0]))
    #
    best_sim = np.zeros((n_0620_t1.shape[0], 4))
    similarity_score_0620_1 = np.zeros((percent_stand_test0620_1.shape[0], 6))

    fig = plt.figure()
    plt.plot(index, ie2[0, :])
    plt.show()

    for i in range(n_0620_t1.shape[0]):
        test_line = test_0620_1[i, :]
        for num_point in range(point_id.shape[0]):
            if n_0620_t1[i, 0] == point_id[num_point]:
                best_sim[i, :2] = 0
                continue
            # else:
        for j in range(6):
            stand_line = stand_all_1[j, :]
            d = np.sqrt(np.sum((test_line - stand_line) ** 2))
            mul = amplification_coefficient4de
            similarity_score_0620_1[i, j] = 1 / (1 + mul * np.mean(d))

        max_simi = np.max(similarity_score_0620_1[i, :])
        temp_list = similarity_score_0620_1[i, :].tolist()  # Convert to a normal python array
        max_index = temp_list.index(max_simi)  # Get the position of the maximum value
        diff = np.sum(test_line - stand_all_1[max_index, :])  # All the difference values of the curve are statistically obtained, either the whole is smaller or the whole is larger
        tail_value = test_line[-1] - stand_all_1[max_index, -1]  #

        count_m = np.argmax(similarity_score_0620_1[i, :]) + 1
        # Just calculate the curves and the contents of the maximum similarity standard database
        best_sim[i, 0] = count_m
        best_sim[i, 1] = max_simi
        best_sim[i, 2] = diff
        best_sim[i, 3] = tail_value

    test_0620_1_use = np.concatenate((n_0620_t1[:, :5], best_sim[:, [0, 1]], array_coord, best_sim[:, [2, 3]]), axis=1)

    sio.savemat('stand_all_later.mat', {'mydata': test_0620_1_use})

    with open('output.txt', 'a') as file:
        # Call the function and pass the file object
        id_detective, ie_detective, ide = threshold_interstitials.threshold_interstitials(test_0620_1_use, file)

    id_test52 = np.zeros((1, 4))
    ie_test52 = np.zeros((1, 4))

    for i in range(best_sim.shape[0]):
        if test_0620_1_use[i, 0] in id_detective:
            id_test52 = np.vstack((id_test52, np.concatenate(
                (test_0620_1_use[i, 0], test_0620_1_use[i, 2:5]), axis=None)))
        elif test_0620_1_use[i, 0] in ie_detective:
            ie_test52 = np.vstack((ie_test52, np.concatenate(
                (test_0620_1_use[i, 0], test_0620_1_use[i, 2:5]), axis=None)))

    id_test52 = id_test52[1:, :]
    ie_test52 = ie_test52[1:, :]
    sio.savemat('id.mat', {'mydata': id_test52})
    sio.savemat('ie.mat', {'mydata': ie_test52})

    with open('output.txt', 'a') as file:
        # Call the function and pass the file object

        print('The ID of ia is: ', ia_detective, '\nThe ID of ib is: ', ib_detective, '\nThe ID of ic is: ',
              ic_detective, file=file)
        print('The positions of ia is: ', ia_test0620_1[0:, 1:], '\nThe positions of ib is: ', ib_test0620_1[0:, 1:],
              '\nThe positions of ic is: ', ic_test0620_1[0:, 1:], file=file)

        print('\nThe ID of id is: ', id_detective, '\nThe ID of ie is: ', ie_detective, '\nThe ID of ide is', ide,
              file=file)
        print('The positions of id is: ', id_test52[0:, 1:], '\nThe positions of ie is: ', ie_test52[0:, 1:],
              file=file)


    with open(xyz_file_output_path, 'w') as xyz_file:
        num_a_atoms = len(ia_test0620_1[0:, 1:])
        num_b_atoms = len(ib_test0620_1[0:, 1:])
        num_c_atoms = len(ic_test0620_1[0:, 1:])
        num_d_atoms = len(id_test52[0:, 1:])
        num_e_atoms = len(ie_test52[0:, 1:])

        xyz_file.write(f"{num_a_atoms + num_b_atoms + num_c_atoms + num_d_atoms + num_e_atoms}\n")
        xyz_file.write(f"{massage_comment}\n")

        # The last one is coordination
        for i in range(0, num_a_atoms):
            x, y, z = map(float, ia_test0620_1[i, 1:][0:])
            xyz_file.write(f"{ia_detective[i]} {Atom_type} {x} {y} {z} {4}\n")

        for i in range(0, num_b_atoms):
            x, y, z = map(float, ib_test0620_1[i, 1:][0:])
            xyz_file.write(f"{ib_detective[i]} {Atom_type} {x} {y} {z} {6}\n")

        for i in range(0, num_c_atoms):
            x, y, z = map(float, ic_test0620_1[i, 1:][0:])
            xyz_file.write(f"{ic_detective[i]} {Atom_type} {x} {y} {z} {6}\n")

        for i in range(0, num_d_atoms):
            x, y, z = map(float, id_test52[i, 1:][0:])
            xyz_file.write(f"{id_detective[i]} {Atom_type} {x} {y} {z} {4}\n")

        for i in range(0, num_e_atoms):
            x, y, z = map(float, ie_test52[i, 1:][0:])
            xyz_file.write(f"{ie_detective[i]} {Atom_type} {x} {y} {z} {4}\n")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if id_test52.shape[0] != 0:
        ax.scatter(id_test52[:, 1], id_test52[:, 2], id_test52[:, 3], c='yellow', marker='o', label='id_test52')

    if ie_test52.shape[0] != 0:
        ax.scatter(ie_test52[:, 1], ie_test52[:, 2], ie_test52[:, 3], c='cyan', marker='o', label='ie_test52')

    if ia_test0620_1.shape[0] != 0:
        ax.scatter(ia_test0620_1[:, 1], ia_test0620_1[:, 2], ia_test0620_1[:, 3], c='red', marker='o', label='ia_test0620_1')

    if ib_test0620_1.shape[0] != 0:
        ax.scatter(ib_test0620_1[:, 1], ib_test0620_1[:, 2], ib_test0620_1[:, 3], c='green', marker='o', label='ib_test0620_1')

    if ic_test0620_1.shape[0] != 0:
        ax.scatter(ic_test0620_1[:, 1], ic_test0620_1[:, 2], ic_test0620_1[:, 3], c='blue', marker='o', label='ic_test0620_1')

    ax.set_xlabel(r'$x_{orientation}$/\AA')
    ax.set_ylabel(r'$y_{orientation}$/\AA')
    ax.set_zlabel(r'$z_{orientation}$/\AA')

    plt.legend(loc='upper left')
    plt.title('10230 particles_detect 10 defects')
    plt.show()

