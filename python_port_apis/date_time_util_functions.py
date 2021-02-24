import time as ti  # This to handle the time and datetime cannot used at the same time


def sleep_seconds(seconds):
    ti.sleep(seconds)


def time_string(str):
    return ti.strftime(str)


def epoch_seconds():
    return int(ti.time())


def seconds_of_Day():
    seconds_day = epoch_seconds()
    seconds_day %= 86400
    return seconds_day


from datetime import *


def current_time():
    return datetime.time()


def today_date():
    return datetime.date_time()


def today_of_week():
    return datetime.day


def date_time():
    return datetime.today()


def current_time_now():
    return datetime.now()
