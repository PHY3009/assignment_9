# T. Martz-Oberlander, 2015-11-11
# Script to read an input_file,
# create a plot with the data,
# and save the plot as a .pdf document

#NOTE: this script only reads all columns of .csv data files 
#files need to have all columns have numbers--DateTime columns don't work


#Import libraries
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():
	# assign variables
	output_file = sys.argv[2]
	input_file = sys.argv[1]
	#columns = sys.argv[3]

#load the data 
	data = pd.read_csv(input_file, delimiter = ',')
    
#print data
	plt.plot(data) #, usecols=range(columns)

#save plot
	plt.savefig(output_file)

#show plot
	plt.show(output_file)

#close main function
main()




