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
# from tabulate import tabulate

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
        type=int)

    parser.add_argument(
        '-n',
        '--distance',
        help='max allowed hamming distance for two words to be the same',
        metavar='INT',
        type=int)

    # parser.add_argument(
    #     '-l',
    #     '--logfile',
    #     help='the file log statements are printed to',
    #     action='store_true',
    #     default='.log')

    # parser.add_argument(
    #     '-t',
    #     '--table',
    #     help='converts output to ascii table',
    #     action='store_true',
    #     default= False)


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


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1 = args.positional[0]
    file2 = args.positional[1]
    max_hamm = args.distance
    min_len = args.min_len
    
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
            list_1.append(word)
    for line in fh2:
        for word in line.split():
            list_2.append(word)
    """###########################"""
    """pull words from the files"""
    # d_print = {}
    for word1, word2, in zip(list_1, list_2):
        distance = dist(word1, word2)
        l = [word1, word2, distance]
        if len(l[0]) <= min_len:
            continue
        if l[2] <= max_hamm:
            continue
        big_list.append(l)
    print(big_list)
        # print("{}   {}   {}".format(word1, word2, distance))


    # """Checks the length of the hamming subjects"""
    # count = 0
    # for word1, word2 in zip(list_1, list_2):
    #     count += dist(word1,word2)
    # print(count)
    # """##########################"""
# -----------------------------------------------
if __name__ == '__main__':
    main()
