#!/usr/bin/env python

"""
Copyright (c) 2006-2017 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from main_modules.settings import PRIORITY, TYPE
__classificationtype__=TYPE.BackEND_SPECIFIED
__priority__ = PRIORITY.LOWEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Slash escape quotes (' and ")

    >>> tamper('1" AND SLEEP(5)#')
    '1\\\\" AND SLEEP(5)#'
    """

    return payload.replace("'", "\\'").replace('"', '\\"')