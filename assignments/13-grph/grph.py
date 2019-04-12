#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-11
Purpose: Matchey KMERS!!
"""

import argparse
import sys
import os
import re
from Bio import SeqIO
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='input file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='Number of codons to over lap at begining and end of sequence',
        metavar='int',
        type=int,
        default=3)

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
    k_value = args.overlap
    input_file = args.positional

    if not os.path.isfile(input_file):
        die('"{}" is not a file'.format(input_file))

    if k_value < 1:
        die('-k "{}" must be a positive integer'.format(k_value))
# --------------------------------------------------
if __name__ == '__main__':
    main()
