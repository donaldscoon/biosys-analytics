#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-19
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
from collections import Counter
from collections import defaultdict



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='str', help='A positional argument', nargs='+')

    parser.add_argument(
        '-s',
        '--sort',
        help='Switches sort to numerically in ascending order',
        action='store_true',
        default=False)

    parser.add_argument(
        '-m',
        '--min',
        help='minimum number of times a word must occur',
        metavar='int',
        type=int,
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
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional
    sort = args.sort
    num = args.min

    dictionary = defaultdict(int)

    """ PULLING WORDS FROM FILES INTO DICTIONARIES"""
    for item in files:
        if not os.path.isfile(item):
            die('"{}" is not a file'.format(item))
        with open(item) as fh:
            for line in fh:
                for thing in line.split():
                    thing = (re.sub('[^a-zA-Z0-9]', '', thing.lower()))
                    dictionary[thing] += 1
    """##########################################"""

    """SORT ALPHBETICALLY"""
    if sort == False:
        for word in sorted(dictionary):
            count = dictionary.get(word)
            # print(word)
            print('{:20} {}'.format(word, count))
    else:
        for word in sorted(dictionary.values()):
            count = dictionary.get(word)
            # print(word)
            print('{:20} {}'.format(word, count))






# --------------------------------------------------
if __name__ == '__main__':
    main()
