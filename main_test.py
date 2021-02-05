# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import threading
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *
import logging

############################################################
# The bellow are local implement python package
# class, etc.
#############################################################
from common_utils import dbg_logging_util
from math_contest_util.amc_contest_main import initial_amc_test_thread
from common_utils.gui_utility_functions import GuiUtility
from common_utils.misc_utility_functions import TerminalFunctionApi
from common_utils.time_update_thread import initial_clock_thread
from test_code_stub.data_types_test_code import print_logo

term_object = TerminalFunctionApi()


def start_up_print ( pos, timeout ):
    tot_run_sec = 0.0
    side_limit = 100
    mov_dir = 1
    while True:
        print_logo(pos, 10)
        ti.sleep(0.5)
        term_object.clear()
        if pos > side_limit:
            mov_dir = -1
        pos += 5 * mov_dir
        if pos < 10:
            mov_dir = 1
        tot_run_sec += 0.5
        if tot_run_sec > timeout:
            break


def main ():
    dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)
    main_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'main', dbg_log_name)
    term_object = TerminalFunctionApi()
    start_up_print(10, 4)
    main_logging.dbg_logging('INFO::Python %s on %s' % (sys.version, sys.platform))
    # creating thread
    new_date_time = datetime.now()
    date_only = '{0:%Y-%m-%d}'.format(new_date_time)
    time_only = '{:%H:%M:%S}'.format(new_date_time)
    current_date = "Today:{date} Time:{time}".format(date=date_only, time=time_only)
    main_open_win = GuiUtility("Welcome", "Arial Bold", 0, 20, 0, "0x0", main_logging)
    main_open_win.open_info_window(current_date, 0)
    amc_test_obj = initial_amc_test_thread()
    clock_thread_obj = initial_clock_thread()
    task_thread = threading.Thread(target=amc_test_obj.amc_contest_thread, args=(0, "AMC-Contest"))
    clock_thread = threading.Thread(target=clock_thread_obj.clock_update_thread, args=(0, "clock_thread"))
    clock_thread.start()
    task_thread.start()
    clock_thread.join()
    task_thread.join()
    while True:
        ti.sleep(1)


if __name__ == '__main__':
    main()
