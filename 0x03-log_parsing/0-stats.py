#!/usr/bin/python3
"""log parsing"""
import sys
import re

def main():
    """
    Main function to read log lines from standard input and compute metrics.
    
    This function initializes the necessary metrics for tracking the total
    file size and counts of specific HTTP status codes. It processes each 
    line of input, applying a regex pattern to validate and extract data.
    Metrics are printed every 10 lines or after the first line, and also 
    upon keyboard interruption (CTRL + C).
    """
    # Initialize metrics
    total_size = 0
    status_codes_count = {}
    line_count = 0

    # Regex pattern to match the input format
    pattern = re.compile(r'^(?P<ip>[\d\.]+) - \[(?P<date>[^\]]+)\] "(?P<method>GET) (?P<path>[^\s]+) HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)$')

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.strip())

            if match:
                status_code = match.group('status')
                file_size = int(match.group('size'))

                # Update total file size
                total_size += file_size

                # Update status codes count
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1
                else:
                    status_codes_count[status_code] = 1

            # Print metrics after every 10 lines or if it's the last line
            if line_count % 10 == 0 or line_count == 1:
                print_metrics(total_size, status_codes_count)

    except KeyboardInterrupt:
        # Print metrics on keyboard interrupt
        print_metrics(total_size, status_codes_count)

def print_metrics(total_size, status_codes_count):
    """
    Print the accumulated metrics of file sizes and status code counts.

    Args:
        total_size (int): The total size of all files processed.
        status_codes_count (dict): A dictionary containing counts of each
                                    HTTP status code.
    
    This function outputs the total file size and the counts of HTTP 
    status codes in ascending order.
    """
    print(f'Total file size: {total_size}')
    
    # Sorted status codes to print in ascending order
    for code in sorted(status_codes_count.keys()):
        print(f'{code}: {status_codes_count[code]}')

if __name__ == "__main__":
    main()
