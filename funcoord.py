#!/usr/bin/python
import math

def xyz2blh(x,y,z):
    RAD2DEG = 180.0/math.pi
    a = 6378137
    e2 = (1.0/298.257223563) * (2.0- 1.0/298.257223563)
    r2 = x*x + y*y + z*z - z*z
    zz = z
    zk = 0

    while(math.fabs(zz-zk) >= 1e-4):
        zk = zz
        sinp = zz / math.sqrt(r2 + zz * zz)
        v = a / math.sqrt(1.0 - e2 * sinp *sinp)
        zz = z +v * e2 * sinp

    if r2 > 1e-12:
        b = math.atan(zz / math.sqrt(r2))
        l = math.atan2(y, x)
        h = math.sqrt(r2 + zz*zz) - v
    else:
        return 0,0,0
    return b*RAD2DEG, l*RAD2DEG, h



if __name__ == '__main__':

    B, L, H = xyz2blh( -2629112.9510 ,  5235662.8777  , 2512742.1710)

    min = (B - int(B)) * 60
    sec = (min - int(min)) *60
    print(int(B), int(min), sec)

    L = 180-L
    min = (L - int(L)) * 60
    sec = (min - int(min)) * 60
    print(int(L), int(min), sec)
    print(H)

    print(B, L, H)