#!/usr/bin/env python3

import sys
import subprocess

filepath = sys.argv[1]
with open(filepath) as f:
    for line in f:
        fileName = line.strip().split()[2].split("/")[2]
        newFileName = fileName.replace('jane', 'jdoe')
        subprocess.run(["mv", "/home/student-02-5a989588ce94/data/{}".format(fileName), "/home/student-02-5a989588ce94/data/{}".format(newFileName)])
