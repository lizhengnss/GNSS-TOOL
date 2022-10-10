#!/usr/bin/env python3
# coding=utf-8
"""
@author: lizhen Created on 2022.10.10
"""

def ReadMyResult(_file, _isvel, _isatt):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split(",")
            if (_isvel and _isatt):
                result.update({round(float(eachData[1]), 2):
                                   { 'b':float(eachData[2]),   'l':float(eachData[3]),    'h':float(eachData[4]),
                                    'vb':float(eachData[13]), 'vl':float(eachData[12]), 'vh':float(eachData[14]),
                                     "r":float(eachData[18]), "p":float(eachData[19]), "y":float(eachData[20]),
                                   'num':float(eachData[9]),
                                # 'ratio':float(eachData[11]),
                                  'stat':float(eachData[8])  } })
            elif _isvel:
                result.update({round(float(eachData[1]), 2):
                                   { 'b':float(eachData[2]),   'l':float(eachData[3]),    'h':float(eachData[4]),
                                    'vb':float(eachData[13]), 'vl':float(eachData[12]), 'vh':float(eachData[14]),
                                   'num':float(eachData[9]),
                                # 'ratio':float(eachData[11]),
                                  'stat':float(eachData[8])  } })
            else:
                result.update({round(float(eachData[1])):
                                   { 'b':float(eachData[2]),   'l':float(eachData[3]),    'h':float(eachData[4]),
                                   'num':float(eachData[9]),
                               #  'ratio':float(eachData[11]),
                                  'stat':float(eachData[8])  } })
    return result


def ReadLeadorResult(_file, _isvel):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split()

            result.update({ float(eachData[0]): {   'b':float(eachData[5]),   'l':float(eachData[6]),   'h':float(eachData[7]),
                                                   'vb':float(eachData[11]), 'vl':float(eachData[12]), 'vh':float(eachData[13]),
                                                 'stat':float(eachData[8])} })   #pos
    return result


def ReadIERefResult(_file, _isvel, _isatt):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split(",")

            if _isatt:
                result.update({round(float(eachData[1]), 2): {'b': float(eachData[2]), 'l': float(eachData[3]), 'h': float(eachData[4]),
                                                              'vb': float(eachData[6]), 'vl': float(eachData[5]),'vh': float(eachData[7]),
                                                              "r": float(eachData[8]), "p": float(eachData[9]), "y": float(eachData[10]),
                                                              'stat': float(eachData[13])}})  # note stat shoule be 14
            else:
                result.update({round(float(eachData[1]), 2): {'b': float(eachData[2]), 'l': float(eachData[3]),
                                                              'h': float(eachData[4]),
                                                              'vb': float(eachData[6]), 'vl': float(eachData[5]),
                                                              'vh': float(eachData[7]),
                                                              'stat': float(eachData[13])}})  # note stat shoule be 14
    return result


def ReadRtklibResult(_file, _isvel):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split()
            result.update({float(eachData[1]):
                               {'b': float(eachData[2]), 'l': float(eachData[3]), 'h': float(eachData[4]),
                                'num': float(eachData[6]),
                              #  'ratio': float(eachData[13]),
                                'stat': float(eachData[5])}})
    return result


def ReadGlabResult(_file, _isvel):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split()
            result.update({float(eachData[1]):
                               {'b': float(eachData[3]), 'l': float(eachData[2]), 'h': float(eachData[4]),
                                'num': 0,
                                'stat': 0}})
    return result


def ReadPandaResult(_file, _isvel):
    result = {}
    with open(_file, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine.startswith("%"):  # ignore comment line
                continue
            eachData = eachLine.split()
            result.update({float(eachData[7]):
                               {'b': float(eachData[15]) , 'l': float(eachData[16]), 'h': float(eachData[17]),
                                'num': 0,
                                'stat': 0}})
    return result
