

from os import listdir
from os import path

fans_files = [path.join('./out', f) for f in listdir('./out') if 'fans' in f]
lines = []
for fans_file in fans_files:
    with open(fans_file) as f:
        lines.extend(f.readlines())
lines = sorted(set(lines))
for line in lines:
    print(line.strip())