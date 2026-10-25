#!/usr/bin/python3
"""Reads log lines from stdin and prints stats"""
import re
import sys

PATTERN = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] '
    r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)$')
CODES = ['200', '301', '400', '401', '403', '404', '405', '500']


def print_stats(total, counts):
    """Prints the total size and the count for each status code"""
    print("File size: {}".format(total))
    for code in sorted(counts):
        print("{}: {}".format(code, counts[code]))


def main():
    """Reads stdin and keeps track of stats"""
    total = 0
    counts = {}
    n = 0
    try:
        for line in sys.stdin:
            match = PATTERN.match(line.rstrip())
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