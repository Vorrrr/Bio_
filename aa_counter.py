import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


aa_count = []
A = False
file = open(input(), 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if gene == 'protein_coding':
        aa_count.append(int(i[17])// 3 - 1)
        if int(i[17])// 3 - 1 > 2000:
            A = True
    if A and gene == 'with_protein':
        print(i[13], '; lenght: ', aa_count[-1], sep='')
        A = False
file.close()
data = pd.DataFrame(data=aa_count)
h = data.hist(legend=False, bins=70)
print('Средняя длина белков:', int(data.mean()))
print('Медиана длины белков:', int(data.median()))
print('Мода длин белков:', int(data.median()))

plt.show()
