#!/usr/bin/python3
"""Reads stdin line and prints log metrics"""
import re
import sys

PATTERN = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] '
    r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total, counts):
    """Prints total file size and per code counts"""
    print("File size: {}".format(total))
    for code in sorted(counts):
        print("{}: {}".format(code, counts[code]))


def main():
    """Reads stdin and computes metrics"""
    total = 0
    counts = {}
    n = 0
    try:
        for line in sys.stdin:
            match = PATTERN.match(line.rstrip('\n'))
            if match is None:
                continue
            code, size = match.groups()
            total += int(size)
            if code in CODES:
                counts[code] = counts.get(code, 0) + 1
            n += 1
            if n % 10 == 0:
                print_stats(total, counts)
    finally:
        print_stats(total, counts)


if __name__ == "__main__":
    main()