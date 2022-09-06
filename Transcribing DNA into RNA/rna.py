with open('rosalind_rna.txt') as f:
    t = f.read()
u = t.replace('T', 'U')
print(u)