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
        help='take on keyword',
        metavar='STR',
        type=str,
        default='None',
        required=True)

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        default='',
        nargs='+')

    parser.add_argument(
        '-o',
        '--output',
        help='output filename',
        metavar='FILE',
        type=str,
        default='out_test.fa')

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
    search_terms = args.keyword
    input_file = args.FILE
    out_file = args.output
    taxa_skip = set(args.skip)

    if not os.path.isfile(input_file):
        die('"{}" is not a file'.format(input_file))

    print('Processing "{}"'.format(input_file))

    skip_counter = 0
    take_counter = 0

    out_fh = open(out_file, "w+")

    for record in SeqIO.parse(input_file, "swiss"):
        annotations = record.annotations
        for annot_type in ['keywords', 'taxonomy']:
            if annot_type in annotations:
                val = set(annotations['keywords'])
                tax = set(annotations['taxonomy'])
                #### Needs all same case .upper or .lower
                if len(taxa_skip.intersection(tax)) > 0:
                    skip_counter += 1
                    # print(skip_counter)
                else:
                    SeqIO.write(record, out_fh, "fasta")
                    take_counter += 1
                    # print(take_counter)
    print('Done, skipped {} and took {}. See output in "{}"'.format(skip_counter, take_counter, out_file))



                # """MATCHS SKIP TERMS TO LIST OF TAXA
                #    need to make it so the program skips
                #    now I am hoarding this to make an attempt
                #    at using sets"""
                # for item in tax:
                #     if item in taxa_skip:
                #         print('ABANDON SHIP')
                # """PRINTS OUT KEYWORDS """
                # if type(val) is list:
                #     for v in val:
                #         print('{}'.format(v))
                # else:
                #     print('{}'.format(val))

# Stuff for guessing game
# variables upper bound, lower bounds, num guess
# import random
# new variable secret number random.choice(range(low,high))
# new variable seed in arg parse default None type int
# seed = args.seed
# not a number error check if guess.isdigit(): >>>continue
# if seed is not None:
#     random.seed(seed)
# prompt=(String)
# while numguess > 0:
#     num guesses -= 1
#     guess=input(prompt)
#     print(guess)
#     guess== int(guess)
#     if guess == secret
#         print(win)
#         sys.exit(0)
#     elif guess < secret:
#         print(low)
#     elif guess > secret:
#         print(high)
# print(youlose)

# --------------------------------------------------
if __name__ == '__main__':
    main()
