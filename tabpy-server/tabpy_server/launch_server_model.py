#!/usr/bin/python
import sys
import subprocess
import os

model = "python "+os.path.dirname(os.path.realpath(__file__))+'/example.py'
server = "python "+os.path.dirname(os.path.realpath(__file__))+'/tabpy.py --port 9004'

p = subprocess.Popen(model , shell=True, stdout=subprocess.PIPE)
p = subprocess.Popen(server , shell=True, stdout=subprocess.PIPE)

print("I am finished running startup.py!")
