import os
import shutil

for file in os.listdir('downloaded/'):
    os.rename('downloaded/'+file+'/annotations/instances_default.json','downloaded/'+file+'/annotations/'+file+'.json')
    shutil.move('downloaded/'+file+'/annotations/'+file+'.json','cocofiles/')
    
