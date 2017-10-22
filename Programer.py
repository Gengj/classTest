#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: Gengj
@license: (C) Copyright 2013-2017.
@contact: 35285770@qq.com
@software: NONE
@file: Programer.py
@time: 17/10/22 下午6:45
@desc:
'''


class Programer(object):
    hobby = 'play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('My name is', self.name, self._age, 'years old')

