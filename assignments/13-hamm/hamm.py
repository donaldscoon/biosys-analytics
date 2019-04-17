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


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'File File', metavar='str', help='Files to Hamm', nargs=2)

    parser.add_argument(
        '-a',
        '--arg',
        help='A named string argument',
        metavar='str',
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

#--------------------------------------------------
def hamdist(str1, str2):
 
        diffs = 0
        for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                        diffs += 1
        return diffs

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

 
if __name__ == "__main__":
   lines = []
   for line in open("rosalind_hamm.txt"):
      lines.append(line)
   s = lines[0]
   t = lines[1]
   
   dist = hamming_distance(s,t)
   print(dist)

# --------------------------------------------------
if __name__ == '__main__':
    main()
