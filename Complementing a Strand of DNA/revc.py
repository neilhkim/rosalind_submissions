from tkinter import S


with open('rosalind_revc.txt') as f:
    s = f.read()
s = s.replace('A', 't')
s = s.replace('T', 'a')
s = s.replace('C', 'g')
s = s.replace('G', 'c')
s = s[::-1]
s = s.upper()
print(s)

