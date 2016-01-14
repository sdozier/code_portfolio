#Helper methods for project Euler problems
#Simone Dozier
import time
import math

def isPalindrome(s):
    """Takes a string with no caps or special characters. Returns boolean"""

    i1=0
    i2=len(s)-1
    while(i1<i2):
        if s[i1] != s[i2]:
            return False
        i1+=1
        i2-=1
    return True

primesList=[2,3,5,7] #primes in order
primes = set(primesList) #primes as a set
def isPrime(n):
    
    #Don't recalculate primes that have already been encountered:
    if n in primes:
        return True

    #A couple things to check before looping
    #This is because the loop starts at 11 and skips even numbers and multiples of 5 for efficiency
    if n<2:
        return False
    if n%2==0 or n%3==0 or n%5==0 or n%7 ==0:
        return False

    sq = math.sqrt(n)
    divisor=11
    while(divisor <= sq):
        #divisors ending in 1, e.g 11
        if n%divisor ==0:
            return False
        divisor+=2
        #divisors ending in 3, e.g 13
        if n%divisor ==0:
            return False
        divisor+=4
        #divisors ending in 7, e.g 17
        if n%divisor==0:
            return False
        divisor+=2
        #divisors ending in 9, e.g 19
        if n%divisor==0:
            return False
        divisor+=2

    #reached end of while loop without finding factor of n. n is prime.
    primes.add(n)
    primesList.append(n)
    return True

def getPrimeFactorSet(n):
    """Returns the prime factors of n as a set.
    
    :Note: Assumes that primeList stores prime numbers <= n in ascending order"""
    
    factors = set()
    i=0
    while(i<len(primesList) and primesList[i]<=n):
        if n%primesList[i]==0:
            factors.add(primesList[i])
        i+=1
    return factors

def timeFun(fun):
    """Time a function"""
    t=time.time()
    fun()
    print "Time: %f " % (time.time()-t)
