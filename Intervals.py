#  File: Intervals.py

#  Description: Collapsing intervals

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/03/2021

#  Date Last Modified: 02/05/2021


import sys

def merge_tuples (tuples_list):
  tuples_list.sort()

  merged_list = [tuples_list[0]]

  for i in range(1, len(tuples_list)):
    if merged_list[-1][1] >= tuples_list[i][0]:
      new_tuple = (merged_list[-1][0], max(merged_list[-1][1], tuples_list[i][1]))
      merged_list[-1] = new_tuple
    else:
      merged_list.append(tuples_list[i])

  return merged_list

def delta(x):
  return (x[1] - x[0], x[0])

def sort_by_interval_size (tuples_list):
  # Input: tuples_list is a list of tuples of denoting intervals
  # Output: a list of tuples sorted by ascending order of the size of
  #         the interval
  #         if two intervals have the size then it will sort by the
  #         lower number in the interval
  new_list = sorted(tuples_list, key = delta)
  print(new_list)

def main():
  # open file intervals.in and read the data and create a list of tuples

  num_lines = 0
  lines = sys.stdin.readlines()
  for i in (0, len(lines)):
    if i == 0:
      num_lines = int(lines[0])
      lines.pop(0)
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  tuples_list = []
  for i in range(len(lines)):
    newlist = lines[i].split()
    tuples_list.append((int(newlist[0]), int(newlist[1])))
  # merge the list of tuples
  a = merge_tuples(tuples_list)
  print(a)
  # sort the list of tuples according to the size of the interval
  # write the output list of tuples from the two functions
  sort_by_interval_size(a)

if __name__ == "__main__":
  main()
