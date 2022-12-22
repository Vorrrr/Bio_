minus, plus, protein_counter = 0, 0, 0
file = open(input(), 'r')
for i in file.readlines():
    strain, gene = i.split('\t')[9], i.split('\t')[1]
    if gene == 'with_protein':
        protein_counter += 1
        if strain == '+':
            plus += 1
        elif strain == '-':
            minus += 1
file.close()
print('+:', plus, '\n-:', minus,'\ntotal:',  protein_counter)
