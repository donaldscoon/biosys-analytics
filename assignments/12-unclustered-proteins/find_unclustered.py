#!/usr/bin/env python3
"""
Author : donaldscoon
Date   : 2019-04-04
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
        '-c',
        '--cdhit',
        help='name of the CD-HIT cluster file',
        metavar='str',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='FASTA file',
        metavar='int',
        type=str,
        default='',
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='place to put matchs',
        metavar='str',
        type=str,
        default='unclustered.py')

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
    cdhit = args.cdhit
    proteins = args.proteins
    out_file = args.outfile


    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))
         
    if not os.path.isfile(cdhit):
        die('--cdhit "{}" is not a file'.format(cdhit))

    cd_re = re.compile('(?P<ig>[|])'
                       '(?P<cd_id>\d{1,})'
                       '(?P<nor>[|])')

    p_re = re.compile('(?P<ignore>[>])'
                      '(?P<p_id>\d{1,})')

    """Pull clusters from cdhits"""
    cluster_count = 0
    d_cluster = {}
    with open(cdhit) as cdfh:
        for line in cdfh:
            # print(line)
            cluster_match = cd_re.search(line)
            if cluster_match != None:
                cluster_count += 1
                d_cluster[cluster_match.group('cd_id')] = cluster_count
    # print(d_cluster)
    """Pull protein ID from fasta file"""
    protein_count = 0
    d_protein = {}
    with open(proteins) as pfh:
        for line in pfh:
            protein_match = p_re.search(line)
            if protein_match != None:
                protein_count +=1
                d_protein[protein_match.group('p_id')] = protein_count
    
    matchy_matchy = 0
    for item in d_protein:
        if item in d_cluster:
            matchy_matchy += 1
    print(protein_count - cluster_count)
    print('"{}""{}"'.format(cluster_count, protein_count))

    out_file = open(out_file, 'w+')




# --------------------------------------------------
if __name__ == '__main__':
    main()
