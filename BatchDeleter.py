#This code imports the necessary modules

import os
import re
import collections
import operator
 
for subdir, dirs, files in os.walk('C:\\Users\\mysti\\Coding\\BFFMaker\\Audio'):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".mp3")) or (filepath.endswith(".sfk")) or (('8000' in filepath) and ('Audio' in filepath)):
            os. remove(filepath) 

print("")

print("The designated files have been removed. Thank you.")

print("")