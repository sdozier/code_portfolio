#Simone Dozier
#Project Euler problems

import time
from helperMethods import *

#Problem 52: Permuted multiples
def isPermutation(n,x):
    #takes 2 lists, assumes n is already sorted
    x.sort()
    return n==x

def fitsReq(x):
    """Checks if number fits the requirements of problem 52
    e.g. x, 2x, ..., 6x all contain the same digits
    """
    n = list(str(x))
    n.sort()
    factor = 2
    for factor in range(2,7):
        if not isPermutation(n,list(str(x*factor))):
            return False
    return True

#use tryTil(10**6)
def tryTil(limit):
    for i in range(1,limit):
        if fitsReq(i):
            print i
            break

#Problem 55: Lychrel numbers
def reverse(s):
    """Takes an integer, expressed as a string, and returns the reverse as an integer

    :Example:
    >>> reverse('1293')
    3921
    """

    r=0
    for i in range(len(s)):
       r+= int(s[i])*(10**i)

    return r

def isLychrel(n):
    #isPalindrome and reverse both work with strings. Leave as strings except when adding for less conversion.
    nxt = str(n+reverse(str(n)))
    if isPalindrome(nxt):
        return False
    n=nxt
    
    for i in range(48):
        nxt = str(int(n)+reverse(n))
        if isPalindrome(nxt):
            return False
        n=nxt
    return True

def countLychrel():
    """Returns the number of Lychrel numbers less than 10000"""
    
    c = 0
    #t=time.time()
    for i in range(1,10000):
        if isLychrel(i):
            c+=1
    #print time.time()-t
    return c

