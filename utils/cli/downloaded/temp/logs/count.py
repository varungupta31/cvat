import os
import glob

files = sorted(glob.glob("*.txt"),reverse=True)

for file in files:
    with open(file,'r') as fin:
        with open("out.txt",'a') as fout:
            lines = len(fin.readlines())
            fout.write(str(lines)+"\n")
