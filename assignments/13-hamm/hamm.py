#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-11
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
import logging


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Files to Hamm', nargs=2)

    parser.add_argument(
        '-d',
        '--debug',
        help='turns on lowlevel debug statements',
        action='store_true',
        default=False)


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
    return diffs
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(str1,str2, diffs))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    file1 = args.positional[0]
    file2 = args.positional[1]
    
    if not os.path.isfile(file1):
        die('"{}" is not a file'.format(file1))
    if not os.path.isfile(file2):
        die('"{}" is not a file'.format(file2))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    fh1 = open(file1)
    fh2 = open(file2)

    list_1 = []
    list_2 = []

    for line in fh1:
        for word in line.split():
            list_1.append(word)
    for line in fh2:
        for word in line.split():
            list_2.append(word)

    # print(list_1)
    # print(list_2)

    """Checks the length of the hamming subjects"""
    count = 0
    for word1, word2 in zip(list_1, list_2):
        count += dist(word1,word2)
    print(count)
    # print(distance)





# --------------------------------------------------
if __name__ == '__main__':
    main()
