#!/usr/bin/python3
"""LOG PARSING"""
import sys


def print_stats(status_codes, file_size):
    """Method that prints the statistics"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
