import os

keep = set()

with open('./removeImages.txt') as f:
     for line in f:
         keep.add(line.strip())

for f in os.listdir('.'):
    if f not in keep:
        print('unlink: ' + f ) 
        os.unlink(f)