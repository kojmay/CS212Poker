#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 05/06/2018 23:36
# @Author  : HaifengMay
# @Site    : 
# @File    : Shuffling.py

ta_data = [['Peter', 'USA', 'CS262'],
           ['Andy', 'USA', 'CS212'],
           ['Sarah', 'England', 'CS101'],
           ['Gundega', 'Latvia', 'CS373'],
           ['Job', 'USA', 'CS387'],
           ['Sean', 'USA', 'CS253']]

ta_300 = [ name+" is the TA for "+classnum for name, country, classnum in ta_data if classnum.find('S3')>0]
print ta_300