# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt



total_pr = 0
total_rna = 0
file = open(input(), 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if gene == 'with_protein':
        total_pr += 1
    if 'RNA' in gene:
        total_rna += 1
        
file.close()
print('RNA total: ', total_rna, '\nRNA/protein = ', str(round(total_rna/total_pr, 5)))


