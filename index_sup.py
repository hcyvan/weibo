import logging
import time
from datetime import datetime
from spider import get_personal_page_info_by_uid

time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
out_file = './out/sup.{}.txt'.format(time_str)
log_file = './log/sup.{}.log'.format(time_str)
input_file = './tonavy.txt'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_file, filemode='w')


def get_sups():
    with open('./{}'.format(input_file)) as f:
        fans = f.readlines()
    return [fan.strip().split(',')[0] for fan in fans]


sups = get_sups()

i = 1
for uid in sups:
    time.sleep(6)
    info = '{}. Get uid: {}'.format(i, uid)
    logging.info(info)
    print(info)
    final = get_personal_page_info_by_uid(uid)
    with open(out_file, 'a') as f:
        f.writelines('{}<|>{}\n'.format(uid, final))
    i = i + 1
