from os.path import exists
from Bio import SeqIO

def read_seq_from_fasta(fname):
    if exists(fname):
        with open('rosalind_lcsm.txt') as f:
            fasta = SeqIO.parse(f, 'fasta')
            seqs = [entry.seq for entry in fasta]
            return seqs

def write_seq_from_fasta(fname, output):
    with open(fname, 'w') as f:
        f.write(output)
