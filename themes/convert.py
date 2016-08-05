#!/usr/bin/python

import sys
import os

with open(sys.argv[1]) as f:
  lines = f.readlines()

for line in lines:
  print line.strip()



