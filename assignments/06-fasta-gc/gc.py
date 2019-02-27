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
from Bio import SeqIO

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
    fasta = args.positional
    out_dir = args.outdir
    pct_gc = args.pct_gc


#    print(args)
#    print(fasta[0])
#    print(out_dir)
#    print(pct_gc)


    for files in fasta:
        if not os.path.isfile(fasta[0]):
            warn('"{}" is not a file'.format(fasta[0]))
            continue

    if not 100 >= pct_gc > 0:
        print('"{}" must be between 0 and 100'.format(pct_gc))

    for file in fasta:
        print(file)
        for record in SeqIO.parse(file, 'fasta'):
            #print(record.seq)
            seq_len = len(record.seq)
            #print(seq_len)
            nucleo = (Counter(record.seq))
            #print(nucleo)
            gc_num = nucleo.get('G', 0) + nucleo.get('C', 0)
            #print(record.seq)
            gc = (int(gc_num/seq_len * 100))
            #print(gc)
            """Attempt at one line :( didnt work
            gc_state = ('{}_HIGH'.format(fasta[0])) if gc >= pct_gc else ('{}_LOW'.format(fasta[0]))
            print(gc_state)"""

            if gc >= pct_gc:
                gc_state = ('{}_HIGH'.format(fasta[0]))
            else:
                gc_state = ('{}_LOW'.format(fasta[0]))
            print(gc_state)


    print('Test Complete, did you screw it up?')







#--------------------------------------------------
if __name__ == '__main__':
    main()
