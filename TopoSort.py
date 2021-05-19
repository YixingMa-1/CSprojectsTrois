#  File: TopoSort.py

#  Description: topological sort algorithm practice

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 05/02/2021

#  Date Last Modified: 05/03/2021

import sys

class Stack(object):
    # stack constructor
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack if empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)

class Queue(object):
    # queue constructor
    def __init__(self):
        self.queue = []

    # handle str representation
    def __str__(self):
        return self.queue

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # only return the item at the end of the queue
    def get_next_item(self):
        if self.size() > 0:
            return self.queue[0]
        return None

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)

class Vertex(object):
    # vertex constructor
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.in_degree = 0

    # handle str representation
    def __str__(self):
        return str(self.label)

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

class Graph(object):
    # graph constructor
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            if (label == self.Vertices[i].get_label()):
                return True
        return False

    # get index from vertex label
    def get_index(self, label):
        num_vertices = len(self.Vertices)
        for i in range(num_vertices):
            if (label == self.Vertices[i].get_label()):
                return i
        return -1

    def get_in_degree(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        in_degree = sum([self.adjMat[i][vertex_index] for i in range(len(self.Vertices))])
        return in_degree

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start_vertex, end_vertex, weight=1):
        self.Vertices[end_vertex].in_degree += 1
        self.adjMat[start_vertex][end_vertex] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, vertex_index):
        for i in range(len(self.adjMat[vertex_index])):
            if self.Vertices[i].was_visited() == False and self.adjMat[vertex_index][i] != 0:
                return i
        return -1

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        for i in range(len(self.adjMat[vertex_index])):
            if (self.adjMat[vertex_index][i] != 0):
                self.Vertices[i].in_degree -= 1

        del self.Vertices[vertex_index]
        del self.adjMat[vertex_index]
        for i in range(len(self.Vertices)):
            del self.adjMat[i][vertex_index]

    # delete an edge from start index to end index
    def delete_directed_edge(self, start_index, end_index):
        self.adjMat[start_index][end_index] = 0

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):  # implement via dfs
        if (len(self.Vertices) > 0):
            stack = Stack()

            vertex_index = 0

            self.Vertices[vertex_index].visited = True

            stack.push(vertex_index)

            while (not stack.is_empty()):
                next_vertex = self.get_adj_unvisited_vertex(stack.peek())
                if next_vertex == -1:
                    next_vertex = stack.pop()

                else:
                    self.Vertices[next_vertex].visited = True
                    stack.push(next_vertex)

                    for i in range(len(self.Vertices)):

                        if (self.adjMat[next_vertex][i] != 0):
                            if i in stack.stack:

                                return True

            return False

        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):

        # 0. Determine the in_degree for all vertices. The in_degree is
        #    the number of edges that are incident on that vertex.
        theQueue = Queue()
        while len(self.Vertices) > 0:
            newlist = []
            for i in self.Vertices:
            # 1. Remove the vertices that have an in_degree of 0 to a list
                if i.in_degree == 0:
                    newlist.append(i)
            for i in newlist:
                self.delete_vertex(i.label)
            #    remove the out going edges from those vertices. Sort the list
            newlist.sort(key=lambda x: x.label)
            #    in a given order. Enqueue the vertices into a Queue and then
            #    update the in_degree of all remaining vertices.
            for j in newlist:
                theQueue.enqueue(j)
        # 3. Dequeue the vertices and print.
        return [vertex.label for vertex in theQueue.queue]

def main():
    # read the file and get num vertices
    num_vertices = int(sys.stdin.readline().strip())

    # initialize the graph object
    theGraph = Graph()

    # insert vertices from file into graph object
    [theGraph.add_vertex(sys.stdin.readline().strip()) for i in range(num_vertices)]

    # get num edges and read into the graph
    num_edges = int(sys.stdin.readline().strip())
    for i in range(num_edges):
        start_label, end_label = sys.stdin.readline().strip().split(" ")
        start_index = theGraph.get_index(start_label)
        end_index = theGraph.get_index(end_label)
        theGraph.add_directed_edge(start_index, end_index)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
        return
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)

main()