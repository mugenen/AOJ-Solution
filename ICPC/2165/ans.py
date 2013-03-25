import sys
import collections
import math

while True:
    N = int(raw_input())
    if N == 0:
        break
    
    I = map(int, raw_input().split())
    M = 256
    result = []
    for S in xrange(16):
        for A in xrange(16):
            for C in xrange(16):
                R = [S]
                for i in xrange(N):
                    R.append((A * R[i] + C) % M)
                count = [0 for i in xrange(M)]
                for i in xrange(N):
                    count[(I[i] + R[i + 1]) % M] += 1
                H = 0
                for c in count:
                    if c != 0:
                        H -= c / float(N) * math.log(c / float(N))
                result.append((H, S, A, C))
    result.sort()
    print ' '.join(map(str, result[0][1:]))
