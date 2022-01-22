import numpy as np
import logging

class CreateArray:
    
    def __init__(self, size, arr_type):
        logging.debug("CreateArray Class is initialized.")

        self.__size = int(size)
        self.__atype = arr_type.lower()
        
        #Create Array based on Type: Sorted, Reverse, Random
        if self.__atype == "sorted":
            self.__array = np.arange(1, self.__size+1)
        elif self.__atype == "reverse":
            self.__array = np.arange(self.__size, 0, -1)
        elif self.__atype == "random":
            np.random.seed(1)
            self.__array = np.random.randint(low=0, high=self.__size, size = self.__size+1)
        logging.info("Size of Array:{}, Type of Array: {} \n Array: {}".format(self.__size, self.__atype.upper(), self.__array))
        
    @property
    def create(self):
        return self.__array

    def __del__(self):
        logging.debug("CreateArray Class terminated successfully.")