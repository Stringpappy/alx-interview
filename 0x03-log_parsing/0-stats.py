#!/usr/bin/python3
'''Script to parse HTTP request logs.'''
import re


def parse_log_line(line):
    '''Extracts details from a log line.'''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    match = re.fullmatch(log_fmt, line)
    if match is not None:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info


def display_stats(total_size, status_counts):
    '''Prints the log statistics.'''
    print('File size: {:d}'.format(total_size), flush=True)
    for code in sorted(status_counts.keys()):
        count = status_counts.get(code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(code, count), flush=True)


def update_stats(line, total_size, status_counts):
    '''Updates stats from a log line.'''
    line_info = parse_log_line(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_counts.keys():
        status_counts[status_code] += 1
    return total_size + line_info['file_size']


def main():
    '''Runs the log parser.'''
    line_num = 0
    total_size = 0
    status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_size = update_stats(line, total_size, status_counts)
            line_num += 1
            if line_num % 10 == 0:
                display_stats(total_size, status_counts)
    except (KeyboardInterrupt, EOFError):
        display_stats(total_size, status_counts)


if __name__ == '__main__':
    main()

