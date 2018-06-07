# This small script will batch copy the INPUT folder to OUTPUT folder with preseserved file structure
# Delays:   0,5 s per file
#           60 s per 100 files
# Licence: MIT

import os
import shutil
import time

TESTMODE = 1
INPUT   = 'input/'
OUTPUT  = 'output/'
COUNTER = 0 

for dirpath, dirnames, filenames in os.walk(INPUT):
    structure = os.path.join(OUTPUT, dirpath[len(INPUT):])
    print ("Copying directory: " + structure)
    if not os.path.isdir(structure):
        if not TESTMODE:
            os.mkdir(structure)
        else:
            print ('TEST - Create folder: ' + structure)
    for file in filenames:
        sourcefile=os.path.join(dirpath, file)
        targetfile=os.path.join(structure, file)
        if not TESTMODE:
            shutil.copy2(sourcefile, targetfile)
        else:
            print ('TEST - SOURCEFILE: ' + sourcefile)
            print ('TEST - TARGETFILE: ' + targetfile)
        time.sleep(0.5)
        COUNTER = COUNTER + 1
        if (COUNTER % 100) == 0:
            print ("Waiting")
            if not TESTMODE:
                time.sleep(60)
