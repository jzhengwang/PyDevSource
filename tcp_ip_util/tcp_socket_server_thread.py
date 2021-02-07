import sys
import threading
import time as ti  # This to handle the time and datetime cannot used at the same time
from datetime import *
import socket
from python_port_apis import platform_util_functions
cur_platform= platform_util_functions.platform_util()

if cur_platform.is_platform_pc():
    import common_utils.dbg_logging_util as dbg_logging_util


class TcpServerUtil:
    def __init__(self, port, ip_addr, ip_protocol, logging):
        self.ip_addr = ip_addr
        self.svr_port = port
        self.localhost = '127.0.0.1'
        self.logging = logging
        self.ip_proc = ip_protocol
        self.client_rx_th = []
        self.client_tx_th = []

    def tcp_sever_thread(self, svr_name):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as svr_sock:
            svr_sock.bind((self.localhost, self.svr_port))
            svr_sock.listen()
            while True:
                conn, client_ip = svr_sock.accept()
                self.logging.dbg_logging('INFO::Connected by {client}'.format(client=client_ip))
                th_id = threading.Thread(target=self.tcp_server_rx_data_thread, args=(conn, client_ip))
                self.client_rx_th.append(th_id)
                th_id = threading.Thread(target=self.tcp_server_tx_data_thread, args=(conn, client_ip))
                self.client_tx_th.append(th_id)

    def tcp_server_rx_data_thread(self, data_sock, client_ip):
        self.logging.dbg_logging('INFO::Connected by {client}, pending rcv data'.format(client=client_ip))
        with data_sock:
            while True:
                data = data_sock.recv(1024)
                if not data:
                    break
                self.logging.dbg_logging('INFO::Received data from {client}'.format(client=client_ip))

    def tcp_server_tx_data_thread(self, data_sock, client_ip):
        self.logging.dbg_logging('INFO::Connected by {client}, pending rcv data'.format(client=client_ip))
        with data_sock:
            while True:
                data = data_sock.recv(1024)
                if not data:
                    break
                self.logging.dbg_logging('INFO::Received data from {client}'.format(client=client_ip))
