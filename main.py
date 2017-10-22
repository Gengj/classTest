#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Gengj
@license: (C) Copyright 2013-2017.
@contact: 35285770@qq.com
@software: NONE
@file: main.py
@time: 17/10/22 下午7:23
@desc:
'''
from Programer import Programer
from BackendProgramer import BackendProgramer


def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    gj = BackendProgramer('Gengjia', 20, 130, 'Python')
    sb = BackendProgramer('WAHT???', 20, 130, 'Java')

    print('dir(gj) is :\n', dir(gj))
    print("==============================================")

    print('gj.__dict__ is :\n', gj.__dict__)
    print("==============================================")

    print('type(gj) is :\n', type(gj))
    print("==============================================")

    print('isinstance(gj,BackendProgramer is ', isinstance(gj, BackendProgramer))
    print("==============================================")

    print('isinstance(gj,Programer is ', isinstance(gj, Programer))

    print("==============================================")
    print("introduce(gj) is \n", introduce(gj))
    print("==============================================")
    print("gj.get_hobby() is \n", gj.get_hobby())
    print("==============================================")
    print("gj.get_weight()is %d \n" % (gj.get_weight))
    print("==============================================")
    print("Programer.get_hobby() is \n", Programer.get_hobby())
    print("==============================================")
    print("gj.self_introduction() is \n", gj.self_introduction())
    print("==============================================")
    introduce(sb)
    print("==============================================")
