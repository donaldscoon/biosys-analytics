#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-08
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0 :
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    filename = args[0]

    if not os.path.isfile(filename):
        print ('{} is not a file'.format(filename), file=sys.stderr)
        sys.exit(1)

    if not 0 < int(args[1]) > 1:
        print('lines ({}) must be a positive number'.format(args[1]))
        sys.exit(1)



    LINES = args[1]
    i = 0
    text = open(filename)

    for line in text:
        i = (i+1)
        print ('{}: {}'.format(i, line.strip()))

        if i == int(LINES):
            break


# --------------------------------------------------
main()
