# -*- utf8 -*-
#! python2
from __future__ import print_function
import os
import sys

'''
for line in sys.stdin:
    print (line, end= "")
    #print (line)
'''
def getcontent():
    return sys.stdin.readlines()

if __name__ == '__main__':
    print(getcontent())
