#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-04
Purpose: Matchy Matchy
"""

import argparse
import sys
import os
import re
import csv
from collections import Counter
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotations file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    """"""
    args = get_args()
    blast_file = args.positional
    anno_file = args.annotations
    out_file = args.outfile
    # print(blast_file)
    # print(anno_file)
    # print(out_file)

    if not os.path.isfile(blast_file):
        die('"{}" is not a file'.format(blast_file))
    """Cant use both of these for some reason"""
    # if not os.path.isfile(anno_file):
    #     die('"{}" is not a file'.format(anno_file)


    for line in open(blast_file):
        split = line.split('\t', 3)
        blast_out = split[1:3]
        # print(blast_out)

    # for line in open(anno_file):
    #     split = line.split(',')
    #     anno_out = split[6:]
    #     print(anno_out)
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            print(row.get('genus'))
            print(row.get('species'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
