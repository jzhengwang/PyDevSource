from io_driver_apis import lcd_driver_util
from python_port_apis import platform_util_functions
from python_port_apis.date_time_util_functions import sleep_seconds, current_time_now

cur_platform = platform_util_functions.platform_util()

if cur_platform.is_platform_pc():
    from common_utils import dbg_logging_util


class lcd_device_util:
    def __init__(self, dev_name, logging):
        self.io_name = dev_name
        self.logging = logging
        self.io_device = lcd_driver_util.lcd()

    ###########################
    #   WRITE TO THE DISPLAY  #
    ###########################
    def lcd_display_str(self, str_name, row, col, clr):
        self.io_device.lcd_clear()  # CLEAR THE SCREEN The function mylcd.lcd_clear() clears the screen
        self.io_device.lcd_display_string(str_name, 1)

    ###########################
    #  BLINKING DISPLAY TEXT  #
    ###########################
    def lcd_blink_text(self, dis_str):
        while True:
            self.io_device.lcd_display_string(dis_str)
            sleep_seconds(1)
            self.io_device.lcd_clear()
            sleep_seconds(1)

    ###################################################################
    #                  PRINT THE DATE AND TIME                        #
    ###################################################################
    def lcd_display_time(self):
        self.io_device.lcd_display_string("Time: %s" % ti.strftime("%H:%M:%S"), 1)
        self.io_device.lcd_display_string("Date: %s" % ti.strftime("%m/%d/%Y"), 2)

    def lcd_scroll_text(self, b_continue, b_left2right):
        str_pad = " " * 16
        my_long_string = "This is a string that needs to scroll"
        my_long_string = str_pad + my_long_string

        while b_continue:
            for i in range(0, len(my_long_string)):
                lcd_text = my_long_string[i:(i + 16)]
                self.io_device.lcd_display_string(lcd_text, 1)
                ti.sleep(0.4)
                self.io_device.lcd_display_string(str_pad, 1)

    def lcd_thread(self, arg0, arg1):
        while True:
            sleep_seconds(1)
            new_date_time = current_time_now()
            date_only = '{0:%Y-%m-%d}'.format(new_date_time)
            time_only = '{:%H:%M:%S}'.format(new_date_time)
            current_date = "Today:{date} Time:{time}".format(date=date_only, time=time_only)
            if cur_platform.is_platform_pc():
                self.logging.dbg_logging("INFO::{thread_name}:".format(thread_name=arg1) + current_date)


def initial_lcd_thread(cur_time):
    if cur_platform.is_platform_pc():
        dbg_log_name = "../dbg_log/dbg_{file}log".format(file=__name__)
        lcd_logging = dbg_logging_util.DbgUtilityApi('DEBUG', 'AMC', dbg_log_name)
        lcd_logging.dbg_set_level("DEBUG", 0)
    else:
        lcd_logging = 0
    return lcd_device_util("rock64", lcd_logging)
