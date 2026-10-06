#!/usr/bin/python3
"""defines a function that checks if all boxes can be opened"""

def canUnlockAll(boxes):
    opened = set([0])

    keys = list(boxes[0])

    while keys:
        key = keys.pop(0)
        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
