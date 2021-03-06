import logging
from datetime import datetime
from spider import search_users_by_char

time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
out_file = './out/fans.{}.txt'.format(time_str)
log_file = './log/myapp.{}.log'.format(time_str)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=log_file, filemode='w')


def get_chars():
    with open('./charLib.txt') as f:
        return f.read()


chars = get_chars()

for char in chars:
    logging.info('Get char: {}'.format(char))
    fans = search_users_by_char(char)
    with open(out_file, 'a') as f:
        for fan in fans:
            info = '-- username: {}, id: {}'.format(fan[1], fan[0])
            logging.info(info)
            print(info)
            f.writelines('{},{}\n'.format(fan[0], fan[1]))

if __name__ == '__main__':
    get_chars()
