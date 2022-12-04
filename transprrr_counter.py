# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


transp_cou = 0
total = 0
file = open('C:\Надя\GCF_013343195.2_ASM1334319v3_feature_table.txt', 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if gene == 'with_protein':
        if 'transporter' in i[13]:
            transp_cou += 1
        total += 1
        
file.close()
print('Transporters: ', transp_cou, '\nPercentage - ', str(round(transp_cou/total * 100, 5)) + '%')
