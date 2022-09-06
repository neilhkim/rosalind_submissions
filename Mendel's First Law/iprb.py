with open('rosalind_iprb.txt') as f:
    sread = f.read()

splitlist = sread.split(' ', '\n')
# splitlist = splitlist.split('\n')

# print(int(sread))
# k, m, n = 22, 26, 20
k, m, n = splitlist
sum = k + m + n
res = 0
res += k/sum
res += m/sum*(k/(sum-1) + (m-1)/(sum-1)*3/4 + n/(sum-1)*1/2)
res += n/sum*(k/(sum-1) + m/(sum-1)*1/2)

print(res)

