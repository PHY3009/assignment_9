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

	#output data
	print(values)
	
	#Saving the figure 
	plt.savefig(savename)
	
def process(data):
	#Defining what to do with the dataframe
	out = data.mean(axis = 1)
	return out
		
#def plot(plot_data, savename):
	#plot data
	#plt.plot(plot_data)
	#save plot 
	#plt.savefig(savename)
	#show plot
	#plt.show()
	

main()