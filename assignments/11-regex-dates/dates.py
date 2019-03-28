#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-26
Purpose: Correct all the bad formatting
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


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
    """If I have run out of jazz mentions.
       can I just improvise like they did
       occasionally?"""







# --------------------------------------------------
if __name__ == '__main__':
    main()
