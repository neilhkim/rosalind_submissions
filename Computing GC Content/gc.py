from Bio import SeqIO

# readstring = '>asdf\nacgcatgctagctatcagtc\n>dfsjk\ngtcagtagctagctagcatcagc'
with open('rosalind_gc.txt') as f:
    readstring = f.read()

# for record in SeqIO.parse('rosalind_gc.txt', 'fasta')

lastmax = 0
lastmaxid = ''
for seq in SeqIO.parse('rosalind_gc.txt', 'fasta'):
    # print(seq.seq)
    gc_ratio = (seq.seq.count('G') + seq.seq.count('C'))/len(seq.seq)
    if gc_ratio > lastmax:
        lastmax = gc_ratio
        lastmaxid = seq.id

print(lastmaxid)
print(float(lastmax)*100)
# readstring = readstring.upper()

# print(readstring)

# while readstring.find('\n'):

pass



# fasta_pairs = readstring.split('>')
# # print(fasta_pairs)
# if fasta_pairs[0] == '':
#     del fasta_pairs[0]
# print(fasta_pairs)
# dict = {}
# for fasta_pair in fasta_pairs:
#     comps = fasta_pair.split('\n')
#     # print(comps)
#     nG = comps[1].count('G')
#     nC = comps[1].count('C')
#     ratio = (nC + nG)/len(comps[1])
#     # print(ratio)
#     dict[comps[0]] = (nC + nG)/len(comps[1])

# # print(list(dict.items()))         
# ks = dict.keys()
# vs = dict.values()
# print(ks)
# print(vs)


# max_gc_ratio = max(dict.values())
# max_gc_key = [z for z in dict.keys() if dict[z] == max_gc_ratio]

# print(max_gc_key)
# print(max_gc_ratio)


# # print(dict.items())        
# # a, c, g, t = s.count('A'), s.count