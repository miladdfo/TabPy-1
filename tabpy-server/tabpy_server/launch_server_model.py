#!/usr/bin/python
import sys
import subprocess
import os


if sys.platform in ['darwin', 'linux2', 'linux']:
    subprocess.call(['python', os.path.dirname(os.path.realpath(__file__))+'/example.py'])
    subprocess.call(['python', os.path.dirname(os.path.realpath(__file__))+'/tabpy.py','--port','9004'])
else:
    print('Operating system not recognized')

print("I am finished running startup.py!")
