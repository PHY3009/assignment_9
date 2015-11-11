# Billy Hung, 2015-11-10
# Load dataset and generate a useful plot

#import libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt


def main():

	# assign variables
	filename = sys.argv[1]
	save_path = sys.argv[2]

	# load the data
	data = pd.read_csv(filename, delimiter=',')
	
	# plot the dataset and save the plot
	plt.plot(data['MEAN'])
	plt.savefig(save_path)
	plt.show()
main()
