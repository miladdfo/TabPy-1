#!/usr/bin/python
import sys
import subprocess
import os

print os.path.realpath(__file__)

if sys.platform in ['darwin', 'linux2', 'linux']:
    if len(sys.argv) >= 2:
        subprocess.call(['python', os.path.realpath(__file__)+'/tabpy.py','--port','9004'])
        subprocess.call(['python', os.path.realpath(__file__)+'/example.py'])
    else:
        subprocess.call(['python', './tabpy.py','--port','9004'])
        subprocess.call(['python', './example.py'])

else:
    print('Operating system not recognized')

print("I am finished running startup.py!")
