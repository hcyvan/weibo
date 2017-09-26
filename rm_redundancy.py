from os import listdir
from os import path


def rm_redundancy():
    fans_files = [path.join('./out', f) for f in listdir('./out') if 'fans' in f]
    lines = []
    for fans_file in fans_files:
        with open(fans_file) as f:
            lines.extend(f.readlines())
    lines = sorted(set(lines))
    for line in lines:
        print(line.strip())


def concat():
    fans_files = [path.join('./out', f) for f in listdir('./out') if 'fans.p' in f]
    # print(fans_files)
    for fans_file in fans_files:
        with open(fans_file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    print(line)



def final():
    with open('./out/fans.follow.count.txt') as f:
        infos = f.readlines()

    count_map = [x.strip().split(',') for x in infos]
    # print(count_map)






if __name__ == '__main__':
    # concat()
    final()
