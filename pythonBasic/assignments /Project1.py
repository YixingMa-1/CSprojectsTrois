# File: Project1.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 03/21/2021
# Date Last Modified: 03/24/2021
# Description of Program: create a program to compute a student's semester
# grade under some simple assumptions
name = input("Enter the student's name: ")
print()
print('HOMEWORKS:')
hw1 = int(input('  Enter HW1 grade: '))
while True:
    if hw1 < 0 or hw1 > 10:
        print('  Grade must be in range [0..10]. Try again.')
        hw1 = int(input('  Enter HW1 grade: '))
        continue
    else:
        break
hw2 = int(input('  Enter HW2 grade: '))
while True:
    if hw2 < 0 or hw2 > 10:
        print('  Grade must be in range [0..10]. Try again.')
        hw2 = int(input('  Enter HW2 grade: '))
        continue
    else:
        break
hw3 = int(input('  Enter HW3 grade: '))
while True:
    if hw3 < 0 or hw3 > 10:
        print('  Grade must be in range [0..10]. Try again.')
        hw3 = int(input('  Enter HW3 grade: '))
        continue
    else:
        break
print()
print('PROJECTS:')
pj1 = int(input('  Enter Project1 grade: '))
while True:
    if pj1 < 0 or pj1 > 100:
        print('  Grade must be in range [0..100]. Try again.')
        pj1 = int(input('  Enter Project1 grade: '))
        continue
    else:
        break
pj2 = int(input('  Enter Project2 grade: '))
while True:
    if pj2 < 0 or pj2 > 100:
        print('  Grade must be in range [0..100]. Try again.')
        pj2 = int(input('  Enter Project2 grade: '))
        continue
    else:
        break
print()
print('EXAMS:')
ex1 = int(input('  Enter Exam1 grade: '))
while True:
    if ex1 < 0 or ex1 > 100:
        print('  Grade must be in range [0..100]. Try again.')
        ex1 = int(input('  Enter Exam1 grade: '))
        continue
    else:
        break
ex2 = int(input('  Enter Exam2 grade: '))
while True:
    if ex2 < 0 or ex2 > 100:
        print('  Grade must be in range [0..100]. Try again.')
        ex2 = int(input('  Enter Exam2 grade: '))
        continue
    else:
        break
print()
print('Grade report for: Susie Student')
avg_hws = (hw1 + hw2 + hw3) / 3 * 10
print("  Homework average (30% of grade): {:.2f}".format(avg_hws))
avg_pjs = (pj1 + pj2) / 2
print("  Project average (30% of grade): {:.2f}".format(avg_pjs))
avg_exams = (ex1 + ex2) / 2
print("  Exam average (40% of grade): {:.2f}".format(avg_exams))
avg_course = 0.3 * (avg_hws + avg_pjs) + 0.4 * avg_exams
print("  Student course average: {:.2f}".format(avg_course))
if 90 <= avg_course <= 100:
    grade = "A"
elif 80 <= avg_course <= 90:
    grade = "B"
elif 70 <= avg_course <= 80:
    grade = 'C'
elif 60 <= avg_course <= 70:
    grade = 'D'
else:
    grade = 'F'

print("  Course grade (CS303E: Spring, 2021): {}".format(grade))



















