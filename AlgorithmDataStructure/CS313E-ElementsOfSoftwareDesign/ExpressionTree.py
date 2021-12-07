#  File: ExpressionTree.py

#  Description: use the tree and stack to infix the expression, and get the result, and also show the prefix and profix version of it.

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/12/2021

#  Date Last Modified:04/16/2021

import sys

operator = ['+', '-', '*', '/', '//', '%', '**']

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node(object):
    def __init__(self, data=None, lChild= None, rChild= None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree(object):
    def __init__(self):
        self.root = Node(None)
    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        current = self.root
        estack = Stack()
        expr = expr.split()
        for token in expr:
    # If the current token is a left parenthesis add a new node as the left child of the current node.
    # Push current node on the stack and make current node equal to the left child.
            if token == '(':
                current.lChild = Node(None)
                estack.push(current)
                current = current.lChild
    # If the current token is an aNode.data set the current node's data value to the aNode.data.
    # Push current node on the stack. Add a new node as the right child of the current node and make the current node equal to the right child.
            elif token in operator:
                current.data = token
                current.rChild = Node(None)
                estack.push(current)
                current = current.rChild
    # If the current token is a right parenthesis make the current node equal
    # to the parent node by popping the stack if it is not empty
            elif token == ')':
                if not estack.is_empty():
                    current = estack.pop()
    # If the current token is an operand, set the current node's data value to the operand
    # and make the current node equal to the parent by popping the stack.
            else:
                current.data = token
                current = estack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode.lChild == aNode.rChild == None:
            return float(aNode.data)
        else:
            if aNode.data == "+":
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif aNode.data == "-":
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            elif aNode.data == "*":
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif aNode.data == "/":
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif aNode.data == "//":
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif aNode.data == "%":
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif aNode.data == "**":
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if (aNode != None):
            string = ''
            if aNode.data != None:
                string = str(aNode.data) + ' '
            string += self.pre_order(aNode.lChild)
            string += self.pre_order(aNode.rChild)
            return string
        return ''

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if (aNode != None):
            string = ''
            string += self.post_order(aNode.lChild)
            string += self.post_order(aNode.rChild)
            if aNode.data != None:
                string += str(aNode.data) + ' '
            return string
        return ''

    # you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    tree = Tree()
    tree.create_tree(expr)
    # # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))
    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    # # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()