import pandas as pd
import sys
import matplotlib.pyplot as plt
input_file = sys.argv[1]
output_file =  sys.argv[2]
nucleotide_data = pd.read_csv(input_file, delimiter=',')
input_file = nucleotide_data
nucleotide_data[['A', 'T', "C" ,'G']].boxplot()
plt.ylabel('number of base in CRISPR spacers')
plt.xlabel('bases')
plt.title('CRISPR spacer beginning nucleotide distribution')
output_file = 'spacer_graph'
plt.savefig('output_file')
