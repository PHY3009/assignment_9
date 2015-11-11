# Isaac Menninga, 2015-11-06
# Read in inflammation data and print the mean inflammation for each patient

#import libraries
import pandas as pd, sys, matplotlib.pyplot as plt

def main():
	#assign variables
	action = sys.argv[1]
	filename = sys.argv[2]

	#load the data
	data = pd.read_csv(filename, delimiter = ',')
	
	#plot data
	plot(data, save_path)

def plot(plot_data, savename):
	#plot data
	plt.plot(plot_data)
	#save plot as savename
	plt.savefig(savename)
	#show fig
	plt.show()
	
main()
