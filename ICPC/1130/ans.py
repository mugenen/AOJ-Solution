import sys
import collections

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]
while True:
    W, H = map(int, sys.stdin.readline().split())
    if W == 0:
        break
    
    tile = [[0 for i in xrange(W + 2)] for j in xrange(H + 2)]
    
    visited = set()
    next = set()
    
    for i in xrange(H):
        line = raw_input().strip()
        for j in xrange(W):
            if line[j] == '.':
                tile[i + 1][j + 1] = 1
            if line[j] == '@':
                tile[i + 1][j + 1] = 1
                next.add((i + 1, j + 1))
#    for line in tile:
#        print line
    while len(next) > 0:
        temp_next = set()
        for n in next:
            visited.add(n)
            for i in xrange(4):
                temp = (n[0] + x[i], n[1] + y[i])
                if temp not in visited and tile[temp[0]][temp[1]] == 1:
                    temp_next.add(temp)
        next = temp_next
    print len(visited)
