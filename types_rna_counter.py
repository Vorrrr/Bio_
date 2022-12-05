r_rna = 0
t_rna = 0
oth = ''
total = 0
file = open('C:\Надя\GCF_013343195.2_ASM1334319v3_feature_table.txt', 'r')
for i in file.readlines():
    i = i.split('\t')
    gene = i[1]
    if 'rRNA' in gene:
        r_rna += 1
        total += 1
    elif 'tRNA' in gene:
        t_rna += 1
        total += 1
    elif 'RNA' in gene and 'RNase' not in gene:
        oth += str(gene) + ', '
        total += 1
        
file.close()
print('Total RNA:', total)
print('rRNA:', r_rna)
print('tRNA:', t_rna)
print('Other:', oth[:-2])

