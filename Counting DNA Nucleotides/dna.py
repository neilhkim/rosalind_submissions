with open('rosalind_dna.txt') as f:
    data = f.read()

a, c, g, t = data.count('A'), data.count('C'), data.count('G'), data.count('T')
print(a, c, g, t)