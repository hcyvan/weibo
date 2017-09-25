import logging
from datetime import datetime
import sys
import os
import time
import random
from spider import get_personal_page_id_by_uid, get_personal_info_by_page_id, get_personal_fans_by_page_id

time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

out_file = './out/fans.p.{}.txt'.format(time_str)
log_file = './log/myapp.p.{}.log'.format(time_str)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_file, filemode='w')

print()

if len(sys.argv) > 1:
    input_file = sys.argv[1]
else:
    input_file = 'fans_id_name.txt'


def get_libang_fans():
    with open('./{}'.format(input_file)) as f:
        fans = f.readlines()
    return [fan.strip().split(',') for fan in fans]


libang_fans = get_libang_fans()


def generate_file_name():
    if not os.path.exists(out_file):
        return out_file
    file_size = os.path.getsize(out_file)
    if file_size > 20000000:
        out_file_name = './out/fans.p.{}.txt'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        return out_file_name
    else:
        return out_file

def info(msg):
    logging.info(msg)
    print(msg)

for libang_fan in libang_fans:
    uid = libang_fan[0]
    nickname = libang_fan[1]
    info('Personal uid: {}, name: {}'.format(uid, nickname))

    with open(out_file, 'a') as f:
        page_id = get_personal_page_id_by_uid(uid)
        info('-- Personal pageId: {}'.format(page_id))
        f.writelines('>>> {}; {}\n'.format(uid, nickname))
        info('---- Get Personal Info')
        f.writelines('>>>>>> Info:\n')
        personal_infos = get_personal_info_by_page_id(page_id)
        for personal_info in personal_infos:
            f.writelines('{} {}\n'.format(personal_info[0], personal_info[1]))

        info('---- Get Personal Fans')
        f.writelines('>>>>>> Fans:\n')
        page = 1
        while True:
            time.sleep(0.5)
            info('------ Personal Fans Page: {}'.format(page))
            fans_in_current_page = get_personal_fans_by_page_id(page_id, page)
            if not fans_in_current_page:
                break
            for fan in fans_in_current_page:
                f.writelines('{},{}\n'.format(fan[0], fan[1]))
            page = page + 1
