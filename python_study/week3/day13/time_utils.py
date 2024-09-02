import time
from datetime import datetime

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H : %M : %S")


def sleep_for(seconds):
    time.sleep(seconds)

def time_elapsed(start_time):
    return time.time() - start_time