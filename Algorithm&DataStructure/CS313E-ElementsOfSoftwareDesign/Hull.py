
#  File: Hull.py

#  Description: A convex hull is the smallest convex polygon that will enclose a set of points. we input many points \
# and output the vertices of the convex and compute the area of the convex.
#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/28/2021

#  Date Last Modified: 03/01/2021

import sys
import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)
# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  determinant = q.x * r.y - r.x * q.y - p.x * r.y + p.x * q.y + \
                p.y * r.x - p.y * q.x
  return determinant
# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
# Output: A list of point objects that define the vertices of the convex
#         hull in clockwise order.
# 1.  Sort the points by x-coordinates resulting in a sorted sequence
#     p_1 ... p_n.
# 2.  Create an empty list upper_hull that will store the vertices
#     in the upper hull.
  upper_hull = []
# 3.  Append the first two points p_1 and p_2 in order into the upper_hull.
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
# 4.  For i going from 3 to n
  for i in range(2, len(sorted_points)):
# 5.    Append p_i to upper_hull.
    upper_hull.append(sorted_points[i])
# # 6.    While upper_hull contains three or more points and the last three
# #       points in upper_hull do not make a right turn do (refer to the
# # 	  notes below on determinants for right and left interpretations)\
    while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1])>= 0:
# 7.    Delete the middle of the last three points from upper_hull
      upper_hull.pop(-2)
# 8.  Create an empty list lower_hull that will store the vertices
#     in the lower hull.
  lower_hull = []
# 9.  Append the last two points p_n and p_n-1 in order into lower_hull with
#     p_n as the first point.
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
# 10. For i going from n - 2 down to 1
  for i in range(len(sorted_points) - 3, 0, -1):
# 11.   Append p_i to lower_hull
    lower_hull.append(sorted_points[i])
# 12.   While lower_hull contains three or more points and the last three
#       points in the lower_hull do not make a right turn do
    while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) >= 0:
# 13.     Delete the middle of the last three points from lower_hull
      del lower_hull[-2]
# 14. Remove the first and last points for lower_hull to avoid duplication
#     with points in the upper hull.
  del lower_hull[0]
  del lower_hull[-1]
# 15. Append the points in the lower_hull to the points in the upper_hull
#     and call those points the convex_hull
  upper_hull.extend(lower_hull)
  convex_hull = upper_hull
# 16. Return the convex_hull.
  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  detplus = 0
  for i in range(len(convex_poly)):
    if i == len(convex_poly) - 1:
      detplus += convex_poly[i].x * convex_poly[0].y
    else:
      detplus += convex_poly[i].x * convex_poly[i + 1].y

  detminus = 0
  for i in range(len(convex_poly)):
    if i == len(convex_poly) - 1:
      detminus += convex_poly[i].y * convex_poly[0].x
    else:
      detminus += convex_poly[i].y * convex_poly[i + 1].x

  determinant = detplus - detminus
  return 0.5 * abs(determinant)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  pass

def main():
  # create an empty list of Point objects
  points_list = []
  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)
  # print(num_points)
  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    # print(line)
    x = int (line[0])
    y = int (line[1])
    points_list.append(Point(x,y))
  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)
  # print the sorted list of Point objects
  # get the convex hull
  m = convex_hull(sorted_points)
  # run your test cases
  # print your results to standard output
  # print the convex hull
  print('Convex Hull')
  for p in m:
    print(str(p))
  # get the area of the convex hull
  print()
  print('Area of Convex Hull =', area_poly(m))
  # print the area of the convex hull
if __name__ == "__main__":
  main()