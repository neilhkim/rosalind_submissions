from os.path import exists
from Bio import SeqIO 
import numpy as np

fname = 'rosalind_cons.txt'
# fname = 'rosalind_gc.txt'
if exists(fname):
    parsed = SeqIO.parse(fname, 'fasta')
else:
    read = '>Rosalind_1\nATCCAGCT\n>Rosalind_2\nGGGCAACT\n>Rosalind_3\nATGGATCT\n>Rosalind_4\nAAGCAACC\n>Rosalind_5\nTTGGAACT\n>Rosalind_6\nATGCCATT\n>Rosalind_7\nATGGCACT'

# x = list(parsed.items())

consensus_seq = ''
seqlen = 0
ACGTstring = 'ACGT'

for item in parsed:
    if seqlen == 0:
        seqlen = len(item.seq)
        nA = [0] * seqlen
        nC = np.zeros(seqlen)
        nG = np.zeros(seqlen)
        nT = np.zeros(seqlen)
        nA = np.intc(nA)
        nC = np.intc(nC)
        nG = np.intc(nG)
        nT = np.intc(nT)
    elif seqlen != len(item.seq):
        print('seqlen not one.')
        exit()
    for i in range(seqlen):
        if item.seq[i] == 'A':
            nA[i] += 1
        elif item.seq[i] == 'C':
            nC[i] += 1
        elif item.seq[i] == 'G':
            nG[i] += 1
        elif item.seq[i] == 'T':
            nT[i] += 1
        else:
            print('Character not ACGT')

# Most frequent seq
for i in range(seqlen):
    test_list = [nA[i], nC[i], nG[i], nT[i]]
    most_freq_letter = ACGTstring[test_list.index(max(test_list))]
    consensus_seq += most_freq_letter

print(consensus_seq)

print('A: ', end='')
for i in range(seqlen):
    print(nA[i], end=' ')

print('\nC: ', end='')
for i in range(seqlen):
    print(nC[i], end=' ')

print('\nG: ', end='')
for i in range(seqlen):
    print(nG[i], end=' ')

print('\nT: ', end='')
for i in range(seqlen):
    print(nT[i], end=' ')