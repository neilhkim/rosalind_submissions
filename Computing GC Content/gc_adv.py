def sort_seq(seq):
    seq_info = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
        'length': 0,
        'GC_ratio': 0,
    }
    for letter in seq:
        seq_info[letter] += 1
    seq_info['length'] = len(seq)
    seq_info['GC_ratio'] = (seq_info['C'] + seq_info['G']) / seq_info['length']
    return seq_info

ret = sort_seq('ACGTGCGAGTGCGCGCGGAGT')
print(list(ret.items()))