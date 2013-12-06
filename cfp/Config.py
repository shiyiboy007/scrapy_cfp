#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Manage configuration ini files and cmd line args"""

# Import from the standard library
import os
import sys
from ConfigParser import RawConfigParser

CONF_FILES = ["query.ini"]


def check():
    "Check that we are in a project"
    # check that that we are in a crawling project
    for filename in CONF_FILES:
        msg = ("\n  You're not in a crawling project {} file is missing\n"
               "  Please initialize a project first\n")
        if not os.path.isfile(filename):
            print msg.format(filename)
            sys.exit()


class Config(object):
    """ Load ini files and store arguments info"""

    def __init__(self):
        self.query = None
        self.argline = None
        check()
        self.load()

    def load(self):
        "Load ini files"
        self.query = RawConfigParser()
        self.argline = RawConfigParser()

        self.argline.add_section('argline')

        queryfilename = CONF_FILES
        self.query.read(queryfilename)
