#! /usr/bin/python2
from __future__ import print_function

import getpass
import sys

user = getpass.getuser()
password = getpass.win_getpass("Paassword: ")
print(user,password)