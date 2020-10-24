
'''
PROBLEM STATEMENT - Complete String or not 

A string is said to be complete if it contains all the characters from a to z. Given a string, check if it complete or not.

Example :
qwertyuioplkjhgfdsazxcvbnm , the quick brown fox jumps over the lazy dog are complete strings whereas qwerty , food , wyyga are not complete strings.

'''


import string
def complete_string(strs):
  alphabet = set(string.ascii_lowercase)
  if(set(strs)>=alphabet):
    print("Complete String")
  else:
    print("Not Complete String")


if __name__ == "__main__":
  complete_string("qwertyuioplkjhgfdsazxcvbnm")
  complete_string("the quick brown fox jumps over the lazy dog")
  complete_string("qwerty")
  complete_string("food")
  complete_string("wyyga")


'''

Output :


Complete String
Complete String
Not Complete String
Not Complete String
Not Complete String

'''
