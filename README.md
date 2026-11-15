# Merge Sort Algorithm in Python

A recursive implementation of the Merge Sort algorithm using the Divide and Conquer paradigm.

## Overview

Merge Sort is a comparison-based sorting algorithm that divides an unsorted list into smaller sublists, recursively sorts them, and merges them back together in ascending order.

## How It Works

The implementation consists of two main functions:

### 1. merge_sort()
- Divides the input list into two halves.
- Recursively sorts each half.
- Calls merge_sort() to combine the sorted sublists.

### 2. merge()
- Compares elements from the left and right sublists.
- Places elements in ascending order.
- Copies any remaining elements into the original list.

## Algorithm Complexity

| Case | Time Complexity |
| :--- | :--- |
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |

- Auxiliary Space Complexity: O(n)

## Features

- Recursive implementation.
- Divide and Conquer approach.
- Handles duplicate and negative values.
- Sorts the original list in place using auxiliary sublists.

## Requirements

- Python 3.x

## Usage

Run the following command:

python Merge.py
## Example

Input:
[2, 8, 3, 6, 1, 7, 3, 23, 12, 54, 375, 78, 34]
Output:
[1, 2, 3, 3, 6, 7, 8, 12, 23, 34, 54, 78, 375]
## Concepts Demonstrated

- Recursion
- Divide and Conquer
- Array manipulation
- Sorting algorithms
- Time and space complexity

## Author

Abdul Hamid Hosseini  
Software Engineering Student | AI & Machine Learning Enthusiast
