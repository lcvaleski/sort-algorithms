import mergeSort
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
print(f"Total sort time: {totalTime} seconds")

# Bubble sort

# Insertion sort

# Selection sort

# Quicksort