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

def tryTil(limit):
    for i in range(1,limit):
        if fitsReq(i):
            print i
            break

def prob52():
    tryTil(10**6)

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

def prob55():
    print countLychrel()

#==============#
#Problem 67: Maximum path sum ii
#==============#
def readTriangle():
    """Converts triangle data in file to a matrix"""
    
    f = open('p067_triangle.txt','r')
    rows=[]
    for line in f:
        l=line[:-1].split(' ')
        rows.append(map(int,l))
    return rows

def prob67():
    """Finds the maximum path through the triangle

    Dynamic programming solution. Calculates maximum path to each square, starting
     with the first two squares and working down the triangle. Only stores the max
     path to each square so you don't calculate every path."""
    
    rows=readTriangle()
    ws = rows[0] #the working sums
    nws = [0,0] #"next working sum"
    for i in range(1,len(rows)):
        nws[0] = ws[0] + rows[i][0]
        nws[-1] = ws[-1] + rows[i][-1]
        for j in range(1,len(ws)):
            x1 = rows[i][j]+ws[j-1]
            x2 = rows[i][j]+ws[j]
            nws[j] = max(x1,x2)
        ws = nws
        nws = [0]*(i+2)
    print max(ws)

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
    """Prints the number of chains, beginning with n < 1,000,000, that contain exactly 60 terms"""

    setUpFactorials()
    c=0
    for i in range(2,1000000):
        if(i%50000==0):
            print "checking %i..." % i #to track progress
        if(loop60(i)):
            c+=1
    print c

