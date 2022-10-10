#!/usr/bin/env python3
# coding=utf-8
"""
@author: lizhen Created on 2019.8.6
"""

def rms(list):
	"""
    @author   : Lizhen
    Version   : 1.0 Created  2019.08.06
    Purpose   : 计算列表的均方根误差
    Input     : list     ——  待计算均方根的列表
    Output    : cal      ——  列表的均方根
	"""
	from math import sqrt
	cal = 0.0
	for each in list:
		cal += each * each
	cal = sqrt(cal / len(list))
	return cal

def std(list):
	"""
    @author   : Lizhen
    Version   : 1.0 Created  2019.08.10
    Purpose   : 计算列表的标准差
    Input     : list     ——  待计算标准差的列表
    Output    : cal      ——  列表的标准差
	"""
	from math import sqrt
	cal = 0.0
	list_mean = mean(list)
	for each in list:
		cal += (each - list_mean) ** 2
	cal = sqrt(cal / len(list))
	return cal

def mean(list):
	"""
    @author   : Lizhen
    Version   : 1.0 Created  2019.08.10
    Purpose   : 计算列表的平均值
    Input     : list     ——  待计算平均值的列表
    Output    : cal      ——  列表的平均值
	"""
	cal = 0.0
	for each in list:
		cal += each
	cal = cal / len(list)
	return cal


def maxabs(list):
	"""
    @author   : Lizhen
    Version   : 1.0 Created  2022.05.7
    Purpose   : 计算列表中绝对值最大的值
    Input     : list     ——  待计算平均值的列表
    Output    : cal      ——  绝对值最大值
    """
	cal = list[0]

	for each in list:
		if abs(each) > cal:
			cal = abs(each)
	return cal