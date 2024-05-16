#!/usr/bin/python3
""" Processes stdin for having http request format"""
import sys
import signal

total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """ Logs the statistics to stdout"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """handles interupts"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 9:
            continue
        ip = parts[0]
        date = parts[3][1:] + " " + parts[4][:-1]
        method = parts[5][1:]
        resource = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[8])
        file_size = int(parts[9])
        
        if method != "GET" or protocol != "HTTP/1.1":
            continue

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

    except Exception as e:
        continue

print_stats()
