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
import logging
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Files to compare', nargs=2)

    parser.add_argument(
        '-d',
        '--debug',
        help='turns on lowlevel debug statements',
        action='store_true',
        default=False)

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words that should be included',
        metavar='INT',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='max allowed hamming distance for two words to be the same',
        metavar='INT',
        type=int,
        default=False)

    parser.add_argument(
        '-l',
        '--logfile',
        help='the file log statements are printed to',
        action='store_true',
        default='.log')

    parser.add_argument(
        '-t',
        '--table',
        help='converts output to ascii table',
        action='store_true',
        default= False)


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
    file1 = args.positional[0]
    file2 = args.positional[1]
    max_hamm = args.hamming_distance
    min_len = args.min_len
    table = args.table
    

# -----------------------------------------------
if __name__ == '__main__':
    main()
