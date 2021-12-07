#  File: TestBinaryTree.py

#  Description: use recursion methods to verify if two trees are similar, to get the height, nodes of one level, the total number of the nodes.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/25/2021

#  Date Last Modified:04/25/2021


import sys

SPACE = 5

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = Node(val)
        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lchild
                else:
                    current = current.rchild
            if (val < parent.data):
                parent.lchild = newNode
            else:
                parent.rchild = newNode

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        if self.root == pNode.root == None:
            return True
        elif self.root != None and pNode.root != None:
            return self.is_similar_r(self.root, pNode.root)
        else:
            return False

    def is_similar_r(self, aNode, pNode):
        if (aNode == None and pNode == None):
            return True
        # use the recursiion to track every left and right child's data, if they are the same
        elif (aNode.data == pNode.data):
            return (self.is_similar_r(aNode.rchild, pNode.rchild) and self.is_similar_r(aNode.lchild, pNode.lchild))
        # if they are not the same, then return False
        return False

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        return self.get_level_r(self.root, level, 0)

    def get_level_r(self, r, level, current):
        # if reach the end that is empty, then return a empty list
        if r == None:
            return []
        elif (level == current):
            return [r]
        else:
            # adding the left children and right children to one list.
            return self.get_level_r(r.lchild, level, current + 1) + self.get_level_r(r.rchild, level, current + 1)

    # Returns the height of the tree
    def get_height(self):
        return self.get_height_r(self.root)

    def get_height_r(self, r):
        # if r is empty, then return 0
        if (r == None):
            return 0
        # we get to every node and compare their height, and choose the largest one
        leftH = self.get_height_r(r.lchild)
        rightH = self.get_height_r(r.rchild)
        if (leftH > rightH):
            return leftH + 1
        else:
            return rightH + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        return self.num_nodes_r(self.root)

    def num_nodes_r(self, aNode):
        if (aNode == None):
            return 0
        # use recursion to count how many nodes we encountered, for each node, plus one
        return 1 + self.num_nodes_r(aNode.lchild) + self.num_nodes_r(aNode.rchild)

    def print_tree(self):
        self.print_tree_helper(self.root, 0)

    def print_tree_helper(self, aNode, space):
        if aNode != None:
            space += SPACE
            self.print_tree_helper(aNode.lchild, space)
            # print()
            for i in range(SPACE, space):
                print(end='')
            print(aNode.data)
            self.print_tree_helper(aNode.rchild, space)

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints
    print(tree1_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints
    print(tree2_input)

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints
    print(tree3_input)

    # insert trees
    tree1 = Tree()
    [tree1.insert(i) for i in tree1_input]
    print('tree1')
    tree1.print_tree()

    tree2 = Tree()
    [tree2.insert(i) for i in tree2_input]
    print('tree2')
    tree2.print_tree()

    tree3 = Tree()
    [tree3.insert(i) for i in tree3_input]
    print('tree3')
    tree3.print_tree()
    # Test your method is_similar()
    print(tree1.is_similar(tree2))
    print(tree2.is_similar(tree1))
    print(tree2.is_similar(tree3))
    print(tree1.get_height())
    print(tree1.num_nodes())
    print(tree1.get_level(1))


# Print the various levels of two of the trees that are different
# Get the height of the two trees that are different
# Get the total number of nodes a binary search tree

if __name__ == "__main__":
    main()
