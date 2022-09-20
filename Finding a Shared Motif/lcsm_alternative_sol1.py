# import sys
# sys.path.append('../')

def longest_common(seqs):
    shortest_seq = min(seqs, key=len)
    for motif_len in range(len(shortest_seq), 0, -1):
        for mpos in range(len(shortest_seq) - motif_len + 1):
            motif = shortest_seq[mpos:mpos + motif_len]
            if all(motif in seq for seq in seqs):
                return motif
    return ""

from os.path import exists
from Bio import SeqIO

if exists('rosalind_lcsm.txt'):
    with open('rosalind_lcsm.txt') as f:
        fasta = SeqIO.parse(f, 'fasta')
        seqs = [entry.seq for entry in fasta]
        lcsm = longest_common(seqs)
        print(lcsm)
        print(len(lcsm))
# Make a python file for common read and write