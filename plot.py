# Isaac Menninga, 2015-11-06
# Read in inflammation data and print the mean inflammation for each 
patient

#import libraries
import pandas as pd, sys, matplotlib.pyplot as plt

def main():
	#assign variables
	action = sys.argv[1]
	filename = sys.argv[2]
	save_path = sys.argv[3]

	#load the data
	data = pd.read_csv(filename, delimiter = ',')

	#call process to get values from action and data
	values = process(action, data)
	
	#print data
	plot(values, save_path)

def process(command, dataset):	
	#choose action depending on user input
	#if user input is '--min', find the min value for each patient
	if command == '--min':
		out = dataset.min(axis = 0)
		
	#if user input is '--max', find the max value for each patient
	elif command == '--max':
		out = dataset.max(axis = 0)
		
	#if user input is '--mean', find the mean value for each patient
	elif command == '--mean':
		out = dataset.mean(axis = 0)
	#else, output an error message
	else:
		print('Please enter a valid input for action. Valid 
inputs are: --min, --max, --mean')
	return out

def plot(plot_data, savename):
	#plot data
	plt.plot(plot_data)
	#save plot as savename
	plt.savefig(savename)
	#show fig
	plt.show()
	
main()
