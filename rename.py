#!/usr/bin/env python3

import os
# import sys
# import re
import shutil
from glob import glob

currentdir = os.path.dirname(os.path.realpath(__file__))
print(currentdir)
destpath = currentdir + "/converted_samples/"
os.makedirs(destpath, exist_ok=True)
dir_path = currentdir + "/samples/"
list = glob(dir_path + '*.wav') # to exclude ._DS_Store
list.sort() 
# print(list)
with open('list_newnames.txt') as file:
    newnames = file.read().splitlines() 

for old, n in zip(list, newnames):
    new = destpath + n + '.wav'
    print(os.path.basename(old) , 'converted to:' , os.path.basename(new))
    shutil.copyfile(old, new )    

exit(0)
