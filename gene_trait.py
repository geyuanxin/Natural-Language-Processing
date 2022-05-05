#%%
import pandas as pd
import numpy as np

gene_trait = np.load('/home/yxge/nlp/gene_trait.npy',allow_pickle=True)
pair = np.empty(shape=(0,2))
for i in range(0, 860):
    one = list(gene_trait[i].items())
    one_gene = one[0][1]
    one_trait = one[1][1]
    one_gene_trait = np.array([(a,b) for a in one_gene for b in one_trait])
    pair = np.concatenate((pair,one_gene_trait),axis=0)

pair = pd.DataFrame(pair)
pair.to_csv('/home/yxge/nlp/gene_trait.txt', sep='\t',header=None,index=False)

