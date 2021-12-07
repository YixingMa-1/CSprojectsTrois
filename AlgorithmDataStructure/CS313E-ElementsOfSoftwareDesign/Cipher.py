#  File: Cipher.py

#  Description: Encrypt and decrypt the 2d list

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/06/2021

#  Date Last Modified: 02/08/2021




import sys
import math
 # Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def encrypt ( strng ):
  # Input: strng is a string of 100 or less of upper case, lower case,
  #        and digits
  L = len(strng)
  # print('L:',L)
  K = int(math.ceil(math.sqrt(L)))
  M = K * K
  # print('K:',K)
  # print('M:', M)
  # add the asterisks
  num_asterisk = M - L
  for i in range(num_asterisk):
    strng.append('*')
  print('append * to string',strng)
  # build 2d list
  rows, cols = (K, K)
  arr = []
  for i in range(cols):
    col = []
    for j in range(rows):
      col.append(0)
    arr.append(col)
  # print('2d list of 0:', arr)
  # append char to 2d list
  for row in range(K):
    for ele in range(row*K, (row+1) * K):
      arr[row][ele % K] = strng[ele]

  print('arr after appending:',arr)

  # build a new arr
  newrows, newcols = (K, K)
  new_arr = []
  for i in range(cols):
    col = []
    for j in range(rows):
      col.append(0)
    new_arr.append(col)
  # print('new empty arr:', new_arr)
  # clockwise 90 degrees
  for row in range(K):
    for col in range(K):
      new_arr[col][K - 1 - row] = arr[row][col]
  print('encryted arr:', new_arr)
  # turning the encrypted 2d list into a string
  Pstring = ''
  for row in range(K):
    for col in range(K):
      if new_arr[row][col] != '*':
        Pstring += new_arr[row][col]

  print(Pstring)












# Output: function returns an encrypted string
def decrypt ( strng ):
  L = len(strng)
  # print('L:', L)
  K = int(math.ceil(math.sqrt(L)))
  M = K * K
  # print('K:', K)
  # print('M:', M)
  # add the asterisks
  num_asterisk = M - L
  for i in range(num_asterisk):
    strng.append('*')
  # print('append * to string', strng)
  # build 2d list
  rows, cols = (K, K)
  arr = []
  for i in range(cols):
    col = []
    for j in range(rows):
      col.append(0)
    arr.append(col)
  # print('2d list of 0:', arr)
  # append char to 2d list
  for row in range(K):
    for ele in range(row * K, (row + 1) * K):
      arr[row][ele % K] = strng[ele]

  # print('arr after appending:', arr)
  # build a new arr
  newrows, newcols = (K, K)
  new_arr = []
  for i in range(cols):
    col = []
    for j in range(rows):
      col.append(0)
    new_arr.append(col)
  # print('new empty arr:', new_arr)

  # counterclockwise 90 degrees
  for row in range(K):
    for col in range(K):
      new_arr[K - 1 - col][row] = arr[row][col]
  # print('decrypted arr:', new_arr)
  Qstring = ''
  for row in range(K):
    for col in range(K):
      if new_arr[row][col] != '*':
        Qstring += new_arr[row][col]
  #       Qstring = ''.join(new_arr)

  print(Qstring)



def main():
  # read the two strings P and Q from standard input
  P = [char for char in sys.stdin.readline().split()[0]]
  Q = [char for char in sys.stdin.readline().split()[0]]
  # print('P:', P)
  # print('Q:', Q)

  # encrypt the string P
  encrypt(P)
  # decrypt the string Q
  decrypt(Q)
  # print the encrypted string of P and the
  # decrypted string of Q to standard out

if __name__ == "__main__":
  main()