#!/usr/bin/python3
"""This module creates a locked class"""


class LockedClass:
    """Locked Class"""
    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object \
has no attribute '{}'".format(attr))
        self.__dict__.update({attr: value})
