import numpy as np
import logging

class CreateArray:
    
    def __init__(self, __size, __atype):
        
        #Create Array based on Type: Sorted, Reverse, Random
        if __atype.lower() == "sorted":
            self.__array = np.arange(1, __size+1)
        elif __atype.lower() == "reverse":
            self.__array = np.arange(__size, 0, -1)
        elif __atype.lower() == "random":
            np.random.seed(1)
            self.__array = np.random.randint(low=0, high=__size, size = __size+1)
        
    def create(self):
        return self.__array