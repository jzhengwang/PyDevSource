import sys
import threading
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *

import CommonUtils.dbg_logging_util as dbg_logging_util


class ClockThreadUtil:
    def __init__ ( self, logging_util ):
        self.logging = logging_util
        self.curTime = datetime.now()

    def clock_update_thread ( self, arg0, arg1 ):
        while True:
            ti.sleep(1)
            new_date_time = datetime.now()
            date_only = '{0:%Y-%m-%d}'.format(new_date_time)
            time_only = '{:%H:%M:%S}'.format(new_date_time)
            current_date = "Today:{date} Time:{time}".format(date=date_only, time=time_only)
            self.logging.dbg_logging("INFO::{thread_name}:".format(thread_name=arg1) + current_date)


def initial_clock_thread ():
    dbg_log_name = "../dbg_log/dbg_{file}log".format(file=__name__)
    clock_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'clockThread', dbg_log_name)
    clock_logging.dbg_set_level("DEBUG", 0)
    clock_th_obj = ClockThreadUtil(clock_logging)
    return clock_th_obj
