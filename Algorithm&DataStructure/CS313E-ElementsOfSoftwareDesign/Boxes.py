
#  File: Boxes.py

#  Description: boxes nested in another boxes

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/25/2021

#  Date Last Modified:03/26/2021
import sys
# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  hi = len(box_list)
  if (idx == hi):
    all_box_subsets.append(sub_set)
    return
  else:
    temp_subset = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, temp_subset, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  largest_subsets = []
  largest_size = 0
  for i in range(len(all_box_subsets)):
    boo = True
    for j in range(len(all_box_subsets[i]) - 1):
        if does_fit(all_box_subsets[i][j], all_box_subsets[i][j + 1]) is False:
          boo = False
          break
    if boo is True:
      if largest_size < len(all_box_subsets[i]):
        largest_size = len(all_box_subsets[i])
        largest_subsets.clear()
        largest_subsets.append(all_box_subsets[i])
      elif largest_size == len(all_box_subsets[i]):
        largest_subsets.append(all_box_subsets[i])
  return largest_subsets
# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])
def main():
  # read the number of boxes
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)
  # create an empty list for the boxes
  box_list = []
  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)
  # sort the box list
  box_list.sort()
  # print ("sorted box list", box_list)
  # print()
  # create an empty list to hold all subset of boxes
  all_box_subsets = []
  # create a list to hold a single subset of boxes
  sub_set = []
  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)
  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes
  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)
  # print the largest number of boxes that fit
  print(len(all_nesting_boxes[0]))
  # print the number of sets of such boxes
  print(len(all_nesting_boxes))
if __name__ == "__main__":
  main()
