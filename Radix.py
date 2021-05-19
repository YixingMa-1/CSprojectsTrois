#  File: Radix.py

#  Description:

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/07/2021

#  Date Last Modified:04/07/2021

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    # create a queue list to temporarily store the ascii value
    Queue_list = []
    for i in range(36):
        Queue_list.append(Queue())
    # print(Queue_list)
    # get the max length to decide how many queues we need
    max_len = 0
    for i in a:
        if len(i) >= max_len:
            max_len = len(i)
    # match letter and convenient version of ascii
    real_ = []
    asc_list = []
    for i in range(48, 58):
        real_.append(chr(i))
        asc_list.append(ord(chr(i)) - 48)
    for i in range(97, 123):
        real_.append(chr(i))
        asc_list.append(ord(chr(i)) - 87)
    # appending a to q_10
    q_10 = Queue()
    for i in a:
        q_10.enqueue(i)

    # sort

    for pass_ in range(max_len - 1, -1, -1):
        while not q_10.is_empty():
            m = q_10.dequeue()
            if len(m) < pass_ + 1:
                Queue_list[0].enqueue(m)
            else:
                num = find_helper(m[pass_], real_, asc_list)
                Queue_list[num].enqueue(m)
        for i in Queue_list:
            while not i.is_empty():
                n = i.dequeue()
                q_10.enqueue(n)
    result = []
    while not q_10.is_empty():
        ele = q_10.dequeue()
        result.append(ele)
    return result


def find_helper(character, real_list, asc_lst):
    for i in range(len(real_list)):
        if real_list[i] == character:
            return asc_lst[i]


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()

