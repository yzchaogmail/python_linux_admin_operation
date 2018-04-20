#! python 2

import os
import sys

def main():

    sys.argv.append("")
    filename = sys.argv[1]
    print(filename)

    if not os.path.isfile(filename):
        raise SystemExit(filename+ ' does not exists [ERROR]')
    elif not os.access(filename,os.R_OK):
        raise SystemExit(filename + ' does not accessable[ERROR]')
    else:
        print(filename + ' is accessable.[FINE]')


if __name__ == '__main__':
    main()

