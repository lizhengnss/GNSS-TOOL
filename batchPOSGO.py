#!/usr/bin/python3
import sys
import subprocess

def execmd(args):
    """
    @author: lizhen
    Created on 2019.7.18
    Version   : 1.0 Generated
    Purpose   : Use the shell to perform command line
    Input     : Command line
    Output    : return return code, standard output, standard error
    """

    print('\33[36m;---- Execute command: %s ----\33[0m'% args)
    process = subprocess.Popen(args = args, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdoutdata, stderrdata = process.communicate()   #shell error information in stderrdata
    stdoutdata_utf = stdoutdata.decode('utf-8')
    if stdoutdata_utf != '':
        print("\33[131m%s\33[0m" %stdoutdata_utf.rstrip('\r\n'))

    return process.returncode, stdoutdata, stderrdata



if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('\33[1;31m**Usage obsfile obs_basefile brdfile outfile x y z \33[0m')
        sys.exit(-1)

    obsfile = sys.argv[1]
    obs_basefile = sys.argv[2]
    brdfile = sys.argv[3]
    outfile = sys.argv[4]
    x = float(sys.argv[5])
    y = float(sys.argv[6])
    z = float(sys.argv[7])

    with open("ref.ini", 'r') as rfile, open("cfg.ini", 'w') as cfile:
        content = rfile.readlines()
        cfile.writelines(content)

        cfile.write('%s\n' % ("File-GnssObs=" + obsfile))
        cfile.write('%s\n' % ("File-Navigation=" + obs_basefile))
        cfile.write('%s\n' % ("File-GnssBase=" + brdfile))
        cfile.write('%s\n' % ("File-Result=" + outfile))

        cfile.write('%s %14.3f, %14.3f, %14.3f \n' % ("BaseStationPos=", x, y, z))

    args = "./MultiPOS -C cfg.ini -S GRCE -M rtk -L 1"
    execmd(args)





