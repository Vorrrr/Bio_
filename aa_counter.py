import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


aa_count = []
file = open('C:\Надя\GCF_013343195.2_ASM1334319v3_feature_table.txt', 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if gene == 'protein_coding':
        aa_count.append(int(i[17])// 3)
file.close()
data = pd.DataFrame(data=aa_count)
h = data.hist(legend=False, bins=70)
plt.show()
print(h)

