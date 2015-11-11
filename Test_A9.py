# Jessica O'Sullivan, 2015-11-10
# This script is designed to save a plot of an input dataset.

#import libraries
import sys
import pandas as pd
import matplotlib.pyplot as plt


#set variables for data input and save file output name
input_file = sys.argv[1]
output_file = sys.argv[2]

#set dataframe as variable data
data = pd.read_csv(input_file, delimiter=',')
	
# plot the data and save as variable data_plot
plot = plt.plot(data)

#save the plot as a figure by the name input by user
plt.savefig(output_file)

#print message to let the user know its been saved
print ('Your figure has been saved.')














