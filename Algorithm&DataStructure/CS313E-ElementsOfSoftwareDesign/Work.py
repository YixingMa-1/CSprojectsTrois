
#  File: Work.py

#  Description: linear search and binary search

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/04/2021

#  Date Last Modified: 03/04/2021

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  i = 0
  sum = 0
  while v // (k**i) > 0:
      sum += v // (k**i)
      i = i + 1
  return sum
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  if n <= k:
    return n
  for v in range(n):
    sum = sum_series(v, k)
    if sum < n:
      continue
    if sum >= n:
      return v
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  low = 0
  high = n
  while high > low:
    mid = (high + low) // 2
    if sum_series(mid, k) < n:
      low = mid + 1
    elif sum_series(mid, k) >= n:
      high = mid
  return high


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  pass

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()
if __name__ == "__main__":
  main()
