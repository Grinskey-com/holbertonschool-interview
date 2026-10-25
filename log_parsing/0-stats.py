#!/usr/bin/python3
"""Reads stdin line and prints log metrics"""
import sys

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
            parts = line.split()
            if len(parts) < 2:
                continue
            code, size = parts[-2], parts[-1]
            if not size.isdigit():
                continue
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
