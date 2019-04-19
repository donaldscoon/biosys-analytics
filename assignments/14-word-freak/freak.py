#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from collections import Counter



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='A positional argument', nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Switches sort to numerically in ascending order',
        default=False)

    parser.add_argument(
        '-m',
        '--min',
        help='minimum number of times a word must occur',
        metavar='int',
        type=int,
        default=0)

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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional

    for item in files:
        print(item)
        if not os.path.isfile(item):
            die('"{}" is not a file'.format(item))
        with open(item) as fh:
            for line in fh:
                for word in line.split():
                    word = (re.sub('[^a-zA-Z0-9]', '', word.lower()))
                    print(word)








# --------------------------------------------------
if __name__ == '__main__':
    main()
