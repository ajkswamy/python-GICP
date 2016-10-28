import sys
import os
homeFolder = os.path.expanduser('~')
sys.path.append(homeFolder + '/repos/BlenderSWCVizualizer')
import numpy as np
from blenderHelper import BlenderSWCImporter

# ----------------------------------------------------------------------------------------------------------------------

dirPath = os.path.join(homeFolder, 'DataAndResults', 'morphology', 'OriginalData', 'GICP_tests', 'car')

expNames = [
            'car0',
            'car1',
            'car2',
            'car3',
            'car4',
            'car5',
            ]

resDir1 = os.path.join(homeFolder, 'DataAndResults', 'morphology', 'GICP', 'GICP_tests', 'car')
resDir2 = os.path.join(homeFolder, 'DataAndResults', 'morphology', 'directPixelBased', 'GICP_tests', 'car')

# ----------------------------------------------------------------------------------------------------------------------
# dirPath = os.path.join(homeFolder, 'DataAndResults', 'morphology', 'OriginalData', 'GICP_tests', 'outdoor')
#
# expNames = ['outdoor14[300x541]',
#             'outdoor1[300x541]',
#             'outdoor3[300x541]',
#             'outdoor2[300x541]',
#             # 'outdoor9[300x541]',
#             # 'outdoor5[300x541]',
#             # 'outdoor6[300x541]',
#             # 'outdoor13[300x541]',
#             # 'outdoor11[300x541]',
#             # 'outdoor0[300x541]',
#             # 'outdoor4[300x541]',
#             # 'outdoor7[300x541]',
#             # 'outdoor15[300x541]',
#             # 'outdoor8[300x541]',
#             # 'outdoor10[300x541]',
#             # 'outdoor12[300x541]'
#             ]
#
#
# resDir = os.path.join(homeFolder, 'DataAndResults', 'morphology', 'directPixelBased', 'GICP_tests', 'outdoor')
# ----------------------------------------------------------------------------------------------------------------------

refF = lambda dirPath, fName, resDir: os.path.join(dirPath, fName + '.swc')
finalRefF = lambda resDir: os.path.join(resDir, 'finalRef.swc')
origF = lambda dirPath, fName, resDir: os.path.join(dirPath, fName + '.swc')
origFPart = lambda dirPath, fName, part: os.path.join(dirPath, fName, fName[:-11] + part + fName[-9:] + '.swc')
regF = lambda dirPath, fName, resDir: os.path.join(resDir, fName + '.swc')
regFNorm = lambda dirPath, fName, resDir: os.path.join(resDir, fName + '_norm.swc')
regFNormNorm = lambda dirPath, fName, resDir: os.path.join(resDir, fName + '_norm_norm.swc')
regABF = lambda A, B, resDir: os.path.join(resDir, A + '-' + B + '.swc')
startPt = lambda dirPath, fName, resDir: os.path.join(resDir, fName + 'trans', '0.swc')
startPtAB = lambda A, B, resDir: os.path.join(resDir, A + '-' + B + 'trans', '0.swc')
intermediateF = lambda itert, fName, resDir: os.path.join(resDir, fName + 'trans', itert + '.swc')
intermediateFIt = lambda itert, fName, resDir, iterNo: os.path.join(resDir, fName + str(iterNo)
                                                                    + 'trans', itert + '.swc')
regPart = lambda fName, resDir, part: os.path.join(resDir, fName, fName + part + '.swc')
regPartNorm = lambda fName, resDir, part: os.path.join(resDir, fName + '_norm', fName + part + '_norm.swc')
regPartNormNorm = lambda fName, resDir, part: os.path.join(resDir, fName + '_norm_norm',
                                                           fName + part + '_norm_norm.swc')
regIt = lambda resDir, expName, iterNo: os.path.join(resDir, expName + str(iterNo) + '.swc')
regItPart = lambda resDir, expName, iterNo, part: os.path.join(resDir, expName + str(iterNo),
                                                               expName + part + '.swc')
refIt = lambda resDir, iterNo: os.path.join(resDir, 'ref' + str(iterNo) + '.swc')
refdensity = lambda resDir, expName: os.path.join(resDir, 'DensityResults', expName + '_density.sswc')
refDiffDensity = lambda resDir, expName: os.path.join(resDir, 'DensityDiffResults', expName + '_density.sswc')
refDiffDensityPart = lambda resDir, expName, part: os.path.join(resDir, 'DensityDiffResults', expName + part + '_density.sswc')

swcs = []
# swcs.append(refF(dirPath, expNames[refInd], resDir))

iterNo = 3

# swcs.append(refIt(resDir, 0))
# swcs.append(refIt(resDir, 1))
# swcs.append(refIt(resDir, 2))
# swcs.append(refIt(resDir, iterNo - 1))
# swcs.append(refIt(resDir, iterNo))


# swcs.append(finalRefF(resDir))

# expNames = expNames[:5]

for expInd, expName in enumerate(expNames):

    swcs.append(origF(dirPath, expName, None))
    # swcs.append(origF(dirPath1, expName, resDir))
    # swcs.append(regPart(expName, dirPath, '_part0'))
    # swcs.append(regPart(expName, dirPath, '_part1'))
    # swcs.append(origFPart(dirPath, expName, 'DB'))
    # swcs.append(origFPart(dirPath, expName, 'VB'))
    # swcs.append(origFPart(dirPath, expName, 'MB'))
    # swcs.append(regIt(resDir, expName, iterNo - 1))
    # swcs.append(regIt(resDir, expName, iterNo))
    # swcs.append(regItPart(resDir, expName, iterNo, '_part0'))
    # swcs.append(regItPart(resDir, expName, iterNo, '_part1'))
    # swcs.append(intermediateFIt('0', expName, resDir, iterNo))
    # swcs.append(regF(None, expName, resDir))
    swcs.append(regF(None, expName, resDir1))
    swcs.append(regF(None, expName, resDir2))
    # swcs.append(regPart(expName, resDir, '_part0'))
    # swcs.append(regPart(expName, resDir, '_part1'))
    # swcs.append(regFNorm(None, expName, resDir))
    # swcs.append(regFNormNorm(None, expName, resDir))
    # swcs.append(regPartNorm(expName, resDir, '_part1'))
    # swcs.append(regPartNormNorm(expName, resDir, '-VB'))
    # swcs.append(regPartNormNorm(expName, resDir, '-DB'))
    # swcs.append(refdensity(resDir, expName))
    # swcs.append(refDiffDensityPart(resDir, expName, '_part1'))

    # swcs.append(origF(testPath, expName, resDir))
    # swcs.append(refF(refPath, expName, resDir))
    # swcs.append(startPt(None, expName, resDir))

    # if expInd != refInd:
    # # if True:
    #
        # swcs.append(origF(dirPath, expName, resDir))
        # swcs.append(regABF(expName, expNames[refInd], resDir))
    #     # swcs.append(startPtAB(expName, expNames[refInd], resDir))
    #     swcs.append(regF(dirPath, expName, resDir))
    #     swcs.append(startPt(dirPath, expName, resDir))

    #     # swcs.append(intermediateF('0', expName, resDir))
    #     swcs.append(intermediateF('1r', expName, resDir))
        # swcs.append(intermediateF('4r', expName, resDir))


    # swcs.append(os.path.join(resDir, expName + 'trans', 'poss0.swc'))
    # swcs.append(os.path.join(resDir, expName + 'trans', 'poss1.swc'))
    # swcs.append(os.path.join(resDir, expName + 'trans', 'poss1.swc'))
    # swcs.append(os.path.join(resDir, expName + 'trans', 'poss2.swc'))

# ----------------------------------------------------------------------------------------------------------------------
# cols = [[ 0.        ,  0.        ,  0.5       ],
#         [ 0.        ,  0.00196078,  1.        ],
#         [ 0.        ,  0.50392157,  1.        ],
#         [ 0.08538899,  1.        ,  0.88235294],
#         [ 0.49019608,  1.        ,  0.47754586],
#         [ 0.89500316,  1.        ,  0.07273877],
#         [ 1.        ,  0.58169935,  0.        ],
#         [ 1.        ,  0.11692084,  0.        ]]

# these values correspond to red, green, blue, magenta, cyan and light green
# baseCols = np.array(
#                     [[1, 0, 0],
#                     [0, 1, 0],
#                     [0, 0, 1],
#                     # [0.5, 0, 0.5],
#                     # [0, 0.5, 0.5],
#                     # [0.5, 0.5, 0]
#                   ]
#                     )
#
# baseCols = np.concatenate([baseCols] * 6)

# baseCols = np.array([[0, 0, 1], [1, 0, 0]])

# baseCols = np.array([[ 1.        ,  0.58169935,  0.        ]])

# cols = np.array([[27, 158, 119], [231, 41, 138]]) / 256.

# r = [1, 0, 0]
# b = [0, 0, 1]
#
# cols = [r, r, r, b, r, r, r, r, r, r, b, r, r, r, r]



# cols = [[0, 0.2, 0.2], [0.1, 0, 0.1]]

baseCols = np.asarray(   [[1.0, 0.11692084, 0.0],
                         [1.0, 0.58169935, 0.0],
                         [0.89500316, 1.0, 0.07273877],
                         [0.49019608, 1.0, 0.47754586],
                         [0.08538899, 1.0, 0.88235294],
                         [0.0, 0.50392157, 1.0],
                         [1.0, 0.11692084, 0.0],
                         [0.0, 0.0, 0.5]] )





nPts = baseCols.shape[0]
nSWC = len(swcs)

if nPts == nSWC:
    cols = baseCols
else:
    cols = np.zeros([nSWC, 3])


    for ind in range(3):
        cols[:, ind] = np.interp(np.linspace(0, nPts, nSWC), range(nPts), baseCols[:, ind])

# cols = [[1, 0, 0]] * len(fExpNames) + [[0, 0, 1]] * len(nExpNames)
alphas = [1] * len(swcs)


# ----------------------------------------------------------------------------------------------------------------------
nPts = 8

# density value of 0 indicates newlyEmergedDensity-foragerDensity=1
# SbaseCols = np.array([ [ 0.78235294,  0.        ,  0.        ,  1.        ],
#                        [ 1.        ,  0.14509804,  0.14509804,  1.        ],
#                        [ 1.        ,  0.70980392,  0.70980392,  1.        ],
#                        [ 1.        ,  1.        ,  1.        ,  0.5       ],
#                        [ 1.        ,  1.        ,  1.        ,  0.5       ],
#                        [ 0.70980392,  0.70980392,  1.        ,  1.        ],
#                        [ 0.14509804,  0.14509804,  1.        ,  1.        ],
#                        [ 0.        ,  0.        ,  0.69529412,  1.        ]])

SbaseCols = np.array([[0.78235294, 0., 0., 1.],
                      [1., 1., 1., 0.5],
                      [1., 1., 1., 0.5],
                      [1., 1., 1., 0.5],
                      [1., 1., 1., 0.5],
                      [1., 1., 1., 0.5],
                      [1., 1., 1., 0.5],
                      [0., 0., 0.69529412, 1.]])
# ----------------------------------------------------------------------------------------------------------------------


if nPts % len(SbaseCols) > 0:
    raise(ValueError('nPts must be a integral multiple of ' + str(len(SbaseCols))))

Scols = np.zeros([nPts, 3])
scaleFactor = int(nPts / len(SbaseCols))

for ind in range(3):
    Scols[:, ind] = np.interp(range(nPts), range(0, nPts, scaleFactor), SbaseCols[:, ind])

# ----------------------------------------------------------------------------------------------------------------------
nrnsBlender = []
matchOrigin = False
scaleDownBy = 1
restrictRadiusTo = 0

for nrnInd, nrn in enumerate(swcs):

    if nrnInd == 0:
        add = False
    else:
        add = True

    # tmpB = BlenderSWCImporter(nrn, add, matchOrigin, colMap=cols)
    # tmpB.importWholeSWC()

    # matchOrigin = True

    tmpB = BlenderSWCImporter(os.path.abspath(nrn), add, matchOrigin, colMap=Scols,
                              scaleDownBy=scaleDownBy, restrictRadiusTo=restrictRadiusTo)
    tmpB.importWholeSWC(col=cols[nrnInd])

    nrnsBlender.append(tmpB)


# tmpB.addSphere(position=[0, 0, 0], col=[1, 0, 0], radius=2)
