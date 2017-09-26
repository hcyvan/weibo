import logging
from datetime import datetime
from spider import get_one_page_by_order

t = '1'

time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
out_file = './out/fans.order.{}.{}.txt'.format(t, time_str)
log_file = './log/myapp.order.{}.{}.log'.format(t, time_str)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_file, filemode='w')

for page in range(1, 251):
    logging.info('Get Page: {}'.format(page))
    fans = get_one_page_by_order(page, t)
    with open(out_file, 'a') as f:
        for fan in fans:
            info = '-- username: {}, id: {}, fans: {}, follow: {}'.format(fan[3], fan[2], fan[1], fan[0])
            logging.info(info)
            print(info)
            f.writelines('{},{},{},{}\n'.format(fan[2], fan[3], fan[0], fan[1]))
