# Miriam Baumann, 2015-11-10
# Reads in a dataframe in the form of a simple text file and 
# plots the mean of each column in the y- axis, and then saves the plot  

# import libraries
import pandas as pd
import sys
import matplotlib as plt

def main ():
# assign variables
	filename = sys.argv[1]
	savename = sys.argv[2]

	# load the data
	data = pd.read_csv(filename, delimiter=',')

	# call process to get values from data
	values = process(data)
	
def process(data):
	#Defining what to do with the dataframe
	data.mean(axis = 1)
	#return(out)
	
def plot(plot, data):	

	plt.plot(plot)
	#Saving the figure 
	plt.savefig(savename)
	
	plt.show()
	

main()