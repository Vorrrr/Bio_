# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


ribo_cou = 0
ribo_pr = 0
total = 0
file = open('C:\Надя\GCF_013343195.2_ASM1334319v3_feature_table.txt', 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if gene == 'with_protein':
        if 'riboso' in i[13]:
            ribo_cou += 1
            if 'ribosomal protein' in i[13]:
                ribo_pr += 1
        total += 1
        
file.close()
print('Ribosome-assotiated proteins: ', ribo_cou, '\n', 'Ribosomal proteins: ', ribo_pr, '\n', 'Percentage of ribosomal proteins in proteom - ', round(ribo_pr/total*100, 5), '%', sep='')



