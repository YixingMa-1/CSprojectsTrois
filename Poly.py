#  File: Poly.py

#  Description:  the addition and multiplication of polynomials

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/12/2021

#  Date Last Modified:04/16/2021
import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None
    self.length = 0

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    self.length += 1
    newLink = Link(coeff, exp)
    # if it's empty, then add the link
    if self.first == None:
      self.first = newLink
      return
    previous = current = self.first
    # if the new exp is smaller than the current one, the pointer needs to move to the next
    while (exp < current.exp or exp == current.exp):
      previous = current
      current = current.next
      # if it's smaller than the tail, then we add it to the tail
      if current == None:
        previous.next = newLink
        return
    # if it's bigger than the head, then we add it before the head.
    if current == self.first:
      newLink.next = current
      self.first = newLink
      return
    # if it's just bigger than the current.exp, we add it before the current.exp
    else:
      previous.next = newLink
      newLink.next = current
      return

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    sum = LinkedList()
    current = self.first
    pcurrent = p.first
    # if one of the polynomials is empty
    if current == None:
      return p
    if pcurrent == None:
      return self
    # add
    while (current != None and pcurrent != None):
    # if current exp is bigger than p.exp, then insert
      if current.exp > pcurrent.exp:
        sum.insert_in_order(current.coeff, current.exp)
        current = current.next
      else:
        sum.insert_in_order(pcurrent.coeff, pcurrent.exp)
        pcurrent = pcurrent.next
    while current != None:
      sum.insert_in_order(current.coeff, current.exp)
      current = current.next
    while pcurrent != None:
      sum.insert_in_order(pcurrent.coeff, pcurrent.exp)
      pcurrent = pcurrent.next
    sum.sim_helper()
    return sum


  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    product = LinkedList()
    # if one of the polynomials is empty, then return the other one
    if self.first == None:
      return p
    if p.first == None:
      return self
    # mutiply them one by one
    current = self.first
    while current != None:
      pcurrent = p.first
      while pcurrent != None:
        product_coeff = current.coeff * pcurrent.coeff
        peoduct_exp = current.exp + pcurrent.exp
        # print(product)
        # print('*')
        pcurrent = pcurrent.next
        product.insert_in_order(product_coeff, peoduct_exp)
      current = current.next
    product.sim_helper()
    return product

  # create a string representation of the polynomial

  def __str__ (self):
    current = self.first
    if current == None:
      return ("")
    postr = str(current)
    while current.next != None:
      current = current.next
      postr += (' ' + '+' + ' ' + str(current))
    return postr

  def sim_helper(self):
    if self.first != None:
      current = self.first
      while current != None:
        cnext = current.next
        while cnext != None and cnext.exp == current.exp:
          current.coeff += cnext.coeff
          current.next = cnext.next
          cnext = cnext.next
        current = current.next

  def clearzero(self):
    current = self.first
    previous = self.first
    if current == None:
      return None
    while current.coeff != 0:
      if current.next == None:
        return None
      else:
        previous = current
        current = current.next
    if current == self.first:
      self.first = self.first.next
    else:
      previous.next = current.next
    return current

def main():
  # read data from file poly.in from stdin
  line = int(sys.stdin.readline())
  p = LinkedList()
  q = LinkedList()
  num_list = []
  for i in range(line):
    coeff, expo = sys.stdin.readline().strip().split()
    p.insert_in_order(int(coeff), int(expo))
  # create polynomial q
  empty = sys.stdin.readline()
  line = int(sys.stdin.readline())
  num_list = []
  for i in range(line):
    coeff, expo = sys.stdin.readline().strip().split()
    q.insert_in_order(int(coeff), int(expo))
  # get sum of p and q and print sum
  sum = q.add(p)
  for i in range(sum.length):
    sum.clearzero()
  print(sum)
  # get product of p and q and print product
  product = q.mult(p)
  for i in range(product.length):
    product.clearzero()
  print(product)
if __name__ == "__main__":
  main()