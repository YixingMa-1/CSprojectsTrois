#  File: Palindrome.py

#  Description: A string is palindromic if it reads the same forwards and backwards. this question is about returning a palindrome.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/07/2021

#  Date Last Modified: 03/08/2021

import sys
# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    list1 = list(str)
    list2 = list1[::-1]
    # print('list2:', list2)
    # print(list(str))
    # the case that we only have one character
    if len(list1) == 1:
        str1 = ''
        return str1.join(list1)
    # the case we have a palindrome string
    if list1 == list2:
        str2 =''
        return str2.join(list1)
    i = 0
    j = len(list1) - 1
    while i < len(list1) and j < len(list1):
        if i == j:
            m = i
            break
        if list1[i] != list1[j]:
            list1.pop()
            j -= 1
        else:
            i += 1
            j -= 1
    # print('list1:', list1)
    # print('m', m)
    ori_str = []
    ori_str = list(str)
    n = []
    n = ori_str[m*2 + 1: ][ : : -1] + ori_str
    str3 = ''
    return str3.join(n)
# Output: a string denoting all test cases have passed
def test_cases():
    pass
  # write your own test cases
  # return "all test cases passed"
def main():
    # run your test cases
    '''
    print (test_cases())
    '''
    # read the data
    con_list = []
    lines = sys.stdin.readlines()
    for ele in lines:
        con_list.append(ele.strip())

    # print('palindrome list:', con_list)
    for i in range(len(con_list)):
        print(smallest_palindrome(con_list[i]))
    # print the smallest palindromic string that can be made for each input
if __name__ == "__main__":
  main()