from os.path import exists


if exists('rosalind_hamm.txt'):
    with open('rosalind_hamm.txt') as f:
        # s = f.read().split('\n')[0]
        # t = f.read().split('\n')[1]
        split = f.read().split('\n')
        s = split[0]
        t = split[1]
        # print(s)
        # print(t)
else:
    s = 'GAGCCTACTAACGGGAT'
    t = 'CATCGTAATGACGGCCT'


dist = 0
for i in range(len(s)):
    if s[i] != t[i]:
        dist += 1

print(dist)