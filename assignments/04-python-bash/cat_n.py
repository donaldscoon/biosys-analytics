#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-08
Purpose: replicate cat in python
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: cat_n.py FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    filename = args[0]

    if not os.path.isfile(filename):
        print ('{} is not a file'.format(filename), file=sys.stderr)
        sys.exit(1)

    i = 1
    text = open(filename)

    for line in text:
        print ('{:3}: {}'.format(i,  line.strip()))
        i = (i+1)

# --------------------------------------------------
main()
