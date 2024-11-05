#!/usr/bin/python3
""" UTF-8 validation"""


def validUTF8(data):
    """function that
    determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for num in data:
        if num < 0 or num > 255:
            return False

        if num_bytes == 0:
            if (num >> 7) == 0b0:
                num_bytes = 0
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
