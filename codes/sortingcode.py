import logging
import numpy as np
class BasicSort:

    def __init__(self, arr, sortfn):
        logging.debug("Sorting class is initialized.")
        self.__arr = arr
        self.__sortfn = sortfn.lower()

        if self.__sortfn == "insertsort":
            self.insertsort()
        elif self.__sortfn == "bubblesort":
            self.bubblesort()
        elif self.__sortfn == "mergesort":
            p = 0
            r = (len(self.__arr)-1)
            self.mergesort(p,r)
        elif self.__sortfn == "quicksort":
            p = 0
            r = (len(self.__arr)-1)
            self.quicksort(p,r)
        elif self.__sortfn == "pythonsort":
            self.pythonsort()
        elif self.__sortfn == "numpysort":
            self.numpysort()

    #Insert Sort
    def insertsort(self):
        logging.debug("Initializing InsertSort Function.")
        n = len(self.__arr)
        for i in range(1, n):
            key = self.__arr[i]
            j = i - 1
            while j >=0 and self.__arr[j] > key:
                self.__arr[j+1] = self.__arr[j]
                j = j - 1
            self.__arr[j+1] = key
        logging.debug("Sorted Array after InsertSort : {}".format(self.__arr))
        logging.debug("InsertSort Function completed successfully.")

    #Bubble Sort
    def bubblesort(self):
        logging.debug("Initializing BubbleSort Function.")
        n = len(self.__arr)
        for j in range(1, n):
            for i in range(0, n - 1):
                if self.__arr[i] > self.__arr[i+1]:
                    temp = self.__arr[i]
                    self.__arr[i] = self.__arr[i+1]
                    self.__arr[i+1] = temp
        logging.debug("Sorted Array after BubbleSort : {}".format(self.__arr))
        logging.debug("BubbleSort Function completed successfully.")

    # Merge Sort
    def mergesort(self, p, r):
        logging.debug("Initializing Merge Sort Function.")
        if p < r:
            q = (p + r) // 2  ##Double slash divides down to nearest whole number
            self.mergesort(p, q)
            self.mergesort(q + 1, r)
            self.merge(p, q, r)
        logging.debug("Sorted Array after MergeSort : {}".format(self.__arr))
        logging.debug("MergeSort Function completed successfully.")

    def merge(self, p, q, r):
        A = self.__arr
        n1 = q - p + 1
        n2 = r - q
        left = [0] * (n1 + 1)
        right = [0] * (n2 + 1)
        for i in range(0, n1):
            left[i] = A[p + i]
        for j in range(0, n2):
            right[j] = A[q + j + 1]
        left[n1] = float('inf')
        right[n2] = float('inf')
        i = 0
        j = 0

        for k in range(p, r + 1):
            if left[i] <= right[j]:
                A[k] = left[i]
                i = i + 1
            else:
                A[k] = right[j]
                j = j + 1

        # return A

    # Quick Sort
    def quicksort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quicksort(p, q - 1)
            self.quicksort(q + 1, r)
        logging.debug("Sorted Array after Quick Sort : {}".format(self.__arr))
        logging.debug("QuickSort Function completed successfully.")

    # Partition Function works with Quick Sort
    def partition(self, p, r):
        A = self.__arr
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                A[i], A[j] = A[j], A[i]

        A[i + 1], A[r] = A[r], A[i + 1]

        return i + 1


    # Python Default List Sort
    def pythonsort(self):
        logging.debug("Initializing Python Default List Sort Function.")
        self.__arr.sort()
        logging.debug("Sorted Array after Python-Default-Sort : {}".format(self.__arr))
        logging.debug("Python-Default-Sort Function completed successfully.")

    # Numpy Default Sort
    def numpysort(self):
        logging.debug("Initializing Numpy Sort Function.")
        self.__arr = np.asarray(self.__arr)
        self.__arr = np.sort(self.__arr)
        logging.debug("Sorted Array after Numpy Sort : {}".format(self.__arr))
        logging.debug("Numpy Sort Function completed successfully.")

    @property
    def sortedoutput(self):
        return self.__arr

    def __del__(self):
        logging.debug("Sorting Class terminated successfully.")
