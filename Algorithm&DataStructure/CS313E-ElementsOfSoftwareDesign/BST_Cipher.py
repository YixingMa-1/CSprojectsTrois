#  File: BST_Cipher.py

#  Description: use the binary search tree to do the encryption and decryption.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/12/2021

#  Date Last Modified:04/16/2021

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def __str__(self):
        return str(self.data)

class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        new_str = ''
        for i in encrypt_str.lower():
            if ord(i) == 32 or (97 <= ord(i) <= 122):
                new_str += i
        [self.insert(cha) for cha in new_str]
    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
        newNode = Node(ch)
        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (ch < current.data):
                    current = current.lChild
                elif ch == current.data:
                    return
                else:
                    current = current.rChild
            if (ch < parent.data):
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    def search(self, ch):
        current = self.root
        string = ''
        while ((current != None) and (current.data != ch)):
            if (ch < current.data):
                string += '<'
                current = current.lChild
            else:
                string += '>'
                current = current.rChild
        if current == self.root:
            return '*'
        return string
    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        if self.root != None:
            current = self.root
            for cha in st:
                if cha == '*':
                    return str(self.root)
                elif cha == '<':
                    current = current.lChild
                else:
                    current = current.rChild
                if current == None:
                    return ''
            return current.data
    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        if self.root is not None:
            en_str = ''
            for cha in st.lower():
                if ord(cha) == 32 or (97 <= ord(cha) <= 122):
                    en_str += (self.search(cha) + '!')
        return en_str

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        if self.root != None:
            de_str = ''
            for lilstring in st.split('!'):
                de_str += self.traverse(lilstring)
            return de_str

    def inOrder(self, aNode):
        if (aNode != None):
            self.inOrder(aNode.lChild)
            print(self)
            aNode.data
            self.inOrder(aNode.rChild)


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode)[0:-1])

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))
    print(the_tree.inOrder(str_to_decode))


if __name__ == "__main__":
    main()
