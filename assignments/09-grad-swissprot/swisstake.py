#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-16
Purpose: Rock the Casbah
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
        'FILE', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-k',
        '--keyword',
        help='take on keyword (default: None)',
        metavar='STR',
        type=str,
        default='None')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa (default: )',
        metavar='STR',
        type=str,
        default='',
        nargs='+')

    parser.add_argument(
        '-o',
        '--output ',
        help='output filename (default: out.fa)',
        metavar='FILE',
        type=str,
        default='out.fa')

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
    # search_terms = args.keywords
    input_file = args.FILE
    # out_file = args.output

    if not os.path.isfile(input_file):
        die('"{}" is not a file'.format(input_file))
    
    print('Processing "{}".'.format(input_file))

    for i, record in enumerate(SeqIO.parse(input_file, "swiss"), start=1):
        # print('{}: {}'.format(i, record.id))
        annotations = record.annotations
        
        """lines with KW are the ANNOTATIONS"""

        for annot_type in ['keywords']:
            if annot_type in annotations:
                val = annotations[annot_type]
                """INSERT AN IF STATEMENT FOR SKIPPING
                MAKE THE REST ELIF/ELSE"""
                if type(val) is list:
                    for v in val:
                        print('{}'.format(v))
                else:
                    print('{}'.format(val))

# --------------------------------------------------
if __name__ == '__main__':
    main()
