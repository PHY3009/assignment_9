# Miriam Baumann, 2015-11-10
# Reads in a dataframe in the form of a simple text file and 
# plots the mean of each column and then saves the plot  

# import libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt

#Defining the variables
filename = sys.argv[1]
savename = sys.argv[2]
	
#load the data using panadas
data = pd.read_csv(filename, delimiter=',')	
	
#Plotting the mean of each column of the data 
plt.plot(data)
	
#Saving the plot
plt.savefig(savename)