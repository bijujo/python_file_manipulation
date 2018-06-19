#!/bin/env python3
#Rename files in /home/ec2-user/testdir
import os
from pathlib import Path
directory='/tmp'
for filename in os.listdir(path=directory):
#for filename in os.listdir(path='.'):
  if filename.endswith('.txt'):
     name=Path(filename).stem
     ext='csv'
     newname=str.join('.',(name,ext))
     print('Renaming {0} to {1}.{2}' .format(filename,name,ext))
     os.rename(os.path.join(directory,filename), os.path.join(directory,newname))
