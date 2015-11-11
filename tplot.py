# Kyle Fawkes,     2015-10-11

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import sys

# main function
def main():
	
	# applying sys to input data
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	
	#load data
	data = pd.read_csv(input_file, delimiter=',')
	
	# executing the time_series_plot fucntion
	plot=plt.plot(data.index[1:10], data.sig_wave_height[1:10])

	#showing the plot
	print(plot)
	
	# saving the plot as...
	plt.savefig(output_file)
	
main()
	

