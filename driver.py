import mergeSort
import insertionSort
import selectionSort
import pandas as pd
import numpy as np
import math
import time
# Load titanic dataset
gender_data = pd.read_csv("./Titanic Data Set/gender_submission.csv")
train_data = pd.read_csv("./Titanic Data Set/train.csv")
test_data = pd.read_csv("./Titanic Data Set/test.csv")

# Place ages in a list
ages = list(train_data['Age']) + list(test_data['Age'])

# Filter out the people who didn't have ages listed
ages = [x for x in ages if not math.isnan(x)]

# Merge sort (func definition in mergeSort.py)
start = time.time()
print("Running merge sort on data")
mergeSort.mergeSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total merge sort time: {totalTime} seconds")

# Insertion sort

start = time.time()
print("Running insertion sort on data")
insertionSort.insertionSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total insertion sort time: {totalTime} seconds")

# Bubble sort

# Selection sort

start = time.time()
print("Running selection sort on data")
selectionSort.selectionSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total selection sort time: {totalTime} seconds")

# Quicksort