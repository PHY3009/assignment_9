#Sabrina DeSoto 11/11/15
#Assignment 9
#script that loads, plots and saves data files

def main():
	#imports
	import pandas as pd, matplotlib.pyplot as plt, sys 
	
	#set arguments
	input_file = sys.argv[1]
	output_file= sys.argv[2]
	
	#load data
	data = pd.read_csv(input_file, delimiter = ',')
	
	#plot data and save fig
	plt.plot(data)
	plt.savefig(output_file)
	plt.show()
	
main()
	