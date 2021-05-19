#  File: TestLinkedList.py

#  Description:

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/06/2021

#  Date Last Modified:04/09/2021

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None
    # get number of links
    def get_num_links(self):
        current = self.first
        num = 1
        if current == None:
            return 0
        while current.next != None:
            current = current.next
            num += 1
        return num

    # add an item at the beginning of the list
    def insert_first(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    # add an item at the end of a list
    def insert_last(self, data):
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        newLink = Link(data)
        previous = current = self.first
        if current == None:
            newLink.next = self.first
            self.first = newLink
            return
        if current.data >= data:
            newLink.next = self.first
            self.first = newLink
            return
        while current.next != None:
            if current.data >= data:
                newLink.next = previous.next
                previous.next = newLink
                return
            else:
                previous = current
                current = current.next
        if current.data > data:
            newLink.next = previous.next
            previous.next = newLink
        else:
            current.next = newLink
        return

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        if self.first == None:
            return None
        current = self.first
        while current.data != data:
            current = current.next
            if current == None:
                return None
        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        if self.first == None:
            return None
        current = self.first
        while current.data != data:
            if current.data > data:
                return None
            current = current.next
            if current == None:
                return None
        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    # Test Failed: False is not true
    def __str__(self):
        current = self.first
        empty_str = ""
        count = 0
        while current != None:
            empty_str += str(current.data) + "  "
            current = current.next
            count += 1
            if count >= 10:
                empty_str = empty_str[0:-2]
                empty_str += "\n"
                count = 0
        empty_str = empty_str[0:-2]
        result = empty_str
        return result
    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        newList = LinkedList()
        current = self.first
        while current != None:
            newList.insert_last(current.data)
            current = current.next
        return newList

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        newList = LinkedList()
        current = self.first
        while current != None:
            newList.insert_first(current.data)
            current = current.next
        return newList

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        if self.first == None:
            return None
        newList = LinkedList()
        current = self.first
        while current != None:
            newList.insert_in_order(current.data)
            current = current.next
        return newList

    # Return True if a list is sorted in ascending order or False otherwise
    # Test Failed: 'NoneType' object has no attribute 'next'
    def is_sorted(self):
        current = self.first
        while (current != None) and (current.next != None):
            if current.data > current.next.data:
                return False
            else:
                current = current.next
        return True

    def is_empty(self):
        if self.first == None:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        newList = LinkedList()
        if self.first == other.first == None:
            return None
        sstrng = self.first
        ostrng = other.first
        while sstrng != None and ostrng != None:
            if sstrng.data > ostrng.data:
                newList.insert_last(ostrng.data)
                ostrng = ostrng.next
            else:
                newList.insert_last(sstrng.data)
                sstrng = sstrng.next
        while sstrng != None and ostrng == None:
            newList.insert_last(sstrng.data)
            sstrng = sstrng.next
        while sstrng == None and ostrng != None:
            newList.insert_last(ostrng.data)
            ostrng = ostrng.next
        return newList

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.first == other.first == None:
            return True
        if self.first == None or other.first == None:
            return False
        sstrg= self.first
        ostrg = other.first
        while sstrg != None and ostrg != None:
            if sstrg.data != ostrg.data:
                return False
            sstrg = sstrg.next
            ostrg = ostrg.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        newList = LinkedList()
        if self.first == None:
            return None
        current = self.first
        while current != None:
            if newList.find_unordered(current.data) == None:
                newList.insert_last(current.data)
                current = current.next
            else:
                current = current.next
                continue
        return newList


def main():



# Test methods insert_first() and __str__() by adding more than
# 10 items to a list and printing it.
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    a = LinkedList()
    list1 = [22,23,24]


# Test method insert_last()
    a.insert_last(22)
    print(a)

# Test method insert_in_order()
    for i in list:
        a.insert_in_order(i)
    print(a)
# Test method get_num_links()
    print('getnum', a.get_num_links())

# Test method find_unordered()
# Consider two cases - data is there, data is not there

# Test method find_ordered()
# Consider two cases - data is there, data is not there

# Test method delete_link()
# Consider two cases - data is there, data is not there

# Test method copy_list()

# Test method reverse_list()

# Test method sort_list()

# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted

# Test method is_empty()

# Test method merge_list()

# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal

# Test remove_duplicates()

if __name__ == "__main__":
    main()