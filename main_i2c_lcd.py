# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from python_port_apis import date_time_util_functions
from python_port_apis import platform_util_functions

############################################################
# The bellow are local implement python package
# class, etc.
#############################################################
from common_utils import dbg_logging_util
from io_driver_apis import i2c_lcd_api
from python_port_apis.date_time_util_functions import current_time_now


def main():
    cur_platform = platform_util_functions.platform_util()
    if cur_platform.is_platform_pc():
        dbg_log_name = "../dbg_log/dbg{file}log".format(file=__name__).replace("__", "_", -1)
        main_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'main', dbg_log_name)
        sys_platform, sys_version = cur_platform.get_node_sys_info()
        main_logging.dbg_logging('INFO::Python %s on %s' % (sys_version, sys_platform))
    print("Start in python:{version} in {hw_platform}".format( version=cur_platform.get_python_version(), hw_platform=cur_platform.get_cpu_name()))
    # creating thread
    new_date_time = current_time_now()
    date_only = '{0:%Y-%m-%d}'.format(new_date_time)
    time_only = '{:%H:%M:%S}'.format(new_date_time)
    current_date = "Today:{date} Time:{time}".format(date=date_only, time=time_only)
    main_i2c_lcd = i2c_lcd_api.initial_lcd_thread(current_date)
    main_i2c_lcd.lcd_blink_text("Welcome to LCD World!")
    while True:
        pass


if __name__ == '__main__':
    main()
