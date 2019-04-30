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

#--------------------------------------------------
def dist(str1, str2):

    char_count = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            char_count += 1
    len_count = abs(len(str1) - len(str2))
    diffs = len_count + char_count
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(str1,str2, diffs))
    return diffs

def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1 = args.positional[0]
    file2 = args.positional[1]
    max_hamm = args.hamming_distance
    min_len = args.min_len
    table = args.table
    
    if max_hamm < 0:
        die('--distance "{}" must be > 0'.format(max_hamm))

    if min_len < 0:
        die('--min_len "{}" must be > 0'.format(min_len))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    logging.debug('file1 = {}, file2 = {}'.format(file1, file2))

    if not os.path.isfile(file1):
        die('"{}" is not a file'.format(file1))
    if not os.path.isfile(file2):
        die('"{}" is not a file'.format(file2))

    fh1 = open(file1)
    fh2 = open(file2)

    """Creates lists to use later"""
    list_1 = []
    list_2 = []
    big_list = []

    for line in fh1:
        for word in line.split():
            word = (re.sub('[^a-zA-Z0-9]', '', word.lower()))
            list_1.append(word)
    for line in fh2:
        for word in line.split():
            word = (re.sub('[^a-zA-Z0-9]', '', word.lower()))
            list_2.append(word)
    """###########################"""

    """pull words from the files"""
    for word1, word2, in zip(list_1, list_2):
        distance = dist(word1, word2)
        l = [word1, word2, distance]
        if len(l[0]) < min_len:
            continue
        if max_hamm != False:
            if l[2] > max_hamm:
                continue
        logging.debug('words campared are {}'.format(l))
        big_list.append(l)

    """tabulate that output"""
    if table == False:
        headers = ['word1', 'word2', 'distance']
        print('\t'.join(headers))
        for line in sorted(big_list):
            print('{}\t{}\t{}'.format(line[0], line[1], line[2]))
        # print(tabulate(big_list, headers="firstrow"))
    else:
        print(tabulate(sorted(big_list), headers=['word1', 'word2', 'distance'], tablefmt="psql"))

    #"""old print statement for testing"""
    # for line in sorted(big_list):
    #     print('{:15} {:15} {:8}'.format(line[0], line[1], line[2]))
# -----------------------------------------------
if __name__ == '__main__':
    main()
