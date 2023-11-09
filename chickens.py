
protein = {}

input_ = str(input())
input_1 = str(input())
array1 = input_.strip().split()
array2 = input_1.strip().split()
print(array1)
print(array2)
for i in range(len(array1)):
    if(array1[i] not in protein):
        protein[array1[i]] = [array2[i]]
    else:
        protein[array1[i]].append(array2[i])
        
       
gene_1 = str(input())
gene_1 = gene_1.upper()
gene_2 = str(input())
gene_2 = gene_2.upper()
gene_1 = list(gene_1)
gene_2 = list(gene_2)
if(len(gene_1) != len(gene_2)):
    print("No")
elif(gene_1 == gene_2):
    print("Yes")
else:
    for i in range(len(gene_1)):
        if(gene_1[i] ==  gene_2[i]):
            continue
        else:
            visited = []
            if(gene_1[i] in protein and protein[gene_1[i]][0] == gene_2[i]):
                gene_1[i] == protein[gene_1[i]][0]
            elif(gene_2[i] in protein and protein[gene_2[i]][0] == gene_1[i]):
                gene_2[i] == protein[gene_2[i]][0]
            else:
                if(gene_1[i] in protein):
                    x = 0
                    while(True):
                        key = protein[gene_1[i]][0]

                        if(key != gene_2[i][0]):
                            visited.append(key)
                        elif(key in visited):
                            pass
                        

print(gene_1==gene_2)

print(protein)
