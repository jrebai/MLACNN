import pandas as pd
import tensorflow as tf


import deepcpg.data.fasta
# from deepcpg.data import fasta

data = pd.read_csv('37.csv',header=None,sep='\t')
data.rename(columns={0:'a',1:'b',2:'c',3:'d'},inplace=True)
data['b'] = data['b'].apply(lambda x : 1 if round(x,1) >0.5 else 0)

# index = list(data.index)
# index = [i for i in index if i%2==0]
data = data[data.index%2==0]

data = data[data['c']!='X']
data = data[data['c']!='Y']

positive_data = data[data['b'] == 1]
negative_data = data[data['b'] == 0]

positive_data = positive_data.sample(n=len(negative_data))

total_table = positive_data.append(negative_data)
total_table = total_table.sample(frac=1)

total_table['d'] = 0
print(len(data))
print(len(positive_data))
print(len(negative_data))
print(len(total_table))

print(total_table)
print('total_table file arrangement done!!')

for i in range(1,22+1):
    respective_data = total_table[total_table['c'] == i]
    print(respective_data)
    respective_data.to_csv('even_table/table'+str(i)+'.tsv', sep='\t', header=None, index=False)

# table1.to_csv(target_forder+'seq_beta_table_' + str(chrom_num) + '.tsv', sep='\t', header=None, index=False)


#
# chrome_fold = '../modify_file_to_vector_base_cvs/raw_dna_seq/'
#
# chrome_list = list()
# for i in range(1,22+1):
#     chrome_list.append(fasta.read_chromo(chrome_fold + 'chromosome.' + str(i) + '.fa', i))
# print('chrome file read done!!')
# tf_chrome = tf.data.Dataset.from_tensor_slices(chrome_list)
# print(tf_chrome[1][:100])
#
# def map_function(vector):#vector 0,1,2,3分别是甲基化位点，甲基化值，chrome 和对应生成的向量
#
#     # chrome_str = fasta.read_chromo(chrome_fold + 'chromosome.' + str(vector[2].numpy()) + '.fa', int(vector[2].numpy()))
#     vector[4] = chrome_list[vector[2]][:20]
#
#
# tf_data = tf.data.Dataset.from_tensor_slices(total_table.values.astype(float))
#
# tf_data = tf_data.map(map_function)
# iters = tf_data.__iter__()
# print(iters.__next__())
# #
# #
# #
# # a = tf.constant([1,2,3,4,5,6])
# # print(a.numpy())


