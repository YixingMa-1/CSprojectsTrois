# File: Payroll.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 02/12/2021
# Date Last Modified: 02/12/2021
# Description of Program: Write a program that reads in the following information and prints a payroll statement
a = input("Employee's name: ")
b = float(input("Enter number of hours worked in a week: "))
c = float(input("Enter hourly pay rate: "))
d = float(input("Enter federal tax withholding rate: "))
e = float(input("Enter state tax withholding rate: "))
gross_pay = c * b
federal_with = c * b * 0.2
state_with = c * b * 0.09
total_de = federal_with + state_with
net_pay = gross_pay - total_de
print()
print("Employee Name: ", a)
print("Hours Worked: {:.1f}".format(b))
print("Pay Rate: ${:.2f}".format(c))
print("Gross Pay: ${:.2f}".format(gross_pay))
print("Deductions:")
print('  Federal Withholding (20.0%): ${:.2f}'.format(federal_with))
print('  State Withholding (9.0%): ${:.2f}'.format(state_with))
print('  Total Deduction: ${:.2f}'.format(total_de))
print("Net Pay: ${:.2f}".format(net_pay))