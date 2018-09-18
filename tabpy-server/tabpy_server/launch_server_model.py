#!/usr/bin/python
import sys
import subprocess
import os

print (os.path.abspath(os.path.join(yourpath, os.pardir)))

if sys.platform in ['darwin', 'linux2', 'linux']:
    if len(sys.argv) >= 2:
        subprocess.call(['python', os.path.abspath(os.path.join(yourpath, os.pardir))+'/tabpy.py','--port','9004'])
        subprocess.call(['python', os.path.abspath(os.path.join(yourpath, os.pardir))+'/example.py'])
    else:
        subprocess.call(['python', os.path.abspath(os.path.join(yourpath, os.pardir))+'/tabpy.py','--port','9004'])
        subprocess.call(['python', os.path.abspath(os.path.join(yourpath, os.pardir))+'/example.py'])

else:
    print('Operating system not recognized')

print("I am finished running startup.py!")
