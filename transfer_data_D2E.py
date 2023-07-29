# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : transfer_data_D2E.py
# Time       ：2022/7/13 13:23
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import os
import shutil
from multiprocessing.dummy import Pool


def transfer_process(filename):
    if not os.path.exists(to_path + filename):
        shutil.copy(from_path + filename, to_path + filename)
        print("copied " + filename)


from_path = "D:/code/SuLab/data/pdb_thread/"
to_path = "E:/pdb_thread/"
if __name__ == '__main__':
    pdbs = os.listdir(from_path)
    print("***start process***")

    pool = Pool(14)
    for pdb in pdbs:
        pool.apply_async(func=transfer_process, args=(pdb, ))
    pool.close()
    pool.join()

    print("***finish process***")
