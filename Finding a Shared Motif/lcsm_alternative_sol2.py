# Binary Search method
# Edited the version by Petar Ivanov

import rosalind_io as rio

def substr_in_all(seqs, motif):
    for seq in seqs:
        if motif not in seq:
            return False
    return True

def common_substr(seqs, lll):
    firstseq = seqs[0]
    for i in range(len(firstseq)-lll+1):
        motif = firstseq[i:i+lll]
        if substr_in_all(seqs, motif):
            print(motif)
            return motif
    return ""

def longest_common_substr(seqs):
    l = 0
    r = len(seqs[0])
    while l + 1 < r:
        mid = round((l+r)/2)
        print(mid)
        if common_substr(seqs, mid) == "":
            r = mid
        else:
            l = mid
    # print(f"{l}, {mid}, {r}")
    ret = common_substr(seqs, l)
    ret = str(ret)
    return ret

seqs = rio.read_seq_from_fasta('rosalind_lcsm.txt')
# seqs = str(seqs)
output = longest_common_substr(seqs)
rio.write_seq_from_fasta('output_lcsm.txt', output)