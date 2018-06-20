#!/bin/env python3
import os
folder = input('Please enter folder: ')
prefix = input('Please enter prefix: ')
ext = input('Please enter extension: ')
num = int(input('Please enter number of files to create: '))

if not os.path.exists(folder):
  os.makedirs(folder)

def filecreate(foldername,prefixname,number,extn):
  fullfilename=('{0}/{1}{2}.{3}'.format(foldername, prefixname, number, extn))
  file=open('{0}/{1}{2}.{3}'.format(foldername, prefixname, number, extn), 'w+')
  file.write("Test line \n")
  file.close()
  print('Print within function. Created file {0}'.format(fullfilename))

for i in range(1,num):
  filecreate(folder, prefix, i, ext)
