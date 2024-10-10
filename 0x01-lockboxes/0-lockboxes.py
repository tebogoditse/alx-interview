#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    for key in range(1, len(boxes)):
        boxes_checked = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                boxes_checked = True
                break
        if boxes_checked is False:
            return boxes_checked
    return True
