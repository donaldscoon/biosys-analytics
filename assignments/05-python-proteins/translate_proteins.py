#!/usr/bin/env python3

"""
Author : donaldscoon
Date   : 2019-02-15
Purpose: Translating the itty bitty codons.
"""

import re
import os
import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR, -c/--codons', help='A positional argument')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations (default: None)',
        metavar='str',
        type=str,
        required=True,
        default='')

    parser.add_argument(
        '-o',
        '--output',
        help='Output filename (default: out.txt)',
        metavar='str',
        type=str,
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
    args = get_args()
    codons = args.codons

    if not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
