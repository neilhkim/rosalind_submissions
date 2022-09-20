from Bio import SeqIO
from os.path import exists
# import sys
# sys.path.append('../')

inputfile = 'rosalind_lcsm.txt'
eg_input_file = 'rosalind_lcsm_example.txt'

if exists(inputfile):
    f = open(inputfile)
elif exists(eg_input_file):
    f = open(eg_input_file)
else: 
    print('No input file')
fasta = SeqIO.parse(f, 'fasta')
strands = [rec.seq for rec in fasta]
ref_strand = min(strands, key=len)
strands.remove(ref_strand)

longest_common_str = ''
for motif_len in range(len(ref_strand), 2, -1):
    # print(f"motif_len: {motif_len}")
    motif_list = []
    for pos1 in range(len(ref_strand) - motif_len + 1):
        motif = ref_strand[pos1:pos1 + motif_len]
        if motif in motif_list:
            # print(f'This motif has been tested: {motif}')
            continue
        else:
            motif_list.append(motif)

        for strand in strands:
            commonstr_in_strand = False
            for pos2 in range(len(strand) - motif_len + 1):
                if strand[pos2:pos2 + motif_len] == motif:
                    commonstr_in_strand = True
                    break
            if not commonstr_in_strand:
                break
        if commonstr_in_strand:
            print(f'This motif is the longest common motif. Len: {motif_len}')
            longest_common_str = motif
            print(motif)
            break
    if commonstr_in_strand:
        break