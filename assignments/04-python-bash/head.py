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

    if len(args) != 2:
        print('Usage: {} FILE NUMBER'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    LINES = args[1]
    i = 0
    text = open(file)



    for line in text:
        i = (i+1)
        print ('{}: {}'.format(i, line.strip()))

        if i == int(LINES):
            break

    print("Done")


# --------------------------------------------------
main()
