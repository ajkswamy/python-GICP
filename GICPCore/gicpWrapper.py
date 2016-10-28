import subprocess
from swcFuncs import transSWC
from asciiSWCConverters import ascii2swc, swc2ascii
import tempfile
import os
import shutil
import time
import numpy as np


def getTransformFromGICPOut(outStr, marker):

    outSplit = outStr.splitlines()
    markerInd = outSplit.index(marker)
    return np.loadtxt(outSplit[markerInd + 1: markerInd + 4])


def runGICPCPP(testASCII, refASCII, tempDir, logFile=None):

    filePath = os.path.split(__file__)[0]
    old_cwd = os.getcwd()
    os.chdir(tempDir)
    out = subprocess.check_output([os.path.join(filePath, 'gicp', 'test_gicp'),
                                   testASCII,
                                   refASCII,
                                   '--t_base',
                                   os.path.join(filePath, 'gicp', 'data', 'sample_base.tfm')],
                                  stderr=subprocess.STDOUT)
    os.chdir(old_cwd)
    if logFile:
        with open(logFile, 'w') as fle:
            fle.write(out)

    baseT = getTransformFromGICPOut(out, 't_base:')
    startT = getTransformFromGICPOut(out, 't0:')
    solT = getTransformFromGICPOut(out, 't1:')

    return baseT, startT, solT


def runGICP(refInFile, testInFile, outFile, deleteTempFiles=True):
    tempDir = tempfile.mkdtemp(dir=os.getcwd())
    inAsciiFiles = []
    inSWCFiles = []
    for inFle in [refInFile, testInFile]:
        if inFle.endswith('.swc'):
            thrash, tempFile = tempfile.mkstemp(dir=tempDir, suffix='.ascii')
            swc2ascii(inFle, tempFile)
            inSWCFiles.append(inFle)
            inAsciiFiles.append(tempFile)
        elif inFle.endswith('.ascii'):
            thrash, tempFile = tempfile.mkstemp(dir=tempDir, suffix='.swc')
            inAsciiFiles.append(inFle)
            ascii2swc(inFle, tempFile)
            inSWCFiles.append(tempFile)
        else:
            raise(IOError('Unsupported file format for %s. Supported formats are ascii and swc,' % inFle))

    [refAsciiFile, testAsciiFile] = inAsciiFiles
    [refSWCFile, testSWCFile] = inSWCFiles

    baseT, startT, solT = runGICPCPP(testAsciiFile, refAsciiFile, tempDir, outFile + '.log')
    transSWC(testSWCFile, solT[:3, :3], solT[:3, 3], outFile)

    if deleteTempFiles:
        shutil.rmtree(tempDir)
    else:
        print('TempFiles in %s not deleted' % tempDir)





