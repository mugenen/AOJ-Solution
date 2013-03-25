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
                O = []
                for i in xrange(N):
                    O.append((I[i] + R[i + 1]) % M)
                count = collections.Counter()
                count.update(O)
                H = 0
                for c in count.values():
                    H -= c / float(N) * math.log(c / float(N))
                result.append((H, S, A, C))
    result.sort()
    print ' '.join(map(str, result[0][1:]))
