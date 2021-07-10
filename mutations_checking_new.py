# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:37:19 2020

@author: rubayet
"""
import pandas as pd
from pandas import DataFrame
import numpy as np
import glob
import os.path
from Bio import SeqIO

for a in SeqIO.parse (r'C:\Users\G-Tech\Desktop\ref_sars.fas', 'fasta'): 
    s1=a.seq

l=[]
f=glob.glob (r'C:\Users\G-Tech\Desktop\m\*.fasta') 
print(f)   
for d in f:   
    #print(d)
    mutations_c=0
    mutation_c_list=[]
    for b in SeqIO.parse (d,"fasta"):
        s2=b.seq
        
        for i,j in zip(s1,s2):
            
            if (i != j and 
                i not in ( '-', 'n', 'r', 'y', 'k', 'm', 's', 'w', 'b', 'd', 'v', 'h') and
                    j not in ( '-', 'n', 'r', 'y', 'k', 'm', 's', 'w', 'b', 'd', 'v', 'h')):          
                mutations_c+=1
                #mutation_c_list.append(mutations_c)
                #print(mutations_c_list)
        mutation_c_list.append(mutations_c-1)
    element_1=str(mutation_c_list[0]).split()
    
    diff_mutation_c_list = np.diff(mutation_c_list)
    list_diff_mutation_c_list=diff_mutation_c_list.tolist()
    final_mutation_c_list= element_1 + list_diff_mutation_c_list 
    #print (mutation_c_list)
    #print(diff_mutation_c_list)
    #print(list_diff_mutation_c_list)
    #print (type(list_diff_mutation_c_list))
    #print(final_mutation_c_list)         
    df=DataFrame(np.column_stack([final_mutation_c_list]), 
                                           columns=['mutation number'])
    df.to_excel ((os.path.join (r'C:\Users\G-Tech\Desktop\m', os.path.basename(d)) + ".xlsx"),'w+', header=True)
    excel=pd.read_excel((os.path.join (r'C:\Users\G-Tech\Desktop\m', os.path.basename(d)) + ".xlsx"))
    df1=pd.DataFrame(excel)
    
    mean=df1.mean(axis=0)[1]
    l.append(mean)
df2=DataFrame(np.column_stack([l]), 
                      columns=['average'])
df2.to_excel (r'C:\Users\G-Tech\Desktop\m\t_av.xlsx', 'sheet1', header=True, index=True)

    
    
    