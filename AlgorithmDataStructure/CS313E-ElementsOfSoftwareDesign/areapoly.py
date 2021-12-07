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

temp = [(-100, -33), (-96, 77), (-93, 80), (-27, 99), (25, 100), (77, 94), \
 (84, 93), (100, 26), (98, -83), (69, -98), (-15, -99), (-95, -98)]
convex_poly = []
for i in range(len(temp)):
  convex_poly.append(Point(temp[i][0], temp[i][1]))
print(convex_poly)
def area_poly (convex_poly):
  # det = (x1 * y2 + x2 * y3 + ... + xn * y1 - y1 * x2 - y2 * x3 - ... - yn * x1)
  #
  # area = (1 / 2) * abs(det)
  detplus = 0
  for i in range(len(convex_poly)):
    if i == len(convex_poly) - 1:
      detplus += convex_poly[i].x * convex_poly[0].y
    else:
      detplus += convex_poly[i].x * convex_poly[i + 1].y

  # print(detplus)
  detminus = 0
  for i in range(len(convex_poly)):
    if i == len(convex_poly) - 1:
      detminus += convex_poly[i].y * convex_poly[0].x
    else:
      detminus += convex_poly[i].y * convex_poly[i + 1].x
  # print(detminus)

  determinant = detplus - detminus
  # print(determinant)

  return 0.5 * abs(determinant)
  # print(area)

area_poly(convex_poly)