#!/bin/env python3
folder = input('Please enter folder: ')
prefix = input('Please enter prefix: ')
ext = input('Please enter extension: ')
num = int(input('Please enter number of files to create: '))
for i in range(num):
  file=open('{0}/{1}{2}.{3}'.format(folder, prefix, int(i), ext), 'w+')
  file.write("Test line")
  file.close()
