#!/usr/bin/env python3
#coding=utf-8
"""
Created on 2022.10.10 14:48:22
@author: lizhen
用于转换开源slam轨迹结果为tum格式方便使用vio进行评估
"""

from funtime import unix2gps

def vins2tum(vinsFile, tumFile):
    with open(vinsFile, 'r') as infile, open(tumFile, 'w') as outfile:
        content = infile.readlines()
        for eachLine in content:
            eachData = eachLine.split(",")
            unixtime = float(eachData[0]) * 1e-9
            time = unix2gps(unixtime)

            outfile.write( '%.4f %s %s %s %s %s %s %s\n' %
                           (time, eachData[1], eachData[2], eachData[3],
                                  eachData[5], eachData[6], eachData[7], eachData[4])
                         )

def openvins2tum(ovFile, tumFile):
    with open(ovFile, 'r') as infile, open(tumFile, 'w') as outfile:
        content = infile.readlines()
        for eachLine in content:
            if eachLine.startswith("#"):  # ignore comment line
                continue
            eachData = eachLine.split()
            unixtime = float(eachData[0])
            time = unix2gps(unixtime)

            outfile.write( '%.4f %s %s %s %s %s %s %s\n' %
                           (time, eachData[1], eachData[2], eachData[3],
                                  eachData[4], eachData[5], eachData[6], eachData[7])
                         )

if __name__ == '__main__':

    filePath = "E:\\VirtualFile\\data\\vio\\campus对比\\"

    inFile = filePath + "vio.csv"
    outFile = filePath + "vins.csv"

    mode = "vins"

    if mode == "vins":
        vins2tum(inFile, outFile)
    elif mode == "openvins":
        openvins2tum(inFile, outFile)






