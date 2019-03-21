#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-21
Purpose: Single player card games
"""

import argparse
import sys
import os
import re
import csv
from collections import Counter
from Bio import SeqIO
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='used for testing',
        metavar='int',
        type=int,
        default=None)

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
    """Dizzy Atmosphere by Dizzy Gillespie"""
    args = get_args()
    seed = args.seed

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suite = ['♥', '♠', '♣', '♦']

    deck = list(product(cards, suite))

    print(len(deck))

# --------------------------------------------------
if __name__ == '__main__':
    main()
