# File: ComparingLinearBinarySearch.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 04/14/2021
# Date Last Modified: 04/14/2021
# Description of Program:
import random
import math

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

# append list
list = []
for i in range(1000):
    list.append(i)
#shuffle the list
random.shuffle(list)
total = 0
# run 10 times for linear search
for i in range(10):
    total += linearSearch(list, random.randint(0,1000))
average10 = total / 10
# run 100 times for linear search
total = 0
for i in range(100):
    total += linearSearch(list, random.randint(0,1000))
average100 = total / 100
# run 1000 times for linear search
total = 0
for i in range(1000):
    total += linearSearch(list, random.randint(0,1000))
average1000 = total / 1000
# run 10000 times for linear search
total = 0
for i in range(10000):
    total += linearSearch(list, random.randint(0,1000))
average10000 = total / 10000
# run 100000 times for linear search
total = 0
for i in range(100000):
    total += linearSearch(list, random.randint(0,1000))
average100000 = total / 100000
# binary search
list.sort()
total = 0
for i in range(1000):
    total += binarySearch(list,random.randint(0, 1000))[1]
baverage = total/1000
print('Linear search:')
print('  Tests: 10       Average probes: {}'.format(average10))
print('  Tests: 100      Average probes: {}'.format(average100))
print('  Tests: 1000     Average probes: {}'.format(average1000))
print('  Tests: 10000    Average probes: {}'.format(average10000))
print('  Tests: 100000   Average probes: {}'.format(average100000))
print('Binary search:')
print('  Average number of probes: {}'.format(baverage))
print('  Differs from log2(1000) by: {}'.format(abs(baverage -  math.log2(1000))))





