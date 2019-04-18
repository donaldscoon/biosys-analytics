#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-11
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Files to Hamm', nargs=2)

    parser.add_argument(
        '-d',
        '--debug',
        help='turns on lowlevel debug statements',
        metavar='str',
        type=str,
        default=False)


    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

#--------------------------------------------------
def dist(str1, str2):

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    diffs = 0
    for ch1, ch2 in zip(fh1, fh2):
        if ch1 != ch2:
            diffs += 1
    return diffs
# loggin.debug('s1 = {}, s2 = {}, d = {}'.format(a,b, hamm_d))
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1 = args.positional[0]
    file2 = args.positional[1]

    if not os.path.isfile(file1):
        die('"{}" is not a file'.format(file1))
    if not os.path.isfile(file2):
        die('"{}" is not a file'.format(file2))

    fh1 = open(file1)
    fh2 = open(file2)

    for line in fh1:
        for word in line.split():
            print(word)
    for line in fh2:
        for word in line.split():
            print(word)







# --------------------------------------------------
if __name__ == '__main__':
    main()
