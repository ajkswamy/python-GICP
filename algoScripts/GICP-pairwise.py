import os
from GICPCore.gicpWrapper import runGICP


homeFolder = os.path.expanduser('~')

# ----------------------------------------------------------------------------------------------------------------------
# testPath = homeFolder + '/DataAndResults/morphology/OriginalData/chiangOPSInt/'
testPath = homeFolder + '/DataAndResults/morphology/UnReg-CentroidMatched/chiangOPSInt/'
refPath = homeFolder + '/DataAndResults/morphology/Registered/chiangOPSInt/'
expNames = [
            'Trh-F-000047.CNG',
            # 'Trh-M-000143.CNG',
            # 'Trh-F-000092.CNG',
            # 'Trh-F-700009.CNG',
            # 'Trh-M-000013.CNG',
            # 'Trh-M-000146.CNG',
            # 'Trh-M-100009.CNG',
            # 'Trh-F-000019.CNG',
            # 'Trh-M-000081.CNG',
            # 'Trh-M-900003.CNG',
            # 'Trh-F-200035.CNG',
            # 'Trh-F-200015.CNG',
            # 'Trh-M-000040.CNG',
            # 'Trh-M-600023.CNG',
            # 'Trh-M-100048.CNG',
            # 'Trh-M-700019.CNG',
            # 'Trh-F-100009.CNG',
            # 'Trh-M-400000.CNG',
            # 'Trh-M-000067.CNG',
            # 'Trh-M-000114.CNG',
            # 'Trh-M-100018.CNG',
            # 'Trh-M-000141.CNG',
            # 'Trh-M-900019.CNG',
            # 'Trh-M-800002.CNG'
]


resDir = homeFolder + '/DataAndResults/morphology/UnRegReg-GICP/chiangOPSInt/'
if not os.path.isdir(resDir):
    os.mkdir(resDir)
# ----------------------------------------------------------------------------------------------------------------------


for expInd, expName in enumerate(expNames):
    print('Doing ' + expName)
    refSWC = os.path.join(refPath, expName + '.swc')

    SWC2Align = os.path.join(testPath, expName + '.swc')

    runGICP(refSWC, SWC2Align, os.path.join(resDir, expName + '.swc'))



