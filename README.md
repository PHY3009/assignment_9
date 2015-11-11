## Script to automate plotting
###Isaac Menninga, 2015-11-10

This script is used to plot data in a simple line plot from an input .csv file. 

Usage:
python plot.py input_file output_file

input_file = The name of the input file containing data
output_file = The name of the file that the user wants to save the figure in. This creates a new file containing the figure, and should not be the name of an existing file. 

Data format:
	Input files should exclusively be .csv files with values delimited by commas. Output file is the name of the file that you want the plot to be saved to. This file should be .pdf to allow reformatting to occur after creation of the plot. 