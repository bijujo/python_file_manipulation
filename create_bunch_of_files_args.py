#!/bin/env python3
import argparse
import os
parser = argparse.ArgumentParser(description='Create n number of files in specified directory')
parser.add_argument('folder',help='Target folder')
parser.add_argument('prefix',help='File name prefix')
parser.add_argument('ext',help='File extension')
parser.add_argument('num',type=int,help='Number of files to create')
args = parser.parse_args()
# Check if folder exists
if not os.path.exists(args.folder):
  os.makedirs(args.folder)
for i in range(args.num):
  file=open('{0}/{1}{2}.{3}'.format(args.folder, args.prefix, int(i), args.ext), 'w+')
  file.write("Test line")
  file.close()
