#T. Martz-Oberlander, 2015-11-11
#Script to read, plot, and save as .pdf for a data file


The main function of this file reads a datafile, plots the data, and saves a figure. Data files used here must be .csv. Additionally, all columns must have numbers in them, not letters or strings.

I attempted to add a 3rd argument to specify which columns of a given 'input_file' datafile to plot. This could be done with a "usecols=range(sys.argv[3])". I received too many errors and gave up.

Commands to enter:

argument 1 is the input file name. It must be stored in the same directory as teh script, or you must specify the absolute path

arg 2 is the name of the plot you want to save the figure as. The name you enter as the 2nd argument must be a [name].pdf


 


  
