import os

def Statas_Processing(ori_dir):
    name_list = os.listdir(ori_dir)
    for name in name_list:
        # print(name)
        ori_name = name
        name = name.split('.')
        # 如果文件名存在后缀
        if name[-1] == 'txt': # and int(name[-2]) > 30000:
            name[-1] = 'dat'
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
