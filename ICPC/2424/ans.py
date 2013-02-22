import sys
import collections


n = int(sys.stdin.readline())
for i in xrange(n):
    t = sys.stdin.readline().strip()
    
    count = 0
    filter = set()
    while True:
        filter.add(t)
        L = len(t)
        if L == 1:
            break
        m = 0
        for i in xrange(1, L):
            a = int(t[:i])
            b = int(t[i:])
            m = max(m, a * b)
        t = str(m)
        if t in filter:
            count = -1
            break
        count += 1
    print count
