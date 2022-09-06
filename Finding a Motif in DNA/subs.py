from os.path import exists

fname = 'rosalind_subs.txt' 
if exists(fname):
    with open(fname) as f:
        read = f.read()
        # print(read)
        s, t, junk = read.split('\n')

else:
    s = 'GATATATGCATATACTT'
    t = 'ATAT'


print(s)
print(t)

locs = []
start = 0

while True:
    loc = s.find(t, start)
    if loc > -1:
        locs.append(loc+1)
        start = loc+1
    else:
        break

for item in locs:
    print(item, end=" ")
# print(locs)