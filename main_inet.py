# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import threading
from python_port_apis import date_time_util_functions
from python_port_apis import platform_util_functions

############################################################
# The bellow are local implement python package
# class, etc.
#############################################################

import tcp_ip_util.tcp_socket_client_thread as tcp_socket_client_thread
import tcp_ip_util.tcp_socket_server_thread as tcp_socket_server_thread
from common_utils import dbg_logging_util
from python_port_apis.date_time_util_functions import current_time_now

cur_platform = platform_util_functions.platform_util()

def main():
    dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)
    main_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'main', dbg_log_name)
    sys_platform, sys_version = cur_platform.get_node_sys_info()
    main_logging.dbg_logging('INFO::Python %s on %s' % (sys_version, sys_platform))
    # creating thread
    new_date_time = current_time_now()
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
        date_time_util_functions.time_util.sleep(5)
        main_logging.dbg_logging("INFO::{name} runs".format(name=__name__))


if __name__ == '__main__':
    main()
