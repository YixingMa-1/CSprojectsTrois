#  File: Reducible.py

#  Description:

#  Student Name: Yixing Ma

#  Student UT EID: ym7653

#  Partner Name: Yaashi Khatri

#  Partner UT EID: yak264

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/02/2021

#  Date Last Modified:04/02/2021

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime  (n) :
  if n == 1:
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into

def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string

def step_size (s, const):
  hash_idx = 0
  for j in range(len(s)):
    letter = ord(s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % const
  Stepsize = const - (hash_idx % const)
  return Stepsize

# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing

def insert_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  next_idx = step_size(s, 13)
  i = 1
  if hash_table[idx] == "":
    hash_table[idx] = s
  else:
    while hash_table[(idx + next_idx * i) % len(hash_table)] != "":
      i += 1
    hash_table[(idx + next_idx * i) % len(hash_table)] = s

# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise

def find_word (s, hash_table):
  idx = hash_word(s, len(hash_table))
  if hash_table[idx] == s:
    return True
  elif hash_table[idx] == "":
    return False
  else:
    next_idx = step_size(s, 13)
    i = 1
    while hash_table[(idx + next_idx * i) % len(hash_table)] != "":
      if idx == (idx + next_idx * i) % len(hash_table):
        break
      if hash_table[(idx + next_idx * i) % len(hash_table)] == s:
        return True
      else:
        i += 1
    return False

# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise

def is_reducible (s, hash_table, hash_memo):
  if ('a' not in s) and ('i' not in s) and ('o' not in s):
    return False
  elif s == "a" or s == "i" or s == "o":
    return True
  elif find_word(s, hash_memo):
    return True
  elif not find_word(s, hash_table):
    return False
  else:
    for i in range(len(s)):
      miniword  = s[:i] + s[i+1:]
      if miniword == 'a' or miniword == 'i' or miniword == 'o':
        return True
      elif ('a' not in miniword) and ('i' not in miniword) and ('o' not in miniword):
        continue
      if not find_word(miniword, hash_table):
        continue
      if find_word(miniword, hash_memo):
        return True
      elif is_reducible(miniword, hash_table, hash_memo):
        insert_word(miniword, hash_memo)
        insert_word(s, hash_memo)
        return True
  return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length

def get_longest_words (string_list):
  new_lst = []
  maxlen = 0
  for i in string_list:
    if len(i) >= maxlen:
      maxlen = len(i)
  for i in string_list:
    if len(i) == maxlen:
      new_lst.append(i)
  return new_lst

def main():
  # create an empty word_list
  word_list  = []
  # read words from words.txt and append to word_list
  for line in sys.stdin:
    line = line.strip()
    word_list.append (line)
  # find length of word_list
  len_lst = len(word_list)
  # determine prime number N that is greater than twice
  # the length of the word_list
  N = len_lst * 2 + 1
  while is_prime(N) == False:
    N += 1
  # create an empty hash_list
  hash_list = []
  # populate the hash_list with N blank strings
  for i in range(N):
    hash_list.append("")
  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for i in word_list:
    insert_word(i, hash_list)
  # create an empty hash_memo of size M
  hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than
  # 0.2 * size of word_list
  M = int(0.2 * len(word_list)) + 1
  while is_prime(M) is False:
    M += 1
  # populate the hash_memo with M blank strings
  for i in range(M):
    hash_memo.append("")
  # create an empty list reducible_words
  reducibleWords = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for ele in word_list:
    if is_reducible(ele, hash_list, hash_memo):
      reducibleWords.append(ele)
  lar_words = get_longest_words(reducibleWords)
  # # # print the reducible words in alphabetical order
  # # # one word per line
  for i in lar_words:
    print(i)
if __name__ == "__main__":
  main()