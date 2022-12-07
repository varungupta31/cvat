import os
from tempfile import tempdir

f = open("cvatdumpfeb5later.sh", "w")
f.write("#!/bin/bash\n")


# for i in range(375,396):
#     f.write('python cli.py --auth varungupta:CVIT@varun1605 --server-host 10.2.16.154 dump --format "COCO 1.0" '+str(i)+" downloaded/"+str(i)+'.zip\n')

for i in range(570,662):
	
    f.write('python cli.py --auth varungupta:CVIT@varun1605 --server-host 10.2.16.154 dump --format "COCO 1.0" ' +
            str(i+6)+" downloaded/"+str(i)+'.zip\n')

