#! python 2

import os
import sys

def main():

    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' is NOT a file [ERROR]')
    elif not os.access(filename,os.R_OK):
        raise SystemExit(filename + ' is NOT accessable[ERROR]')
    else:
        print (filename + 'is accessable [OK]')


if __name__ == '__main__':
    main()