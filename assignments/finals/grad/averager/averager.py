#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-11
Purpose: A program for the peasentry.
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
        'positional', metavar='FILE', help='Files to compare', nargs='+')

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

    for name in files:
        if not os.path.isfile(name):
            warn('"{}" is not a file'.format(name))
            break
        with open(name) as fh:
            for line in fh:
                

# -----------------------------------------------
if __name__ == '__main__':
    main()