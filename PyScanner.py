#!/bin/python3

import socket
import sys
import threading
from queue import Queue
from datetime import datetime
import pyfiglet

# Global variables
start_time = datetime.now()


def validate_arguments():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Syntax: python3 PyScanner.py <ip>")
        sys.exit()
    return sys.argv[1]


def get_target_ip(hostname):
    try:
        target_ip = socket.gethostbyname(hostname)
        socket.inet_aton(target_ip)
        return target_ip
    except socket.error:
        print("Invalid IP address")
        sys.exit()


def display_banner(target):
    ascii_art = pyfiglet.figlet_format("PyScanner", font="slant")
    print(ascii_art)
    print("-" * 50)
    print("Scanning target " + target)
    print("Time started: " + str(start_time))
    print("-" * 50)


def port_scan(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")


def threader(target, queue):
    while True:
        port = queue.get()
        port_scan(target, port)
        queue.task_done()


def main():
    hostname = validate_arguments()
    target_ip = get_target_ip(hostname)
    display_banner(target_ip)

    queue = Queue()
    for _ in range(100):
        t = threading.Thread(target=threader, args=(target_ip, queue))
        t.daemon = True
        t.start()

    for port in range(1, 65535):
        queue.put(port)

    queue.join()
    print("Time taken:", datetime.now() - start_time)


if __name__ == "__main__":
    main()
