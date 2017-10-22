#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Gengj
@license: (C) Copyright 2013-2017.
@contact: 35285770@qq.com
@software: NONE
@file: BackendProgramer.py
@time: 17/10/22 下午7:20
@desc:
'''

from Programer import Programer

class BackendProgramer(Programer):

    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

