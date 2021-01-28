#####################################################################################################################
# The logging functions are named after the level or severity of the events they are used to track.
#   DEBUG: Detailed information, typically of interest only when diagnosing problems.
#       Sub-Level: 0 ~ 15
#   INFO:  Confirmation that things are working as expected.
#       Sub-Level: 0 ~ 15
#   WARNING: An indication that something unexpected happened or indicative of some problem in the near future
#       (e.g. ‘disk space low’). The software is still working as expected.
#   ERROR: Due to a more serious problem, the software has not been able to perform some function.
#   CRITICAL:A serious error, indicating that the program itself may be unable to continue running.
# This is wrapper layer to handle all the logging from all the modules and threads
#####################################################################################################################

import platform
import os
import logging
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *

dbg_level_numeric = {'NONE': 0, 'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50}
dbg_level_handlers = {
    "NONE": logging.debug,
    "DEBUG": logging.debug,
    "INFO": logging.info,
    "WARNING": logging.warning,
    "ERROR": logging.error,
    "CRITICAL": logging.critical,
}


class DbgUtilityApi:
    def __init__(self, debug_level, debug_title, log_file_name) -> object:
        self.level = debug_level
        self.sub_level = 0
        self.logger = logging.Logger(debug_title)  # debug_title
        self.log_file_str = log_file_name + ".txt"
        self.log_file_log = log_file_name + ".log"
        self.dbg_file_write("logging started !\n", True)

    def dbg_file_write(self, test_str, file_init):
        d_dir = os.path.dirname(self.log_file_str)
        if not os.path.isdir(d_dir):
            os.mkdir(os.path.dirname(self.log_file_str))
        if file_init:
            with open(self.log_file_str, 'w', encoding="utf8") as fulltext:
                fulltext.write(test_str)
        else:
            with open(self.log_file_str, 'a', encoding="utf8") as fulltext:
                fulltext.write(test_str)

    def dbg_set_level(self, level, sub_level):
        self.level = level
        self.sub_level = sub_level

    def get_dbg_level(self):
        level = self.logger.getEffectiveLevel()
        sub_level = self.sub_level
        return level, sub_level

    def dbg_logging(self, message):
        # message : level:msg body:[:parameters] x n
        logging_list = message.split(sep='::', maxsplit=-1)
        num_item = len(logging_list)
        if num_item >= 2:  # the logging
            key_text = logging_list[0]
            dbg_level_handlers[key_text](logging_list[1])
        else:
            call_trace = self.logger.findCaller(stack_info=True, stacklevel=6)
            for str_call in call_trace:
                print(str_call)
            msg_text = call_trace[2]

        new_date_time = datetime.now()
        time_only = '{:%H:%M:%S}'.format(new_date_time)        #date_only = '{0:%Y-%m-%d}'.format(new_date_time)
        msg_text = "[DBG::"+time_only+"]" + ':' + logging_list[num_item-1]+"\n"
        self.dbg_file_write(msg_text, False)
