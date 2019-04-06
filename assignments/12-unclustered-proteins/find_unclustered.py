#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-04
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
        '-c',
        '--cdhit',
        help='name of the CD-HIT cluster file',
        metavar='str',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='FASTA file',
        metavar='int',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='place to put matchs',
        metavar='str',
        type=str,
        default='unclustered.py')

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
    str_arg = args.arg
    int_arg = args.int
    flag_arg = args.flag
    pos_arg = args.positional

    print('str_arg = "{}"'.format(str_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
