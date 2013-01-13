import sys
import collections


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    divisible = 0
    for i in xrange(3, n + 1, 2):
        if n % i == 0:
            divisible += 1
    print divisible
