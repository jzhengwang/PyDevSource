# https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

import sys
import threading
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *
import socket

import common_utils.dbg_logging_util as dbg_logging_util


class TcpClientUtil:
    def __init__(self, port, ip_address, ip_protocol, cli_alias, logging):
        self.ip_address = ip_address
        self.svs_port = port
        self.localhost = '127.0.0.1'
        self.logging = logging
        self.ip_proc = ip_protocol
        self.client_rx_th = []
        self.cli_name = ip_address + ':' + str(port)
        self.alias = cli_alias

    def tcp_client_thread(self, cli_alias):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli_sock:
            cli_sock.connect((self.ip_address, self.svs_port))
            self.logging.dbg_logging(
                'INFO:: {client_name} Connect to {server}'.format(client_name=cli_alias, server=self.cli_name))
            th_id = threading.Thread(target=self.tcp_client_rx_data_thread, args=(cli_sock, self.cli_name))
            self.client_rx_th.append(th_id)
        while True:
            ti.sleep(1)

    def tcp_client_rx_data_thread(self, cli_sock, svr_name):
        with cli_sock:
            while True:
                data = cli_sock.recv(1024)
                if not data:
                    break
                self.logging.dbg_logging('INFO::Received data from {server}'.format(server=svr_name))

    def tcp_send_data_packet_api(self, data):
        self.logging.dbg_logging('INFO::App sending data to {server}'.format(server=self.ip_address))
