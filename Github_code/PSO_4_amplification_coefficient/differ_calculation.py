import numpy as np
import scipy.io as sio

def calculate_differ_de():
    # Load MAT file
    id1data = sio.loadmat('id1.mat')  # Assume that all variables are stored in the data.mat file
    id2data = sio.loadmat('id2.mat')
    ie1data = sio.loadmat('ie1.mat')
    ie2data = sio.loadmat('ie2.mat')
    fcdata = sio.loadmat('f_c.mat')
    scdata = sio.loadmat('s_c.mat')

    # Extract variables from the loaded data
    id1 = id1data['id1']
    id2 = id2data['id2']
    ie1 = ie1data['ie1']
    ie2 = ie2data['ie2']
    f_c = fcdata['f_c']
    s_c = scdata['s_c']


    # Example Initialize summ
    summ = np.zeros((15, 1))

    # There are 15 different curves
    for j in range(15):
        if j == 0:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id1 - id2) ** 2, axis=1)))
        elif j == 1:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id1 - ie1) ** 2, axis=1)))
        elif j == 2:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id1 - ie2) ** 2, axis=1)))
        elif j == 3:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id1 - f_c) ** 2, axis=1)))
        elif j == 4:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id1 - s_c) ** 2, axis=1)))
        elif j == 5:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id2 - ie1) ** 2, axis=1)))
        elif j == 6:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id2 - ie2) ** 2, axis=1)))
        elif j == 7:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id2 - f_c) ** 2, axis=1)))
        elif j == 8:
            summ[j, 0] = np.mean(np.sqrt(np.sum((id2 - s_c) ** 2, axis=1)))
        elif j == 9:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ie1 - ie2) ** 2, axis=1)))
        elif j == 10:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ie1 - f_c) ** 2, axis=1)))
        elif j == 11:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ie1 - s_c) ** 2, axis=1)))
        elif j == 12:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ie2 - f_c) ** 2, axis=1)))
        elif j == 13:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ie2 - s_c) ** 2, axis=1)))
        elif j == 14:
            summ[j, 0] = np.mean(np.sqrt(np.sum((f_c - s_c) ** 2, axis=1)))

    # Save summ as a MAT file
    sio.savemat('differ_de.mat', {'summ': summ})

def calculate_differ_abc():
    # Load MAT file
    iadata = sio.loadmat('ia.mat')  # Assume that all variables are stored in the data.mat file
    ibdata = sio.loadmat('ib.mat')
    icdata = sio.loadmat('ic.mat')
    fcdata = sio.loadmat('f_c.mat')
    scdata = sio.loadmat('s_c.mat')

    # Extract variables from the loaded data
    ia = iadata['ia']
    ib = ibdata['ib']
    ic = icdata['ic']
    f_c = fcdata['f_c']
    s_c = scdata['s_c']


    # Example Initialize summ
    summ = np.zeros((10, 1))

    # There are 10 different curves
    for j in range(10):
        if j == 0:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ia - ib) ** 2, axis=1)))
        elif j == 1:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ia - ic) ** 2, axis=1)))
        elif j == 2:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ib - ic) ** 2, axis=1)))
        elif j == 3:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ia - f_c) ** 2, axis=1)))
        elif j == 4:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ia - s_c) ** 2, axis=1)))
        elif j == 5:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ib - f_c) ** 2, axis=1)))
        elif j == 6:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ib - s_c) ** 2, axis=1)))
        elif j == 7:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ic - f_c) ** 2, axis=1)))
        elif j == 8:
            summ[j, 0] = np.mean(np.sqrt(np.sum((ic - s_c) ** 2, axis=1)))
        elif j == 9:
            summ[j, 0] = np.mean(np.sqrt(np.sum((f_c - s_c) ** 2, axis=1)))

    # Save summ as a MAT file
    sio.savemat('differ_abc.mat', {'summ': summ})
