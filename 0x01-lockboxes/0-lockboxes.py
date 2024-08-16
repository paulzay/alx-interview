#!/usr/bin/python3
"""LOCKBOXES"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    if type(boxes) is not list:
        return False
    if boxes == []:
        return False
    if len(boxes) == 0:
        return False
