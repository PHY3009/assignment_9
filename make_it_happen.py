# Nicholas Allan, 2015-11-10
# 

#import libraries
import pandas as pd 
import sys
import matplotlib.pyplot as plt

def main():
     
    #output variables
	output_file = sys.argv[2]
	#input variables 
	#action = sys.argv[1]
	input_file = sys.argv[1]

		#load the data
	data = pd.read_csv(input_file, delimiter = ',')
 
		#print data
	plot(data, output_file)


def plot(plot_data, savename):
        #plot data
	plt.plot(plot_data)
        #save the plot
	plt.savefig(savename)
        
main()
