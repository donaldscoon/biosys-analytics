#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-03-04
Purpose: Matchy Matchy
"""

import argparse
import sys
import os
import re
import csv
from collections import Counter
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument(
    #     'positional', metavar='FILE', help='BLAST output (-outfmt 6)')
    parser.add_argument('file', metavar='FILE', help='Input file')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotations file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
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


# --------------------------------------------------
def main():
    """Do jazz hands make noise?
       if so that noise goes here. """
    args = get_args()
    blast_hits = args.file
    anno_file = args.annotations
    out_file = args.outfile

    if not os.path.isfile(blast_hits):
        die('"{}" is not a file'.format(blast_hits))
    """Cant use both of these for some reason"""
    # if not os.path.isfile(anno_file):
    #     die('"{}" is not a file'.format(anno_file)

    """Outputs records to dictionary {d_anno}"""
    d_anno = {}
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            seqid = row.get('centroid')
            d_anno[seqid] = row
    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    """Outputs record to dictionary {d_blast}"""
    d_blast = {}
    with open(blast_hits) as fh:
        fieldnames = 'qsedid sseqid pident length mismatch gapopen qstart sstart send evalue bitscore'.split()
        reader = csv.DictReader(fh, delimiter='\t', fieldnames=fieldnames)
        for row in reader:
            sseqid = row.get('sseqid')
            d_blast[sseqid] = row
    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    """Section that makes the comparisons"""
    for row in d_blast:
        lookup = d_blast.get(row).get('sseqid')
        lookup_pident = d_blast.get(row).get('pident')
        if lookup in d_anno:
            genus = d_anno.get(lookup).get('genus')
            species = d_anno.get(lookup).get('species')
            if genus == '':
                genus = 'NA'
                if species == '':
                    species = 'NA'
            print("seq_id\tpident\tgenus\tspecies", file=open(out_file, 'a'))
            if out_file:
                print("{}\t{}\t{}\t{}".format(lookup, lookup_pident, genus, species), file=open(out_file, "a"))
            else:
                print("{}\t{}\t{}\t{}".format(lookup, lookup_pident, genus, species))
        else:
            warn('Cannot find seq "{}" in lookup'.format(lookup))

# --------------------------------------------------
if __name__ == '__main__':
    main()
