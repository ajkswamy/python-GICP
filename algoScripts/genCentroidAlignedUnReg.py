import os
from GICPCore.swcFuncs import transSWC
import numpy as np
homeFolder = os.path.expanduser('~')

# ----------------------------------------------------------------------------------------------------------------------
# testPath = homeFolder + '/DataAndResults/morphology/OriginalData/chiangOPSInt/'
# refPath = homeFolder + '/DataAndResults/morphology/Registered/chiangOPSInt/'
# expNames = [
#             'Trh-F-000047.CNG',
#             'Trh-M-000143.CNG',
#             'Trh-F-000092.CNG',
#             'Trh-F-700009.CNG',
#             'Trh-M-000013.CNG',
#             'Trh-M-000146.CNG',
#             'Trh-M-100009.CNG',
#             'Trh-F-000019.CNG',
#             'Trh-M-000081.CNG',
#             'Trh-M-900003.CNG',
#             'Trh-F-200035.CNG',
#             'Trh-F-200015.CNG',
#             'Trh-M-000040.CNG',
#             'Trh-M-600023.CNG',
#             'Trh-M-100048.CNG',
#             'Trh-M-700019.CNG',
#             'Trh-F-100009.CNG',
#             'Trh-M-400000.CNG',
#             'Trh-M-000067.CNG',
#             'Trh-M-000114.CNG',
#             'Trh-M-100018.CNG',
#             'Trh-M-000141.CNG',
#             'Trh-M-900019.CNG',
#             'Trh-M-800002.CNG'
# ]
#
#
# resDir = homeFolder + '/DataAndResults/morphology/UnReg-CentroidMatched/chiangOPSInt/'


# ----------------------------------------------------------------------------------------------------------------------
testPath = homeFolder + '/DataAndResults/morphology/OriginalData/chiangLLC/'
refPath = homeFolder + '/DataAndResults/morphology/Registered/chiangLLC/'
expNames = [
            'Gad1-F-000062.CNG',
            'Cha-F-000012.CNG',
            'Cha-F-300331.CNG',
            'Gad1-F-600000.CNG',
            'Cha-F-000018.CNG',
            'Cha-F-300051.CNG',
            'Cha-F-400051.CNG',
            'Cha-F-200000.CNG'
            ]

resDir = homeFolder + '/DataAndResults/morphology/UnReg-CentroidMatched/chiangLLC/'
# ----------------------------------------------------------------------------------------------------------------------
if not os.path.isdir(resDir):
    os.mkdir(resDir)


for expInd, expName in enumerate(expNames):

    testSWC = os.path.join(testPath, expName + '.swc')
    refSWC = os.path.join(refPath, expName + '.swc')

    testMean = np.loadtxt(testSWC)[:, 2:5].mean(axis=0)
    refMean = np.loadtxt(refSWC)[:, 2:5].mean(axis=0)

    transSWC(testSWC, np.eye(3), refMean - testMean, os.path.join(resDir, expName + '.swc'))

