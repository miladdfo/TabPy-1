import sys
import subprocess
import os


if sys.platform == 'win32':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if len(sys.argv) >= 2:
        subprocess.Popen(['startup.bat', sys.argv[1]], cwd=dir_path)
    else:
        subprocess.Popen(['startup.bat'], cwd=dir_path)

elif sys.platform in ['darwin', 'linux2', 'linux']:
    if len(sys.argv) >= 2:
        subprocess.Popen(['sh', './startup.sh', sys.argv[1]])
        subprocess.call(['python', 'prod_fraud_model.py'])
    else:
        subprocess.Popen(['sh', './startup.sh'])
        subprocess.call(['python', 'prod_fraud_model.py'])

else:
    print('Operating system not recognized')

print("I am finished running startup.py!")
