# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import threading
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *

############################################################
# The bellow are local implement python package
# class, etc.
#############################################################

import common_utils.time_update_thread as time_update_thread
import tcp_ip_util.tcp_socket_client_thread as tcp_socket_client_thread
import tcp_ip_util.tcp_socket_server_thread as tcp_socket_server_thread
from common_utils import dbg_logging_util


def main():
    dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)
    main_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'main', dbg_log_name)
    main_logging.dbg_logging('INFO::Python %s on %s' % (sys.version, sys.platform))
    # creating thread
    new_date_time = datetime.now()
    date_only = '{0:%Y-%m-%d}'.format(new_date_time)
    time_only = '{:%H:%M:%S}'.format(new_date_time)
    current_date = "Today:{date} Time:{time}".format(date=date_only, time=time_only)
    tcp_server_obj = tcp_socket_server_thread.TcpServerUtil(6553, '127.0.0.1', 'IPV4', main_logging)
    tcp_client_obj = tcp_socket_client_thread.TcpClientUtil(6553, '127.0.0.1', 'IPV4', 'test_client', main_logging)
    tcp_sever_thread = threading.Thread(target=tcp_server_obj.tcp_sever_thread, args=("TcpSever",))
    tcp_client_thread = threading.Thread(target=tcp_client_obj.tcp_client_thread, args=("TcpClient",))
    tcp_sever_thread.start()
    tcp_client_thread.start()
    tcp_sever_thread.join()
    tcp_client_thread.join()
    while True:
        ti.sleep(5)
        main_logging.dbg_logging("INFO::{name} runs".format(name=__name__))


if __name__ == '__main__':
    main()
