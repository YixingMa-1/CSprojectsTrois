# File: Student.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 03/23/2021
# Date Last Modified: 03/26/2021
# Description of Program:  define a simple Student class. \
# Each Student object contains a name (string), and two exam grades (floats or integers)


class Student:
    def __init__(self, name, exam1=None, exam2=None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2

    def __str__(self):
        print(self.__name, self.__exam2, self.__exam1)
        return "Student:" + self.__name + '\n' +\
               "  Exam1:" + str(self.__exam1) + '\n' + \
               "  Exam2:" + str(self.__exam2)

    def getName(self):
        return self.__name


    def getExam1Grade(self):
        return self.__exam1


    def getExam2Grade(self):
        return self.__exam2

    def getAverage(self):
        return (self.__exam1 + self.__exam2) / 2



