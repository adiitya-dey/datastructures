
from statistics import mean
import timeit, time
import logging
import pandas as pd
import json
import matplotlib.pyplot as plt
from .createarray import CreateArray
from .sortingcode import BasicSort
import os
from matplotlib.scale import LogScale
import sys

# Increase Recursion Limit from Default Value = 1000 to New Value = 9999999
# Recursion Limit needs to be increased for Recursive Sorting(Merge and Quick Sort).
sys.setrecursionlimit(9999999)

# Declare logging configuration values.
# Note: Change "level=logging.INFO" to "level=logging.DEBUG" to trace all activities.
logging.basicConfig(filename='application.log', filemode = 'a', format='%(process)d-%(levelname)s-%(asctime)s - %(message)s', level=logging.DEBUG)


class Sorting:


    def start(self):

        # If the directory "figures" does not exist, create the directory. All csv and png files will be stored here.
        if os.path.isdir('figures') == False :
            logging.info("figures directory not found. Creating dir...")
            os.mkdir('figures')
        path = 'figures'
       
       # Exponent list consists of exponents for the power of 2 which will determine the size of array.
       # Ex: 2**2, 2**4,... etc.     
        __exponent_list = [2,4,6,8,10,12]
    
        # Types of Arrays to use for Sorting are Sorted Arrays, Reversed Arrays and Pseudo-Random Arrays.
        __array_category = ['Sorted', 'Reverse', 'Random']

        # List the types of sorting functions to test.
        # Note: Only add those types for which functions have been declared in BasicSort Class.
        __sorting_types = ['Insertsort', 'BubbleSort']

        # Intialize dictionary to store timings for each Array size and Sorting function.
        # Ex: outputdict = {'Size': 4, 'Insertsort': 0.000386, 'BubbleSort': 0.000422}
        __outputdict = {}

        for __category in __array_category:
            # Intialize list to capture all output values for the Array Category.
            # Ex: Sorted outputlist = [{'Size': 4, 'Insertsort': 0.000386, 'BubbleSort': 0.000422}, \
            # {'Size': 16, 'Insertsort': 0.000627, 'BubbleSort': 0.00137}]
            __outputlist = []
            for __ex in __exponent_list:
                # Declare size of array.
                __arraysize = 2**__ex
                __outputdict['Size'] =__arraysize
                for sorttype in __sorting_types:
                    # Create new array based on array category(Ex: Random,etc.) and array size(Ex: 2**4, 2**8, etc.).
                    newarray = CreateArray(__arraysize, __category).create()
                    stmt_to_run = 'BasicSort(newarray.copy(),sorttype)'
                    # Timeit function runs the sorting function 5 times, and repeat the operation 5 times. \
                    # Out of the 5 repeated timings calculated, minimum timing among them is chosen.
                    average_time = mean(timeit.repeat(stmt = stmt_to_run, repeat=5, number=5, 
                    globals={'BasicSort': globals().get('BasicSort'),'newarray':locals().get('newarray'),
                    'sorttype': locals().get('sorttype')}))
                    __outputdict[sorttype] = average_time
                __outputlist.append(__outputdict.copy())
                logging.debug("{} Output List: {}".format(__category, __outputlist))

            # Output of the timings calculated for each Array category is converted to json format.
            # Note: Keeping information in json format can assist in future if the output needs to shared with other applications.
            __jsonoutput = json.dumps(__outputlist)
            logging.debug("Conversion of outputlist to Json: \n {}".format(__jsonoutput))

            # Json value is converted to Pandas Dataframe to save in csv format.
            dataframe = pd.read_json(__jsonoutput).set_index('Size')
            logging.debug("{} Dataframe created. Dataframe values are: \n {}".format(__category, dataframe))

            # Declaring filesnames for csv and png for storing in figures Directory.
            t = time.localtime()
            timestamp = time.strftime('%b-%d-%Y_%H%M', t)
            csvfilename = 'array_' + __category.lower() + '_' + timestamp + '.csv'
            csvfilename = os.path.join(path,csvfilename)
            plotfilename = 'array_' + __category.lower() + '_' + timestamp + '.png'
            plotfilename = os.path.join(path, plotfilename)
            logging.debug("CSV File name created is {}. PNG filename created is {}".format(csvfilename, plotfilename))

            # Store Pandas Dataframe as csv file in figures Directory.
            # Ex: figures\array_reverse_Oct-22-2021_2103.csv
            dataframe.to_csv(csvfilename, sep=';')
            logging.info("{} Dataframe is converted to CSV successfully and stored in {}.".format(__category, csvfilename))

            # Declare configurations for pyplot function.
            params = {
                'axes.labelsize': 10,
                'axes.titlesize': 14,
                'legend.fontsize': 10,
                'xtick.labelsize': 10,
                'ytick.labelsize': 10

            }

            plt.rcParams.update(params)
            plt.figure(figsize=(8,6))
            plt.plot(dataframe, marker='o')
            plt.legend(dataframe.columns, loc=0)
            plt.xscale(LogScale(axis=1,base=2))
            plt.yscale(LogScale(axis=1, base=10))
            plt.xlabel("Array Size -->")
            plt.ylabel("Time (seconds) -->")
            plt.grid()
            plt.title("Comparisions between {} Arrays".format(__category))

            # Store plotted graph as png file in figures Directory.
            # Ex: figures\array_reverse_Oct-22-2021_2103.png
            plt.savefig(plotfilename)
            logging.info("Plot for {} is converted to PNG successfully and stored in {}.".format(__category, plotfilename))

            logging.info("All CSV and PNG files creation is completed. All operations are completed succesfully.")
