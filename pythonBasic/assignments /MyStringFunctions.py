# File: MyStringFunctions.py
# Student: Yixing Ma
# UT EID: ym7653
# Course Name: CS303E
#
# Date Created: 04/01/2021
# Date Last Modified: 04/02/2021
# Description of Program: Defining a collection of functions on strings


def myAppend( str, ch ):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in range(len(str)):
        if str[i] == ch:
            count += 1
    return count

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2


def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if len(str) == 0:
        print("Empty string: no min value")
        return None
    else:
        min = 100
        for ch in str:
            if ord(ch) < min:
                min = ord(ch)
        return chr(min)

def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i >= len(str):
        print("Invalid index")
        return None
    else:
        return str[:i] + ch + str[i:]

def myPop( str, i ):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid index")
        return (str, None)
    else:
        return (str[:i] + str[i+1:],str[i])

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    for i in range(len(str)):
        if str[i] == ch:
            return i
    return -1

    # for i in str:
    #     if i == ch:
    #         return str.index(i)
    # return -1
# NEED TO BE FIXED
def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str
    for i in range(len(str) - 1, 0, -1):
        if str[i] == ch:
            return i
    return -1

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.

    if str == '':
        return str
    for i in range(len(str)):
        if str[i] == ch:
            m = i
            return str[:m] + str[m:]
    return str


def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    new_str = ''
    for i in range(len(str)):
        if str[i] != ch:
            new_str += str[i]
    return new_str
    if new_str == '':
        return str



def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order
    return str[::-1]

