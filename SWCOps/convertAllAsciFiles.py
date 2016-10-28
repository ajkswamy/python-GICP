import sys
import os
from GICPCore.asciiSWCConverters import ascii2swc

assert len(sys.argv) == 3, 'Two arguments, the path of the swcfile and default Radius expected, ' + str(len(sys.argv)) + 'found'

if os.path.isdir(sys.argv[1]):

    asciiFiles = [x for x in os.listdir(sys.argv[1]) if x.endswith('.ascii')]

    for fle in asciiFiles:
        ascii2swc(os.path.join(sys.argv[1], fle), os.path.join(sys.argv[1], fle[:-6] + '.swc'), float(sys.argv[2]))

if os.path.isfile(sys.argv[1]):

    ascii2swc(sys.argv[1], sys.argv[1][:-6] + '.swc', float(sys.argv[2]))