#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-21
Purpose: Single player card games
"""

import argparse
import sys
import os
import itertools, random
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
        help='helps pass the test',
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

    """ADD RANDOM SEED STUFF HERE"""
    if seed is not None:
        random.seed(seed)

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suite = ['♥', '♠', '♣', '♦']
    # value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

    deck = sorted(product(suite, cards))
    shuffle = random.shuffle(deck)
    player1_wins = 0
    player2_wins = 0

    while len(deck) != 0:
        """Ready Player 1?"""
        player1 = deck.pop(0)
        player1_card = player1[1]
        player1_suite = player1[0]
        player1_value = player1[1]
        if player1_value == 'J':
            player1_value = 11
        if player1_value == 'Q':
            player1_value = 12
        if player1_value == 'K':
            player1_value = 13
        if player1_value == 'A':
            player1_value = 14
        player1_hand = player1_suite + player1_card

        """Ready Player 2?"""
        player2 = deck.pop(0)
        player2_card = player2[1]
        player2_suite = player2[0]
        player2_value = player2[1]
        if player2_value == 'J':
            player2_value = 11
        if player2_value == 'Q':
            player2_value = 12
        if player2_value == 'K':
            player2_value = 13
        if player2_value == 'A':
            player2_value = 14
        player2_hand = player2_suite + player2_card


        """This means war"""
        if int(player1_value) > int(player2_value):
            winner = ('P1')
            print('{} {} {}'.format(player1_hand, player2_hand, winner))
            player1_wins += 1
        elif int(player1_value) < int(player2_value):
            winner = ('P2')
            print('{} {} {}'.format(player1_hand, player2_hand, winner))
            player2_wins += 1
        else:
            winner = ('WAR!')
            print('{} {} {}'.format(player1_hand, player2_hand, winner))

    """and the winner is..."""
    if player1_wins > player2_wins:
        print('P1 {} P2 {}: Player 1 wins'.format(player1_wins, player2_wins))
    elif player1_wins < player2_wins:
        print('P1 {} P2 {}: Player 2 wins'.format(player1_wins, player2_wins))
    else:
        print('P1 {} P2 {}: DRAW'.format(player1_wins, player2_wins))
        """Nobody. They both suck at random chance games."""



# --------------------------------------------------
if __name__ == '__main__':
    main()
