#  File: Triangle.py

#  Description:  find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/28/2021

#  Date Last Modified:03/29/2021

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
# In this function, you will implement the exhaustive search,
# that is recursively search for all the possible paths and store the sum of each path length somewhere in your code.
# As you have all the paths sums, you can find the maximum among them
def brute_force(grid):
    new_list = []
    brute_hepler(grid, 0, 0, new_list, 0)
    return max(new_list)
def brute_hepler(grid, row, col ,new_list, sum):
    if row >= len(grid):
        new_list.append(sum)
    else:
        sum += grid[row][col]
        return brute_hepler(grid, row + 1, col, new_list, sum) or brute_hepler(grid, row + 1, col + 1, new_list, sum)
# returns the greatest path sum using greedy approach
def greedy(grid):
    return greedy_helper(grid, grid[0][0], 0)
def greedy_helper(grid, sum, col):
    for row in range(len(grid) - 1):
        if grid[row + 1][col] < grid[row + 1][col + 1]:
            col += 1
        sum += grid[row + 1][col]
    return sum

# returns the greatest path sum using divide and conquer (recursive) approach
# This function is very similar to brute_force. You will recursively search all paths, but in each recursive call only returns a single value.
# And instead of keeping track of all the possible sums, you only obtain the maximum one.
def divide_conquer (grid):
    return divide_helper(grid, 0, 0)
def divide_helper(grid, row, col):
    if row >= len(grid):
        return 0
    else:
        return grid[row][col] + max(divide_helper(grid, row + 1, col), divide_helper(grid, row + 1, col + 1))
# returns the greatest path sum and the new grid using dynamic programming
# This function is a memorized version of divide_conquer(). You can have another list to store the maximum paths in each cell,
# and moving from the bottom of the triangle to the top.
def dynamic_prog (grid):
    for row in range(len(grid) - 1, 0, -1):
        for col in range(row):
            grid[row - 1][col] += max(grid[row][col], grid[row][col + 1])
    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)
    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]
    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]
    return grid
def main():
    # read triangular grid from file
    grid = read_file()
    # '''
    # # check that the grid was read in properly
    # print (grid)
    # '''
    # for r in grid:
    #     for c in r:
    #         print(c, end = ' ')
    #     print()

    # output greatest path from exhaustive search
    print("The greatest path sum through exhaustive search is\n{}".format(brute_force(grid)))
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print("The time taken for exhaustive search in seconds is\n{}".format(times))

    # output greatest path from greedy approach
    print("The greatest path sum through greedy search is\n{}".format(greedy(grid)))
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print("The time taken for greedy approach in seconds is\n{}".format(times))

    # output greatest path from divide-and-conquer approach
    print("The greatest path sum through recursive search is\n{}".format(divide_conquer(grid)))
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The time taken for recursive search in seconds is\n{}".format(times))

    # output greatest path from dynamic programming
    print("The greatest path sum through dynamic programming is\n{}".format(dynamic_prog(grid)))
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print("The time taken for dynamic programming in seconds is\n{}".format(times))


if __name__ == "__main__":
    main()
