import mergeSort
import insertionSort
import selectionSort
import bubbleSort
import quickSort
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
print("###############################################")
start = time.time()
print("Running merge sort on data")
mergeSort.mergeSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total merge sort time: {totalTime} seconds")
print("###############################################")


# Insertion sort

start = time.time()
print("Running insertion sort on data")
insertionSort.insertionSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total insertion sort time: {totalTime} seconds")
print("###############################################")


# Bubble sort

start = time.time()
print("Running bubble sort on data")
bubbleSort.bubbleSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total bubble sort time: {totalTime} seconds")
print("###############################################")

# Selection sort

start = time.time()
print("Running selection sort on data")
selectionSort.selectionSort(ages)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total selection sort time: {totalTime} seconds")
print("###############################################")


# Quick sort

start = time.time()
print("Running quick sort on data")
quickSort.quickSort(ages, 0, len(ages) - 1)
end = time.time()
totalTime = round((end - start), 5)
print(f"Total quick sort time: {totalTime} seconds")
print("###############################################")
