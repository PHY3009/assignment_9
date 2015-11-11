#Sabrina DeSoto 11/11/15
#Assignment 9
#script that loads, plots and saves data files

def main():
	#imports
	import pandas as pd, matplotlib.pyplot as plt, sys 
	
	#set arguments
	data_to_plot = sys.argv[1]
	savepath = sys.argv[2]
	
	#load data
	data = pd.read_csv('data_to_plot', delimiter = ',')
	
	#plot data and save fig
	plt.plot(data)
	plt.savefig(savepath)
	plt.show()
	
main()
	