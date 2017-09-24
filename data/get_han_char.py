file_name = 'kMandarin_8105.txt'
string=''
with open(file_name) as f:
    for line in f.readlines():
        if '#' == line[0]:
            continue
        chars = line.split()
        string += chars[3]

print(string)