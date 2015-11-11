
# coding: utf-8

# In[5]:
"""I didnt get too creative here"""


#import libraries
import pandas as pd
import sys
import matplotlib.pyplot as plt
#defining the main function which defines the variables, loads the data, the variable functions that process the data.

def main ():
        
        #assign variables
        action = sys.argv[1]
        filename = sys.argv[2]
        save_path = sys.argv[3]
        
        #load the data
        data = pd.read_csv(filename, delimiter=',')
        
        # call process to get values from action and data
        values = process(action, data)
        plot = data_plot(action, data)
        
        #output data
        print (values)
        print (data_plot)
        
        #save figure
        plt.savefig(save_path)

def process (command, dataframe):
        #create a command where you can choose the processing method you want depending on user input
        if command == '--min':
                out = dataframe.min(axis=1)
        elif command == '--max':
                out = dataframe.max(axis=1)
        elif command == '--mean':
                out = dataframe.mean(axis=1)
        else:
                "Please specify if you would like the min, mean or max values for the data"
        
def data_plot (command, dataframe):
       
        #plot the data
        if command == '--min':
                plot = plt.plot(dataframe.min(axis=1))
        elif command == '--max':
                plot = plt.plot(dataframe.max(axis=1))
        elif command == '--mean':
                plot = plt.plot(dataframe.mean(axis=1))
        
main()

# In[6]:




# In[7]:




# In[8]:




# In[15]:




# In[ ]:



