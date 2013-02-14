import sys
import collections

n = -1
while True:
    if n != -1:
        print '#'
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    result = []
    for i in xrange(n):
        read = raw_input().split()
        L = read[0]
        P, A, B, C, D, E, F, S, M = map(int, read[1:])
        time = A + B + C + (D + E) * M
        profit = F * M * S - P
        result.append((float(profit) / time, L))
    result.sort(key = lambda x: (-x[0], x[1]))
    for r in result:
        print r[1]