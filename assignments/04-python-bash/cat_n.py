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

    if not os.biosys-analytics.isfile(args):
        print('{} is not a file'.format(args))

    file = args[0]
    i = 1
    text = open(file)

    for line in text:
        print ('{}: {}'.format(i,  line.strip()))
        i = (i+1)

# --------------------------------------------------
main()
