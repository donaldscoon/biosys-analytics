#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-02-26
Purpose: Rock the Casbah
"""

import os
import argparse
import sys
import re
from collections import Counter
from bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='FASTA files to read', nargs='+')

    parser.add_argument(
        '-o',
        '--outdir',
        help='directory name to write the output',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='Percent GC',
        metavar='int',
        type=int,
        default=50)

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
    """Scatty Datt Dat Doo"""
    args = get_args()
    fasta = args.fasta
    out_dir = args.out
    pct_gc = args.pct_GC

    for pathname in args.positional:
       if not os.path.isfile(pathname):
          warn('"{}" is not a file'.format(pathname))
          continue

    for file in fasta:
       print(file)
       for record in SeqIO.parse(file, 'fasta'):
          print(record.seq)
          seq_len = len(record.seq)
          nucs = (Counter(record.seq)
          gcnum = nucs.get('G', 0) + nucs.get('C', 0)
          #print(record.seq)
          gc = (int(gc_num/seq_len * 100))
          print(gc)
          print('HIGH' if gc >= pct_gc else 'LOW')
          print()

print('Test Complete, did you screw it up?')







"""    d = {}
       print(dirname)

       for file in os.listdir(dirname):
           path = os.path.join(dirname, file)
           line = open(path).readline().rstrip()
           d[line] = file
"""



# --------------------------------------------------
if __name__ == '__main__':
    main()
