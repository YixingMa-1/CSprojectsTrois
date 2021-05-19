#  File: OfficeSpace.py

#  Description:

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/25/2021

#  Date Last Modified: 02/26/2021



import sys
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap

def overlap (rect1, rect2):
    if rect1[2] < rect2[0] or rect2[2] < rect1[0] or \
            rect1[3] < rect2[1] or rect2[3] < rect1[1]:
        return (0, 0, 0, 0)
    x1 = max(rect1[0], rect2[0])
    y1 = max(rect1[1], rect2[1])
    x2 = min(rect1[2], rect2[2])
    y2 = min(rect1[3], rect2[3])
    return (x1, y1, x2, y2)

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space (bldg):
    num = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j] == 0:
                num += 1
    return num

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space (bldg):
    num = 0
    for i in range(len(bldg)):
        for j in range(len(bldg[0])):
            if bldg[i][j] > 1:
                num += 1
    return num

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    num = 0
    for i in range(rect[0], rect[2]):
        for j in range(rect[1], rect[3]):
            if bldg[j][i] == 1:
                num += 1
    return num


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    arr = []
    for i in range(office[3]):
        col = []
        for j in range(office[2]):
            col.append(0)
        arr.append(col)
    for i in range(len(cubicles)):
        for m in range(cubicles[i][0], cubicles[i][2]):
            for n in range(cubicles[i][1], cubicles[i][3]):
                arr[n][m] += 1
    bldg = arr
    return bldg

# Input: no input
# Output: a string denoting all test cases have passed

def main():
  # read the data
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
      lines[i] = lines[i].strip()
    newList = []
    for i in range(len(lines)):
        newList.append(lines[i].split())
    # print(newList)
    w = int(newList[0][0])
    h = int(newList[0][1])
    office = (0, 0, w, h)
    # print('office:', office)
    numEmpl = int(newList[1][0])
    allRec = []
    for i in range(numEmpl):
        for j in range(1,5):
            allRec.append(int(newList[2+i][j]))
# create an array to contain all rec
    arr = []
    for i in range(numEmpl):
        col = []
        for j in range(4):
            col.append(0)
        arr.append(col)
    # print('empty array:', arr)
    for j in range(numEmpl):
        for i in range(j*4, (j+1)*4):
            if i % 4 == 0:
                arr[j][0] = allRec[i]
                arr[j][1] = allRec[i + 1]
                arr[j][2] = allRec[i + 2]
                arr[j][3] = allRec[i + 3]
                break
    cubicles = []
    for i in range(numEmpl):
        cubicles.append(tuple(arr[i]))
# create bldg
    bldg = request_space(office, cubicles)
    contested_space(bldg)
  # print the following results after computation
  # compute the total office space
    print('Total', area(office))
  # compute the total unallocated space
    print('Unallocated', unallocated_space(bldg))
  # compute the total contested space
    print('Contested', contested_space(bldg))
    unallocated_space(bldg)
  # compute the uncontested space that each employee gets
    for i in range(len(cubicles)):
        print(newList[2+i][0], uncontested_space(bldg, cubicles[i]))

if __name__ == "__main__":
  main()