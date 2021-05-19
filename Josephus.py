#  File: Josephus.py

#  Description: The problem is: given a number n, the ordering of the men in the circle, and the man from whom the count begins

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/12/2021

#  Date Last Modified:04/12/2021


import sys


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        current = self.first
        # if it's empty
        if (current == None):
            self.first = new_link
            new_link.next = self.first
            return
        # if it's not empty then use the while loop till the end
        while (current.next != self.first):
            current = current.next
        current.next = new_link
        new_link.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        # if it's empty
        if (current == None):
            return None
        # if it has one element
        if current.next == None:
            if current.data == data:
                return current
            else:
                return None
        # move till the tail
        while (current.data != data):
            if current.next == self.first:
                return None
            current = current.next
        return current

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        current = previous = self.first
        # if it's empty
        if (current == None):
            return None
        # if it has one element
        if current.next == None:
            if current.data == data:
                previous.next = current.next
                return current
            else:
                return None
        # set previous.next to self.first position
        while previous.next != self.first:
            previous = previous.next
        # delete the data
        while current.data != data:
            if current.next == self.first:
                return None
            previous = current
            current = current.next
        if self.first != self.first.next:
            self.first = current.next
        else:
            self.first = None
        previous.next = current.next
        return current

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def deleteAfter(self, start, n):
        current = previous = self.first
        if self.first == None:
            return None
        if current.next == None:
            previous.next = current.next
            return current
        current = self.find(start)
        for i in range(1, n):
            current = current.next
        print(str(current.data), end='')
        self.delete(current.data)
        return current.next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        # checks if the current list is empty
        strng = '['
        if self.first == None:
            strng += ']'
            return strng
        current = self.first
        if current.next == self.first:
            strng += (str(current.data) + ']')
            return strng

        while (current.next != self.first):
            strng += (str(current.data) + ", ")
            current = current.next
        strng += (str(current.data) + "]")
        return strng

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)
    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)
    # your code
    soldiers = CircularList()
    for i in range(1, num_soldiers + 1):
        soldiers.insert(i)
    for i in range(1, num_soldiers):
        start_count = soldiers.deleteAfter(start_count, elim_num)
        print()
        start_count = start_count.data
    for i in range(num_soldiers + 1, num_soldiers + 2):
        start_count = soldiers.deleteAfter(start_count, elim_num)
        start_count = start_count.data
    print()


if __name__ == "__main__":
    main()