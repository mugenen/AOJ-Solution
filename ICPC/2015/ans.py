import sys
import math
import collections

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0:
        break
    vertical = collections.Counter()
    lateral = collections.Counter()
    road_v = []
    road_l = []
    for i in xrange(N):
        h = int(raw_input())
        road_v.append(h)
    for i in xrange(M):
        w = int(raw_input())
        road_l.append(w)
    
    for i in xrange(N):
        for j in xrange(i + 1, N + 1):
            vertical[sum(road_v[i:j])] += 1
    for i in xrange(M):
        for j in xrange(i + 1, M + 1):
            lateral[sum(road_l[i:j])] += 1
    result = 0
    for v in vertical:
        result += vertical[v] * lateral[v]
    print result
