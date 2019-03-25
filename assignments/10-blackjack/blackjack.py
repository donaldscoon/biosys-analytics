#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-21
Purpose: Rock the Casbah
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
        '-s', '--seed', help='activates seed', action='store_true')

    parser.add_argument(
        '-p', '--player_hits', help='Player takes an extra card', action='store_true')

    parser.add_argument(
        '-d', '--dealer_hits', help='Dealer takes an extra card', action='store_true')

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
    """Make a jack black noise here"""
    args = get_args()
    p_hits = args.player_hits
    d_hits = args.dealer_hits
    # seed = args.seed
    print(p_hits)
    print(d_hits)
    """ADD RANDOM SEED STUFF HERE"""

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suite = ['♥', '♠', '♣', '♦']

    deck = sorted(product(suite, cards))
    shuffle = random.shuffle(deck)

    """I should probably find a way to make this shorter."""
    if p_hits and d_hits == False:
        """First Card"""
        p_draw_1 = deck.pop(0)
        p_c_draw_1 = p_draw_1[1]
        p_s_draw_1 = p_draw_1[0]
        p_v1 = p_draw_1[1]
        if p_v1 == 'J':
            p_v1 = 10
        if p_v1 == 'Q':
            p_v1 = 10
        if p_v1 == 'K':
            p_v1 = 10
        if p_v1 == 'A':
            p_v1 = 1
        p_card1 = p_s_draw_1 + p_c_draw_1

        """Second Card"""
        d_draw_1 = deck.pop(0)
        d_c_draw_1 = d_draw_1[1]
        d_s_draw_1 = d_draw_1[0]
        d_v1 = d_draw_1[1]
        if d_v1 == 'J':
            d_v1 = 10
        if d_v1 == 'Q':
            d_v1 = 10
        if d_v1 == 'K':
            d_v1 = 10
        if d_v1 == 'A':
            d_v1 = 1
        d_card1 = d_s_draw_1 + d_c_draw_1

        """Third Card"""
        p_draw_2 = deck.pop(0)
        p_c_draw_2 = p_draw_2[1]
        p_s_draw_2 = p_draw_2[0]
        p_v2 = p_draw_2[1]
        if p_v2 == 'J':
            p_v2 = 10
        if p_v2 == 'Q':
            p_v2 = 10
        if p_v2 == 'K':
            p_v2 = 10
        if p_v2 == 'A':
            p_v2 = 1
        p_card2 = p_s_draw_2 + p_c_draw_2

        """Fourth Card"""
        d_draw_2 = deck.pop(0)
        d_c_draw_2 = d_draw_2[1]
        d_s_draw_2 = d_draw_2[0]
        d_v2 = d_draw_2[1]
        if d_v2 == 'J':
            d_v2 = 10
        if d_v2 == 'Q':
            d_v2 = 10
        if d_v2 == 'K':
            d_v2 = 10
        if d_v2 == 'A':
            d_v2 = 1
        d_card2 = d_s_draw_2 + d_c_draw_2

        """Math Time"""
        player_total = int(p_v1) + int(p_v2)
        dealer_total = int(d_v1) + int(d_v2)

        """Player Hits"""
        if p_hits is not False:
            p_draw_3 = deck.pop(0)
            p_c_draw_3 = p_draw_3[1]
            p_s_draw_3 = p_draw_3[0]
            p_v3 = p_draw_3[1]
            if p_v3 == 'J':
                p_v3 = 10
            if p_v3 == 'Q':
                p_v3 = 10
            if p_v3 == 'K':
                p_v3 = 10
            if p_v3 == 'A':
                p_v3 = 1
            p_card3 = p_s_draw_3 + p_c_draw_3
            player_total = int(player_total) + int(p_v3)
        
        """Dealer Hits"""
        if d_hits is not False:
            d_draw_3 = deck.pop(0)
            d_c_draw_3 = d_draw_3[1]
            d_s_draw_3 = d_draw_3[0]
            d_v3 = d_draw_3[1]
            if d_v3 == 'J':
                d_v3 = 10
            if d_v3 == 'Q':
                d_v3 = 10
            if d_v3 == 'K':
                d_v3 = 10
            if d_v3 == 'A':
                d_v3 = 1
            d_card3 = d_s_draw_3 + d_c_draw_3
            dealer_total = int(dealer_total) + int(d_v3)

        """Now we shall see, who wins!"""
        print("{} {} {}".format(d_card1, d_card2, dealer_total))
        print("{} {} {}".format(p_card1, p_card2, player_total))



# --------------------------------------------------
if __name__ == '__main__':
    main()
