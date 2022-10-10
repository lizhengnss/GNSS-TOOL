#!/usr/bin/python3
from math import radians, sin
from funcoord import xyz2blh
from funcom import rms, mean
import matplotlib.pyplot as plt

RE = 6378137

class coord(object):
    def __init__(self):
        self.x, self.y, self.z = 0.0, 0.0, 0.0
        self.b, self.l, self.h = 0.0, 0.0, 0.0
    def setValue(self, a, b, c, type):
        self.detx, self.dety, self.detz = [], [], []
        if type == 'xyz':
            self.x, self.y, self.z = a, b, c
            self.b, self.l, self.h = xyz2blh(a, b, c)
            self.l = 180-self.l
        elif type == 'blh':
            self.b, self.l, self.h = a, b, c
        else:
            print('error parameter of function =setvalue=')
            exit(1)

    def getRes(self, x, y, z):
        self.detx.append(radians(x - self.b) * RE)
        self.dety.append(radians(y - self.l) *  RE / sin(radians(y)))
        self.detz.append(z - self.h)


    def statistic(self):
        self.xrms, self.yrms, self.zrms = rms(self.detx), rms(self.dety), rms(self.detz)
        self.xmean, self.ymean, self.zmean = mean(self.detx), mean(self.dety), mean(self.detz)



if __name__ == '__main__':
    calFile = "E:\\VirtualFile\\data\\spp\\my.txt"
    valueTrue = coord()

    valueTrue.setValue( 0.563370879035000E+07,0.173201808333999E+07, -.243398546130001E+07 , 'xyz')

    calValue = {}
    with open(calFile, 'r') as file:
        content = file.readlines()
        for eachLine in content:
            if eachLine[0] == "%":  # ignore comment line
                continue
            eachData = eachLine.split(",")
            calValue.update({ eachData[1]: {'b':float(eachData[2]), 'l':float(eachData[3]), 'h':float(eachData[4])} })

    for epoch, data in calValue.items():
        valueTrue.getRes(data['b'], data['l'], data['h'])

    valueTrue.statistic()    ## get tatistical results

    ## draw figure
    plt.figure(dpi = 100, figsize=(10, 6.18))
    plt.plot(valueTrue.detz, label='rmsh' + str(round(valueTrue.zrms, 3)))
    plt.plot(valueTrue.detx, label = 'rmsb' + str(round(valueTrue.xrms, 3)))
    plt.plot(valueTrue.dety, label = 'rmsl' + str(round(valueTrue.yrms, 3)))

    plt.xlabel('epoch')
    plt.ylabel('m')
    plt.ylim(-10, 10)
    plt.legend()
    plt.grid(True)
    plt.show()

