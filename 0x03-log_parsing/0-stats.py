#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def parse_log_line(log_line):
    '''Extracts sections of a line of an HTTP request log.
    '''
    pattern_parts = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    metrics = {
        'status_code': 0,
        'file_size': 0,
    }
    log_pattern = '{}\\-{}{}{}{}\\s*'.format(pattern_parts[0], pattern_parts[1], pattern_parts[2], pattern_parts[3], pattern_parts[4])
    match_result = re.fullmatch(log_pattern, log_line)
    if match_result is not None:
        status_code = match_result.group('status_code')
        file_size = int(match_result.group('file_size'))
        metrics['status_code'] = status_code
        metrics['file_size'] = file_size
    return metrics


def display_statistics(total_file_size, status_code_counts):
    '''Prints the accumulated statistics of the HTTP request log.
    '''
    print('Total file size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)


def increment_metrics(log_line, total_file_size, status_code_counts):
    '''Updates the metrics from a given HTTP request log.

    Args:
        log_line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    '''
    line_data = parse_log_line(log_line)
    status_code = line_data.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_file_size + line_data['file_size']


def start_log_parser():
    '''Starts the log parser.
    '''
    line_count = 0
    total_file_size = 0
    status_code_counts = {
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
            log_line = input()
            total_file_size = increment_metrics(
                log_line,
                total_file_size,
                status_code_counts,
            )
            line_count += 1
            if line_count % 10 == 0:
                display_statistics(total_file_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        display_statistics(total_file_size, status_code_counts)


if __name__ == '__main__':
    start_log_parser()

