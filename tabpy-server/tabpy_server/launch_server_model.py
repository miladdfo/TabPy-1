import sys
import subprocess
import os


if sys.platform in ['darwin', 'linux2', 'linux']:
    if len(sys.argv) >= 2:
        subprocess.call(['python', './tabpy.py','--port','9004'])
        subprocess.call(['python', './example.py'])
    else:
        subprocess.call(['python', './tabpy.py','--port','9004'])
        subprocess.call(['python', './example.py'])

else:
    print('Operating system not recognized')

print("I am finished running startup.py!")
