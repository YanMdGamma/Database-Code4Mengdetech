import numpy as np
# 计算路径
def dis_r(x_4, y_4, z_4, x_s4, y_s4, z_s4):
    dis_r = np.sqrt((x_4 - x_s4)**2 + (y_4 - y_s4)**2 + (z_4 - z_s4)**2)
    return dis_r