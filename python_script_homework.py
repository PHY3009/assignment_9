#Jhanelle Williams 10-11-2015
#Assignment 9
# The aim of this assignment is to create a python script which loads datasets, plot and save the figures

#import libraries that have tools to perform the desired functions

import sys
import pandas as pd
import matplotlib.pyplot as plt

def main():

	#assign variables
	input_file= sys.argv[1]
	output_file=sys.argv[2]
	#action=sys.argv[2]

	#load data
	sample_data=pd.read_csv(input_file, delimiter=',')

	#plot data
	plt.plot(sample_data)
	#show plot
	plt.savefig(output_file)
	plt.show()

main()
