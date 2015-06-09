#Simone Dozier
#Project Euler problems

from helperMethods import *
import math

#==============#
#Problem 52: Permuted multiples
#==============#
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

#==============#
#Problem 55: Lychrel numbers
#==============#
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
    for i in range(1,10000):
        if isLychrel(i):
            c+=1
    return c

#==============#
#Problem 74: Digit factorial chains
#==============#
#avoid recalculating chains and factorials--significantly faster. Credit to harplanet for the idea.
knownLens=dict()
fs=dict()

def setUpFactorials():
    """Initializes factorial dictionary fs"""
    for i in range(10):
        fs[i]=math.factorial(i)

def nextFact(n):
    """Returns the sum of the factorial of the digits of n.

    Expects factorial dictionary fs to be set up.

    :Example:
    >>> nextFact(109)
    1! + 0! + 9! = 362882
    """
    f=0
    while(n>=10):
        f+=fs[n%10]
        n=n/10
    f+=fs[n%10]
    return f

def loop60(n):
    """Returns boolean: whether continually applying nextFact(n) creates a chain of 60 non-repeating terms"""
    
    seen=set()
    chain=[]
    terms=1
    #Chain is guaranteed not to EXCEED 60 for n < 1,000,000, so no need to check beyond that
    while terms <= 60:
        chain.append(n)
        if n in seen:
            for c in chain:
                knownLens[c]=terms
            return False
        if n in knownLens and terms+knownLens[n]<60:
            for c in chain:
                knownLens[c]=terms+knownLens[n]
            return False
        seen.add(n)
        terms+=1
        n=nextFact(n)
    for c in chain:
        knownLens[c]=60
    return True

def loop60old(n):
    """Returns boolean: whether continually applying nextFact(n) creates a chain of 60 non-repeating terms"""
    seen=set()
    for i in range(60):
        if n in seen:
            return False
        seen.add(n)
        n=nextFact(n)
    return True

def prob74():
    """Returns the number of chains, beginning with n < 1,000,000, that contain exactly 60 terms"""

    setUpFactorials()
    c=0
    for i in range(2,1000000):
        if(i%50000==0):
            print i #to track progress
        if(loop60(i)):
            c+=1
    return c
