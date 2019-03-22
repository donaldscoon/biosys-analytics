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
import itertools, random
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

    deck = list(product(suite, cards))
    print(deck)

    # while len(deck) != 0:
    #     """ready Player 1"""
    #     player1 = deck.pop(0)
    #     player1_card = player1[1]
    #     player1_suite = player1[0]
    #     player1_hand = player1_suite + player1_card

    #     """ready Player 2"""
    #     player2 = deck.pop(0)
    #     player2_card = player2[1]
    #     player2_suite = player2[0]
    #     player2_hand = player2_suite + player2_card

        # """this means war"""
        # if player1_card > player2_card:
        #     winner = ('Player 1')
        #     print('{} {} {}'.format(player1_hand, player2_hand, winner))
        # elif player1_card < player2_card:
        #     winner = ('Player 2')
        #     print('{} {} {}'.format(player1_hand, player2_hand, winner))
        # else:
        #     winner = ('Draw')
        #     print('{} {} {}'.format(player1_hand, player2_hand, winner))


# --------------------------------------------------
if __name__ == '__main__':
    main()
