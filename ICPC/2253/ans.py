import sys
import collections


delta = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, -1), (-1, 0)]
while True:
    t, n = map(int, raw_input().split())
    if t == 0 and n == 0:
        break
    obstacle = set()
    for i in xrange(n):
        x, y = map(int, raw_input().split())
        obstacle.add((x, y))
    cand = [tuple(map(int, raw_input().split()))]
    visited = set(cand)
    for i in xrange(t):
        new_cand = []
        for x, y in cand:
            for d_x, d_y in delta:
                key = (x + d_x, y + d_y)
                if key not in obstacle and key not in visited:
                    visited.add(key)
                    new_cand.append(key)
        cand = new_cand
    print len(visited)
