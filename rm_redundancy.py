with open('./fans.2017-09-24_12-22-47.txt') as f:
    lines = f.readlines()

for line in set(lines):
    print(line.strip())
