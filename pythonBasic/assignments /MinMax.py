# File: MinMax.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 03/04/2021
# Date Last Modified:  03/05/ 2021
# Description of Program: Write a program in file MinMax.py \
# that accepts an arbitrary number of integer inputs from the user and prints out \
# the minimum and maximum of the numbers entered
num = []
i = 1
y = input("Enter an integer or 'stop' to end: ")
if y == 'stop':
    print("You didn't enter any numbers")
    quit()
else:
    num.append(int(y))
while i == 1:
    m = input("Enter an integer or 'stop' to end: ")
    if m != 'stop':
        num.append(int(m))
    else:
        break
maximum = max(num)
minimum = min(num)

print('The maximum is', maximum)
print('The minimum is', minimum)