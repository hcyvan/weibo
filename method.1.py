import time
import random

work_seed=4
stop_seed=4

def get_interval(seed):
    return seed+int(random.uniform(0,seed))

start_time=time.time()
work_time=get_interval(work_seed)
print('working for {}'.format(work_time))
while True:
    real_work_time = time.time() - start_time

    if work_time < real_work_time:
        sleep_time=get_interval(stop_seed)
        print('sleeping for {}'.format(sleep_time))
        time.sleep(sleep_time)
        start_time = time.time()

        work_time=get_interval(work_seed)
        print('working for {}'.format(work_time))


    # print('working...{}'.format(time.time()))
