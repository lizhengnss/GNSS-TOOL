#!/usr/bin/env python3
# coding=utf-8
"""
@author: lizhen Created on 2021.7.7 09:49:36
"""
import sys


def deg2dms(deg):
    """
    @author: lizhen Created on 2021.7.7
    Purpose: Convert degree to degrees, minutes and seconds
    """
    degree = int(deg)
    min = (deg - degree) * 60
    minute = int(min)
    second = (min - minute) * 60
    return degree, minute, second


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('\33[1;31m**Usage 1. deg2dms:  deg2dms deg\33[0m')
        sys.exit(1)
    else:
        mode = sys.argv[1]
        if (mode == 'deg2dms'):
            deg = float(sys.argv[2])
            degree, minute, second = deg2dms(deg)
            print(degree, minute, second)

