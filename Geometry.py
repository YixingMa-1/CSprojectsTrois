#  File: Geometry.py

#  Description: Develop several classes in Solid Geometry - Point, Sphere, Cube, and Cylinder.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/08/2021

#  Date Last Modified: 02/12/2021


import math
import sys

class Point (object):

  # constructor with default values
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
    self.x = x
    self.y = y
    self.z = z
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__(self):
    return str('(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + ')')
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2 + abs(self.z - other.z) ** 2) ** 0.5
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__(self, other):
    tol = 1.0e-6
    return ((abs(self.x - other.x) < tol)) and ((abs(self.y - other.y) < tol)) and ((abs(self.z - other.z) < tol))


class Sphere (object):
  # constructor with default values
  def __init__(self, x=  0.0, y =  0.0, z =  0.0, radius = 1.0):
    self.center = Point(x, y, z)
    self.radius = radius
    self.cube_left_up_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                     self.center.z + self.radius)
    self.cube_left_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                       self.center.z - self.radius)
    self.cube_left_up_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                    self.center.z + self.radius)
    self.cube_left_down_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                      self.center.z - self.radius)
    self.cube_right_up_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                      self.center.z + self.radius)
    self.cube_right_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                        self.center.z + self.radius)
    self.cube_right_up_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                     self.center.z + self.radius)
    self.cube_right_down_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                       self.center.z - self.radius)

  def list_cube_outside_sphere(self):
    cube_left_up_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                          self.center.z + self.radius)
    cube_left_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                            self.center.z - self.radius)
    cube_left_up_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                         self.center.z + self.radius)
    cube_left_down_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                           self.center.z - self.radius)
    cube_right_up_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                           self.center.z + self.radius)
    cube_right_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                             self.center.z + self.radius)
    cube_right_up_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                          self.center.z + self.radius)
    cube_right_down_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                            self.center.z - self.radius)
    cube_outside_sphere = [cube_left_up_front_point, cube_left_down_front_point, cube_left_up_back_point, cube_left_down_back_point, cube_right_up_front_point,
                           cube_right_down_front_point,  cube_right_up_back_point, cube_right_down_back_point]
    return cube_outside_sphere
      # returns string representation of a Sphere of the form:
      # Center: (x, y, z), Radius: value
  def __str__(self):
    # self.center = float(center)
    return 'Center: ' + str(self.center.__str__()) + ', ' + 'Radius: ' + str(float(self.radius))
#   # compute surface area of Sphere
#   # returns a floating point number
  def area (self):
    return 4 * math.pi * self.radius ** 2
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return 4 / 3 * math.pi * self.radius ** 3
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    dist = p.distance(self.center)
    if (dist < self.radius):
      return True
    return False
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    dist = self.center.distance(other.center)
    return (self.radius > (other.radius + dist))
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    dist = self.center.distance(a_cube.center)
    hypot_half = (((a_cube.side ** 2) + (a_cube.side ** 2)) ** 0.5) / 2
    return (self.radius >= dist + hypot_half)
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    if abs(self.radius) > abs(self.center.x - a_cyl.center.x - a_cyl.radius) and abs(self.radius) > abs(
            self.center.y - a_cyl.center.y - a_cyl.radius) and abs(self.radius) > abs(
            self.center.z - a_cyl.center.z - .5 * a_cyl.height):
      return True
    return False
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    if self.is_inside_sphere(other) is True:
      return False
    if other.is_inside_sphere(self) is True:
      return False
    dist = self.center.distance(other.center)
    return dist < (self.radius + other.radius)
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
    if (self.is_inside_cube(a_cube) is True) or (a_cube.is_inside_sphere(self) is True):
      return False
    temp1 = a_cube.list_cube_points()
    for i in range(8):
      if self.is_inside_point(temp1[i]) is True:
        return True
    front = (self.center.x + self.radius, self.center.y, self.center.z)
    back = (self.center.x - self.radius, self.center.y, self.center.z)
    left = (self.center.x, self.center.y - self.radius, self.center.z)
    right = (self.center.x, self.center.y + self.radius, self.center.z)
    down = (self.center.x, self.center.y, self.center.z - self.radius)
    up = (self.center.x, self.center.y, self.center.z + self.radius)
    temp2 = [front, back, left, right, down, up]
    for i in range(8):
      if a_cube.is_inside_point[temp2[i]]:
        return True
    return False
#   # return the largest Cube object that is circumscribed
#   # by this Sphere
#   # all eight corners of the Cube are on the Sphere
#   # returns a Cube object
  def circumscribe_cube (self):
    self.side = self.radius * (2 / math.sqrt(3))
    return Cube(self.center.x, self.center.y, self.center.z, self.side)

class Cube (object):
#   # Cube is defined by its center (which is a Point object)
#   # and side. The faces of the Cube are parallel to x-y, y-z,
#   # and x-z planes.
  def __init__ (self, x =  0.0, y =  0.0, z =  0.0, side = 1.0):
    self.center = Point(x, y, z)
    self.side = side
    self.cube_left_up_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                          self.center.z + 0.5 * self.side)
    self.cube_left_down_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                            self.center.z - 0.5 * self.side)
    self.cube_left_up_back_point = Point(self.center.x + 0.5 * self.side, self.center.y - 0.5 * self.side,
                                         self.center.z + 0.5 * self.side)
    self.cube_left_down_back_point = Point(self.center.x + 0.5 * self.side, self.center.y - 0.5 * self.side,
                                           self.center.z - 0.5 * self.side)
    self.cube_right_up_front_point = Point(self.center.x - 0.5 * self.side, self.center.y + 0.5 * self.side,
                                           self.center.z + 0.5 * self.side)
    self.cube_right_down_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                             self.center.z + 0.5 * self.side)
    self.cube_right_up_back_point = Point(self.center.x + 0.5 * self.side, self.center.y + 0.5 * self.side,
                                          self.center.z + 0.5 * self.side)
    self.cube_right_down_back_point = Point(self.center.x + 0.5 * self.side, self.center.y + 0.5 * self.side,
                                            self.center.z - 0.5 * self.side)
  def list_cube_points(self):
    cube_left_up_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                          self.center.z + 0.5 * self.side)
    cube_left_down_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                            self.center.z - 0.5 * self.side)
    cube_left_up_back_point = Point(self.center.x + 0.5 * self.side, self.center.y - 0.5 * self.side,
                                         self.center.z + 0.5 * self.side)
    cube_left_down_back_point = Point(self.center.x + 0.5 * self.side, self.center.y - 0.5 * self.side,
                                           self.center.z - 0.5 * self.side)
    cube_right_up_front_point = Point(self.center.x - 0.5 * self.side, self.center.y + 0.5 * self.side,
                                           self.center.z + 0.5 * self.side)
    cube_right_down_front_point = Point(self.center.x - 0.5 * self.side, self.center.y - 0.5 * self.side,
                                             self.center.z + 0.5 * self.side)
    cube_right_up_back_point = Point(self.center.x + 0.5 * self.side, self.center.y + 0.5 * self.side,
                                          self.center.z + 0.5 * self.side)
    cube_right_down_back_point = Point(self.center.x + 0.5 * self.side, self.center.y + 0.5 * self.side,
                                            self.center.z - 0.5 * self.side)
    cube_points = [cube_left_up_front_point, cube_left_down_front_point, cube_left_up_back_point, cube_left_down_back_point,
                   cube_right_up_front_point, cube_right_down_front_point, cube_right_up_back_point,cube_right_down_back_point]
    return cube_points

#   # string representation of a Cube of the form:
#   # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: ' + self.center.__str__() + ', ' + 'Side: ' + str(float(self.side))
#   # compute the total surface area of Cube (all 6 sides)
#   # returns a floating point number
  def area (self):
    return 6 * self.side ** 2
#   # compute volume of a Cube
#   # returns a floating point number
  def volume (self):
    return self.side ** 3
#   # determines if a Point is strictly inside this Cube
#   # p is a point object
#   # returns a Boolean
  def is_inside_point (self, p):
    if (self.center.x - self.side * 0.5) < p.x < (self.center.x + self.side * 0.5):
      if (self.center.y - self.side * 0.5) < p.y < (self.center.y + self.side * 0.5):
        if (self.center.z - self.side * 0.5) < p.z < (self.center.z + self.side * 0.5):
          return True
    return False
#   # determine if a Sphere is strictly inside this Cube
#   # a_sphere is a Sphere object
#   # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    temp = a_sphere.list_cube_outside_sphere()
    for i in range(8):
      if self.is_inside_point(temp[i]) is False:
        return False
    return True
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    temp1 = other.list_cube_points()
    for i in range(8):
      if self.is_inside_point(temp1[i]) is False:
        return False
    return True
#   # determine if a Cylinder is strictly inside this Cube
#   # a_cyl is a Cylinder object
#   # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
    temp = a_cyl.list_rec_outside_cyl()
    for i in range(8):
      if self.is_inside_point(temp[i]) is False:
        return False
    return True
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def cube_outside_cube(self, other):
    if (self.center.y + self.side * 0.5) - (other.center.y - other.side * 0.5) <= 0:
      return True
    if (self.center.z + self.side * 0.5) - (other.center.z - other.side * 0.5) <= 0:
      return True
    if (self.center.x + self.side * 0.5) - (other.center.x - other.side * 0.5) <= 0:
      return True
    return False

  def does_intersect_cube (self, other):
    if self.is_inside_cube(other) is True or other.is_inside_cube(self) is True:
      return False
    if self.cube_outside_cube(other) is True or other.cube_outside_cube(self) is True:
      return False
    return True

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    if self.does_intersect_cube(other) is False:
      return 0
    y_left = max((self.center.y - self.side * 0.5),(other.center.y - other.side * 0.5))
    y_right = min((self.center.y + self.side * 0.5), (other.center.y + other.side * 0.5))
    x_front = max((self.center.x - self.side * 0.5), (other.center.x - other.side * 0.5))
    x_back = min((self.center.x + self.side * 0.5), (other.center.x + other.side * 0.5))
    z_down = max((self.center.y - self.side * 0.5),(other.center.y - other.side * 0.5))
    z_up = min((self.center.x + self.side * 0.5), (other.center.x + other.side * 0.5))
    y_interval = y_right - y_left
    x_interval = x_back - x_front
    z_interval = z_up - z_down
    volume = y_interval * x_interval * z_interval
    return volume

#   # return the largest Sphere object that is inscribed
#   # by this Cube
#   # Sphere object is inside the Cube and the faces of the
#   # Cube are tangential planes of the Sphere
#   # returns a Sphere object
  def inscribe_sphere (self):
    InscribedSphere = Sphere(self.center.x, self.center.y, self.center.z, (self.side * .5))
    return InscribedSphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x =  0.0, y =  0.0, z = 0.0, radius = 1.0, height = 1.0):
    self.center = Point(x, y, z)
    self.radius = radius
    self.height = height
    self.rec_left_up_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                         self.center.z + self.height * 0.5)
    self.rec_left_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                           self.center.z - self.height * 0.5)
    self.rec_left_up_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                        self.center.z + self.height * 0.5)
    self.rec_left_down_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                          self.center.z - self.height * 0.5)
    self.rec_right_up_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                          self.center.z + self.height * 0.5)
    self.rec_right_down_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                            self.center.z - self.height * 0.5)
    self.rec_right_up_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                         self.center.z + self.height * 0.5)
    self.rec_right_down_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                           self.center.z - self.height * 0.5)
  def list_rec_outside_cyl(self):

    rec_left_up_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                       self.center.z + self.height * 0.5)
    rec_left_down_front_point = Point(self.center.x - self.radius, self.center.y - self.radius,
                                       self.center.z - self.height * 0.5)
    rec_left_up_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                    self.center.z + self.height * 0.5)
    rec_left_down_back_point = Point(self.center.x + self.radius, self.center.y - self.radius,
                                      self.center.z - self.height * 0.5)
    rec_right_up_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                      self.center.z + self.height * 0.5)
    rec_right_down_front_point = Point(self.center.x - self.radius, self.center.y + self.radius,
                                        self.center.z - self.height * 0.5)
    rec_right_up_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                     self.center.z + self.height * 0.5)
    rec_right_down_back_point = Point(self.center.x + self.radius, self.center.y + self.radius,
                                       self.center.z - self.height * 0.5)
    rec_ouside_cyl = [rec_left_up_front_point, rec_left_down_front_point, rec_left_up_back_point, rec_left_down_back_point,
                      rec_right_up_front_point, rec_right_down_front_point, rec_right_up_back_point, rec_right_down_back_point]
    return rec_ouside_cyl

  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return (
      'Center: ' + self.center.__str__() + ', Radius: ' + str(float(
        self.radius)) + ', Height: ' + str(float(self.height)))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * self.radius
#   # compute volume of a Cylinder
#   # returns a floating point number
  def volume (self):
    return math.pi * self.radius * self.radius * self.height
#   # determine if a Point is strictly inside this Cylinder
#   # p is a Point object
#   # returns a Boolean
  def is_inside_point (self, p):
    if abs(p.x - self.center.x) >= self.radius:
      return False
    if abs(p.y - self.center.y) >= self.radius:
      return False
    if abs(p.z - self.center.z) >= self.height * .5:
      return False
    return True
#   # determine if a Sphere is strictly inside this Cylinder
#   # a_sphere is a Sphere object
#   # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    horizontal_distance = math.sqrt((self.center.x - a_sphere.center.x)**2 + (self.center.y - a_sphere.center.y) ** 2)
    top_point_sphere = a_sphere.center.z + a_sphere.radius
    low_point_sphere = a_sphere.center.z - a_sphere.radius
    top_point_cylinder = self.center.z + self.height * 0.5
    low_point_cylinder = self.center.z - self.height * 0.5
    if horizontal_distance + a_sphere.radius < self.radius:
      if max(top_point_cylinder,top_point_sphere) == top_point_cylinder and min(low_point_cylinder,low_point_sphere) == low_point_cylinder:
        return True
    else:
      return False
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    top_point_cube = a_cube.center.z + a_cube.side * 0.5
    low_point_cube = a_cube.center.z - a_cube.side * 0.5
    top_point_cylinder = self.center.z + self.height * 0.5
    low_point_cylinder = self.center.z - self.height * 0.5
    leftfront = math.sqrt((self.center.y - (a_cube.center.y - a_cube.side * 0.5)) ** 2 + (self.center.x - (a_cube.center.x - a_cube.side * 0.5)) ** 2)
    rightfront = math.sqrt((self.center.y - (a_cube.center.y + a_cube.side * 0.5)) ** 2 + (self.center.x - (a_cube.center.x - a_cube.side * 0.5)) ** 2)
    leftback = math.sqrt((self.center.y - (a_cube.center.y - a_cube.side * 0.5)) ** 2 + (self.center.x - (a_cube.center.x + a_cube.side * 0.5))** 2)
    rightback = math.sqrt((self.center.y - (a_cube.center.y + a_cube.side * 0.5)) ** 2 + (self.center.x - (a_cube.center.x + a_cube.side * 0.5)) ** 2)
    if max(top_point_cylinder, top_point_cube) == top_point_cube or min(low_point_cylinder,low_point_cube) == low_point_cube:
      return False
    else:
      if leftfront < self.radius and rightfront < self.radius and leftback < self.radius and rightback < self.radius:
        return True
      else:
        return False
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    top_point_scylinder = self.center.z + 0.5 * self.height
    low_point_scylinder = self.center.z - 0.5 * self.height
    top_point_ocylinder = other.center.z + 0.5 * other.height
    low_point_ocylinder = other.center.z - 0.5 * other.height
    circlecenter_distance = math.sqrt((self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2)
    if max(top_point_scylinder, top_point_ocylinder) == top_point_ocylinder or min(low_point_ocylinder,low_point_scylinder) == low_point_ocylinder:
      return False
    else:
      if circlecenter_distance + other.radius < self.radius:
        return True
      else:
        return False
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    if self.is_inside_cylinder(other) is True or other.is_inside_cylinder(self) is True:
      return False
    if (self.radius - other.radius) ** 2 <= (self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2 <= \
            (self.radius + other.radius) ** 2:
      if (other.center.z - other.height * 0.5) <= (self.center.z - self.height * 0.5) <= (other.center.z + other.height * 0.5):
        return True
      elif (self.center.z - self.height * 0.5) <= (other.center.z - other.height * 0.5) <= (self.center.z + self.height * 0.5):
        return True
    return False



def main():
  # read data from standard input
  lines = sys.stdin.readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
  tuple_list = []
  for i in range(0, len(lines)):
    newlist = lines[i].split()
    if len(newlist) == 4:
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2]), float(newlist[3])))
    elif len(newlist) == 5:
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2]), float(newlist[3]), float(newlist[4])))
    elif len(newlist) == 3:
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2])))
    elif (newlist[3] != '#' and newlist[4] == '#'):
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2]), float(newlist[3])))
    elif (newlist[3] != '#' and newlist[4] != '#' and newlist[5] == '#'):
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2]), float(newlist[3]), float(newlist[4])))
    else:
      tuple_list.append((float(newlist[0]), float(newlist[1]), float(newlist[2])))
  # print(tuple_list)
  # read the coordinates of the first Point p
  P = Point()
  (P.x, P.y, P.z) = tuple_list[0]
  # print('P.x:',P.x,'P.y:', P.y,'P.z:', P.z)
  # # create a Point object
  Q = Point()
  # # read the coordinates of the second Point q
  (Q.x, Q.y, Q.z) = tuple_list[1]
  # print('Q.x:',Q.x,'Q.y:', Q.y,'Q.z:', Q.z)
  # # create a Point object
  sphereA = Sphere()
  # # # # read the coordinates of the center and radius of sphereA
  (sphereA.x, sphereA.y, sphereA.z, sphereA.radius) = tuple_list[2]
  # # # create a Sphere object
  # print('sphereA_center.x:', sphereA.x, 'sphereA_center.y:', sphereA.y, 'sphereA_center.z:', sphereA.z, 'sphereA.radius:', sphereA.radius)
  # read the coordinates of the center and radius of sphereB
  # create a Sphere object
  sphereB = Sphere()
  (sphereB.x, sphereB.y, sphereB.z, sphereB.radius) = tuple_list[3]
  # print('sphereB_center.x:', sphereB.x, 'sphereB_center.y:', sphereB.y, 'sphereB_center.z:', sphereB.z, 'sphereB.radius:', sphereB.radius)
  # read the coordinates of the center and side of cubeA
  cubeA = Cube()
  # create a Cube object
  (cubeA.x, cubeA.y,cubeA.z, cubeA.side) = tuple_list[4]
  # print('cubeA_center.x:', cubeA_center.x,'cubeA_center.y:', cubeA_center.y,'cubeA_center.z:', cubeA_center.z,'cubeA_center.side:', cubeA_center.side)
  # read the coordinates of the center and side of cubeB
  cubeB = Cube()
  (cubeB.x, cubeB.y,cubeB.z, cubeB.side) = tuple_list[5]
  # print('cubeB_center.x:', cubeB_center.x,'cubeB_center.y:', cubeB_center.y,'cubeB_center.z:', cubeB_center.z,'cubeB_center.side:', cubeB_center.side)
  # read the coordinates of the center, radius and height of cylA
  cylA= Cylinder()
  (cylA.x, cylA.y, cylA.z, cylA.radius, cylA.height) = tuple_list[6]
  # print('cylA_center.x:', cylA_center.x, 'cylA_center.y:', cylA_center.y,'cylA_center.z:', cylA_center.z, 'cylA_center.radius:', cylA_center.radius, 'cylA_cetner.height:', cylA_center.height)
  # create a Cylinder object
  # read the coordinates of the center, radius and height of cylB
  cylB = Cylinder()
  (cylB.x, cylB.y, cylB.z, cylB.radius, cylB.height) = tuple_list[7]
  # print('cylB_center.x:', cylB_center.x, 'cylB_center.y:', cylB_center.y,'cylB_center.z:', cylB_center.z, 'cylB_center.radius:', cylB_center.radius, 'cylB_cetner.height:', cylB_center.height)
  # create a Cylinder object
  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  origin = Point(0, 0, 0)
  if P.distance(origin) > Q.distance(origin):
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
  # print if Point p is inside sphereA
  if sphereA.is_inside_point(P) is True:
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')
  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB) is True:
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA) is True:
    print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cylA) is True:
    print('cylA is inside sphereA')
  else:
    print('cylA is not inside sphereA')
  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere is True:
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB

  # if sphereB.does_intersect_cube(cubeB):
  #   print('cubeB does intersect sphereB')
  # else:
  #   print('cubeB does not intersect sphereB')

  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
  if (sphereA.circumscribe_cube()).volume() > cylA.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  # print if Point p is inside cubeA
  if cubeA.is_inside_point(P) is True:
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA) is True:
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB) is True:
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA

  if cubeA.is_inside_cylinder(cylA):
    print('cylA is inside cubeA')
  else:
    print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB) is True:
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sp hereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume() is True:
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
  if (cubeA.inscribe_sphere()).area() > cylA.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  # print if Point p is inside cylA
  if cylA.is_inside_point(P) is True:
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')
  # print if sphereA is inside cylA
  if cylA.is_inside_sphere(sphereA) is True:
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA) is True:
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')
  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB) is True:
    print('cylB is inside cylA')
  else:
    print('cylB is not inside cylA')
  # print if cylB intersects with cylA

if __name__ == "__main__":
  main()