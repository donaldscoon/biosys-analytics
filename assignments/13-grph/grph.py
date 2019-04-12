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

    text = [line.strip() for line in open(input_file)]
    i = 2
    while i < len(text):
        if not text[i].startswith('>') and not text[i-1].startswith('>'):
            text[i-1] += text[i]
            del text[i]
            i -= 1
        i += 1
    dna = {}
    for i in range(0,len(text),2):
        dna[text[i][1:]] = text[i+1]
    for first in dna.keys():
        for second in dna.keys():
            if first != second and dna[first][len(dna[first])-k_value:] == dna[second][0:k_value]:
                print(first + " " + second)







    # d_k_start = {}
    # d_k_end = {}

    # d_k_title_re = re.compile('(?P<title>Rosalind_\d{4})$')

    # d_k_start_re = re.compile('(?P<start>^[ACGTacgt]{3})')

    # d_k_end_re = re.compile('(?P<end>\D{3}$)')

    # with open(input_file) as fh:
    #     for line in fh:
    #         print(line)
            # match1 = d_k_title_re.search(line)
            # d_match = match1.groupdict()
            # print(d_match)

        # d_match['month'] = (d_months.get(month))





# --------------------------------------------------
if __name__ == '__main__':
    main()
