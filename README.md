plot_data.sh

This script is executed by typing python plot_data.sh (data name) (save name) into the 
terminal that is opened to the same area as the data. The bracket inputs are the two 
arguments the script takes. The script is headed with a def main(): which holds 
the commands it executes. First the scipt imports the libraries. Next it defines the 
arguments, of which the first argument is the data file the user desires to plot and the 
second is that filename the plot will be saved as. Then the data is loaded as a csv, 
using pandas. The last command is to plot the data using matplotlib and to save/show the
figure. Finally the script is completed by calling main(). 